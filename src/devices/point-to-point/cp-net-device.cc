/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2009 New York University
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 * Programmer: Adrian Sai-wah Tam <adrian.sw.tam@gmail.com>
 */

#include "ns3/log.h"
#include "ns3/uinteger.h"
#include "ns3/pointer.h"
#include "ns3/double.h"
#include "ns3/ppp-header.h"
#include "ns3/ipv4-header.h"
#include "ns3/ipv4.h"
#include "ns3/queue.h"
#include "ns3/random-variable.h"
#include "ns3/error-model.h"
#include "ns3/cp-net-device.h"
#include "ns3/cn-header.h"

NS_LOG_COMPONENT_DEFINE ("CpNetDevice");

namespace ns3 {

NS_OBJECT_ENSURE_REGISTERED (CpNetDevice);

TypeId
CpNetDevice::GetTypeId (void)
{
	static TypeId tid = TypeId ("ns3::CpNetDevice")
	.SetParent<QbbNetDevice> ()
	.AddConstructor<CpNetDevice> ()
	.AddAttribute (	"SpeedUp",
			"Speedup factor for the 802.1Qau algorithm",
			UintegerValue (1),
			MakeUintegerAccessor (&CpNetDevice::m_speedup),
			MakeUintegerChecker<uint32_t>())
	.AddAttribute (	"QueueEq",
			"Equilibrium point for congestion control",
			UintegerValue (20),
			MakeUintegerAccessor (&CpNetDevice::m_qeq),
			MakeUintegerChecker<uint32_t>())
	.AddAttribute (	"WeightFactor",
			"Control parameter in calculating the congestion level variable Fb",
			DoubleValue (1.0),
			MakeDoubleAccessor (&CpNetDevice::m_w),
			MakeDoubleChecker<double>())
	;
	return tid;
}


CpNetDevice::CpNetDevice ()
{
	// Most things are done by the underlying PointToPointNetDevice
	NS_LOG_FUNCTION (this);
	for (unsigned i=0; i<qCnt; i++) {
		m_qOld[i] = m_timeToMark[i] = 0;
	};
}

CpNetDevice::~CpNetDevice ()
{
}

bool
CpNetDevice::Send(Ptr<Packet> packet, const Address &dest, uint16_t protocolNumber)
{
	NS_LOG_FUNCTION (this << packet << dest << protocolNumber);

	// Rely on PointToPointNetDevice::Send() to put the packet into wire.
	// If failed, return and do nothing, otherwise, check if we need to send
	// a congestion notification
	Ptr<Packet> p = packet->Copy();
	bool ok = QbbNetDevice::Send(packet, dest, protocolNumber);
	if (!ok) return false;

	Ipv4Header ipv4h;
	p->PeekHeader(ipv4h);
	Ipv4Address sAddr = ipv4h.GetSource();
	Ipv4Address myAddr = m_node->GetObject<Ipv4>()->GetAddress(m_ifIndex,0).GetLocal();
	flowid fid = flowid(p);
	// Sanity check: I don't generate CN to myself and no CN for CN
	if (ipv4h.GetProtocol() < 0xFE && myAddr != sAddr) {
		uint16_t qFb = ShouldSendCN(fid, p->GetSize());	// Quantized feedback value
		if (qFb == 0) return true;
		NS_LOG_INFO("Generate congestion notification for " << fid);
		p = Create<Packet>(0);
		CnHeader cn(fid, qFb);	// Prepare CN header
		p->AddHeader(cn);
		Ipv4Header head;	// Prepare IPv4 header
		head.SetDestination(sAddr);
		head.SetSource(myAddr);
		head.SetProtocol(0xFF);
		head.SetTtl(64);
		head.SetPayloadSize(p->GetSize());
		head.SetIdentification(UniformVariable(0,65536).GetValue());
		p->AddHeader(head);
		AddHeader(p, protocolNumber);	// Attach PPP header
		Receive(p);			// Route this packet
	};

	return true;
};

uint8_t
CpNetDevice::ShouldSendCN(flowid& fid, uint32_t pktSize)
{
	// Check if we reached the mark time
	unsigned qIndex = Hash(fid) % qCnt;
	m_timeToMark[qIndex] -= pktSize * m_speedup;
	NS_LOG_INFO("Queue "<< qIndex <<" TimeToMark "<< m_timeToMark[qIndex]
		<<" qlen="<< m_queue[qIndex]->GetNPackets() <<" Q_old="<< m_qOld[qIndex]);
	if (m_timeToMark[qIndex] > 0) {
		return 0;
	};

	// Calculate Fb value
	int32_t Q = m_queue[qIndex]->GetNPackets();
	double Fb = std::min(
			std::max( 0.0, -(int32_t(m_qeq)-Q-m_w*(Q-m_qOld[qIndex])) ),
			(2*m_w+1)*m_qeq );
	// and quantize Fb into 6 bits (2^7=64)
	uint8_t qFb = std::min(uint8_t(Fb/((2*m_w+1)*m_qeq)*64), uint8_t(63));
	NS_LOG_INFO("Q="<< Q <<", Q_old="<< m_qOld[qIndex] <<", Fb="<< Fb <<", qFb="<< (int)qFb);
	// Update parameters
	m_qOld[qIndex] = Q;
	uint32_t size;
	switch (qFb / 8) {
		case 0:	size = 150000; break;
		case 1: size =  75000; break;
		case 2: size =  50000; break;
		case 3: size =  37500; break;
		case 4: size =  30000; break;
		case 5: size =  25000; break;
		case 6: size =  21500; break;
		default:size =  18500; break;
	};
	m_timeToMark[qIndex] = UniformVariable(0.85,1.15).GetValue()*size;
	// Return quantized feedback value
	return qFb;
};

} // namespace ns3
