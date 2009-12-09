/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2009 Adrian S. Tam
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
 */

#include "ns3/qbb-net-device.h"
#include "ns3/md5sum.h"
#include "ns3/log.h"
#include "ns3/boolean.h"
#include "ns3/uinteger.h"
#include "ns3/object-vector.h"
#include "ns3/pause-header.h"
#include "ns3/infinite-queue.h"
#include "ns3/assert.h"
#include "ns3/ipv4.h"
#include "ns3/simulator.h"
#include "ns3/point-to-point-channel.h"
#include "ns3/random-variable.h"

NS_LOG_COMPONENT_DEFINE ("QbbNetDevice");

namespace ns3 {

NS_OBJECT_ENSURE_REGISTERED (QbbNetDevice);

TypeId 
QbbNetDevice::GetTypeId (void)
{
	static TypeId tid = TypeId ("ns3::QbbNetDevice")
	 .SetParent<PointToPointNetDevice> ()
	 .AddConstructor<QbbNetDevice> ()
	 .AddAttribute ("QbbEnabled",
			"Enable the generation of PAUSE packet.",
			BooleanValue (true),
			MakeBooleanAccessor (&QbbNetDevice::m_qbbEnabled),
			MakeBooleanChecker ())
	 .AddAttribute ("QbbThreshold",
			"Threshold of number of packets in queue to send PAUSE.",
			UintegerValue (900),
			MakeUintegerAccessor (&QbbNetDevice::m_threshold),
			MakeUintegerChecker<uint32_t> ())
	 .AddAttribute ("PauseTime",
			"Number of microseconds to pause upon congestion",
			UintegerValue (300),
			MakeUintegerAccessor (&QbbNetDevice::m_pausetime),
			MakeUintegerChecker<uint32_t> ())
	 .AddAttribute ("BufferSize",
			"Size of Tx buffer in number of bytes, shared by all queues",
			UintegerValue (UINT32_MAX),
			MakeUintegerAccessor (&QbbNetDevice::m_buffersize),
			MakeUintegerChecker<uint32_t> ())
	 .AddAttribute ("TxQ",
			"The list of Tx queues for different priority classes",
			ObjectVectorValue (),
			MakeObjectVectorAccessor (&QbbNetDevice::m_queue),
			MakeObjectVectorChecker<Queue> ())
	;
	return tid;
}


QbbNetDevice::QbbNetDevice () : m_bufferUsage(0)
{
	NS_LOG_FUNCTION (this);

	// Set all the queues used are infinite queues
	for (unsigned i=0; i<qCnt; i++) {
		m_queue.push_back( CreateObject<InfiniteQueue>() );
	};
}

QbbNetDevice::~QbbNetDevice ()
{
	NS_LOG_FUNCTION_NOARGS ();
}

void 
QbbNetDevice::DoDispose()
{
	NS_LOG_FUNCTION_NOARGS ();
	// Cancel all the Qbb events
	for (unsigned i=0; i<qCnt; i++) {
		Simulator::Cancel(m_resumeEvt[i]);
		Simulator::Cancel(m_recheckEvt[i]);
	};
	m_queue.clear();
	PointToPointNetDevice::DoDispose ();
}

void 
QbbNetDevice::TransmitComplete (void)
{
	NS_LOG_FUNCTION_NOARGS ();
	NS_ASSERT_MSG(m_txMachineState == BUSY, "Must be BUSY if transmitting");
	m_txMachineState = READY;

	NS_ASSERT_MSG (m_currentPkt != 0, "QbbNetDevice::TransmitComplete(): m_currentPkt zero");

	m_phyTxEndTrace (m_currentPkt);
	m_currentPkt = 0;

	DequeueAndTransmit();
}

void
QbbNetDevice::DequeueAndTransmit (void)
{
	// Quit if channel busy
	if (m_txMachineState == BUSY) return;

	// Look for a packet in a round robin
	unsigned qIndex = m_lastQ;
	for (unsigned i=0; i<qCnt; i++) {
		qIndex++;
		if (qIndex >= qCnt) qIndex = 0;
		if (m_paused[qIndex] && m_qbbEnabled) continue;
		Ptr<Packet> p = m_queue[qIndex]->Dequeue();
		if (p != 0) {
			m_snifferTrace (p);
			m_promiscSnifferTrace (p);
			TransmitStart(p);
			m_lastQ = qIndex;
			m_bufferUsage -= p->GetSize();
			uint32_t avail = GetTxAvailable();
			if (avail) m_sendCb(this, avail);
			return;
		};
	};
	// No queue can deliver any packet, so we just exit
	return;
}

void
QbbNetDevice::Resume (unsigned qIndex)
{
	NS_LOG_FUNCTION(qIndex);
	NS_ASSERT_MSG(m_paused[qIndex], "Must be PAUSEd");
	m_paused[qIndex] = false;
	NS_LOG_LOGIC("Node "<< m_node->GetId() <<" dev "<< m_ifIndex <<" queue "<< qIndex <<
			" resumed at "<< Simulator::Now().GetSeconds());
	DequeueAndTransmit();
}

void
QbbNetDevice::PauseFinish(unsigned qIndex)
{
	// Wrapper to Resume() so that it can be overloaded without
	// interfering with the Scheduler hook
	Resume(qIndex);
}

void
QbbNetDevice::Receive (Ptr<Packet> packet)
{
	NS_LOG_FUNCTION (this << packet);
	uint16_t protocol = 0;

	Ptr<Packet> p = packet->Copy();
	ProcessHeader(p, protocol);
	Ipv4Header ipv4h;
	p->RemoveHeader(ipv4h);

	// If this is a Pause, stop the corresponding queue
	if (ipv4h.GetProtocol() != 0xFE) {
		PointToPointNetDevice::Receive(packet);
	} else {
		// Hit trace hooks
		m_snifferTrace (packet);
		m_promiscSnifferTrace (packet);
		m_phyRxEndTrace (packet);
		m_macRxTrace(packet);
		if (!m_qbbEnabled) return;
		// Read the pause headers
		PauseHeader pauseh;
		p->RemoveHeader(pauseh);
		unsigned qIndex = pauseh.GetQIndex();
		// Pause and schedule the resume event
		m_paused[qIndex] = true;
		Simulator::Cancel(m_resumeEvt[qIndex]);
		m_resumeEvt[qIndex] = Simulator::Schedule(MicroSeconds(pauseh.GetTime()),
						&QbbNetDevice::PauseFinish, this, qIndex);
	};
}

bool
QbbNetDevice::Send(Ptr<Packet> packet, const Address &dest, uint16_t protocolNumber)
{
	NS_LOG_FUNCTION(this << packet << dest << protocolNumber);
	NS_LOG_LOGIC ("UID is " << packet->GetUid ());

	// From PointToPointNetDevice::Send(), make sure channel available
	if (IsLinkUp () == false) {
		m_macTxDropTrace (packet);
		return false;
	}

	// If this packet is a PAUSE, preempt everything and send, as if
	// it is sent out-of-band
	Ipv4Header h;
	packet->PeekHeader(h);
	if (h.GetProtocol() == 0xFE) {
		if (!m_qbbEnabled) return true;
		NS_LOG_INFO("Deliver PAUSE");
		AddHeader(packet, protocolNumber);
		m_snifferTrace (packet);
		m_promiscSnifferTrace (packet);
		m_phyTxBeginTrace (packet);
		Time txTime = Seconds(m_bps.CalculateTxTime(packet->GetSize()));
		bool result = m_channel->TransmitStart(packet, this, txTime);
		if (result == false) {
			m_phyTxDropTrace(packet);
		}
		return result;
	};

	// Get the flow id of the packet
	flowid f = flowid(packet);
	unsigned qIndex = Hash(flowid(packet)) % qCnt;

	// Enqueue, call DequeueAndTransmit(), and check for queue overflow
	AddHeader(packet, protocolNumber);
	m_macTxTrace (packet);
	m_queue[qIndex]->Enqueue(packet);
	m_bufferUsage += packet->GetSize();
	DequeueAndTransmit();
	if (m_qbbEnabled && IsLocal(h.GetSource())==false) {
		CheckQueueFull(qIndex);
	}
	return true;
}

void
QbbNetDevice::CheckQueueFull(unsigned qIndex)
{
	NS_LOG_FUNCTION(this);
  
	if (m_queue[qIndex]->GetNPackets() > m_threshold) {
		// Create the PAUSE packet
		NS_LOG_INFO("Generate PAUSE");
		Ptr<Packet> p = Create<Packet>(0);
		PauseHeader pauseh(m_pausetime /* in usec */, m_queue[qIndex]->GetNPackets(), qIndex);
		p->AddHeader(pauseh);
		Ipv4Header ipv4h;  // Prepare IPv4 header
		ipv4h.SetProtocol(0xFE);
		ipv4h.SetSource(m_node->GetObject<Ipv4>()->GetAddress(m_ifIndex,0).GetLocal());
		ipv4h.SetDestination(Ipv4Address("255.255.255.255"));
		ipv4h.SetTtl(1); 
		ipv4h.SetIdentification(UniformVariable(0,65536).GetValue());
		p->AddHeader(ipv4h);
		// Loop through every net device and send
		Ptr<Ipv4> m_ipv4 = m_node->GetObject<Ipv4>();
		for(uint32_t i=m_node->GetNDevices(); i>0; i--) {
			Ptr<NetDevice> device = m_ipv4->GetNetDevice(i);
			if (device == this) {
				continue;
			};
			Ptr<Packet> pCopy = p->Copy();
			device->Send(pCopy, Mac48Address("01:00:00:00:00:00"), 0x0800);
		};
		NS_LOG_LOGIC("Node "<< m_node->GetId() <<" device "<< m_ifIndex <<" queue "<< qIndex <<
				" send PAUSE at "<< Simulator::Now().GetSeconds());
		Simulator::Cancel(m_recheckEvt[qIndex]);
		m_recheckEvt[qIndex] = Simulator::Schedule(MicroSeconds(m_pausetime/2),
				&QbbNetDevice::CheckQueueFull, this, qIndex);
	};
};

bool
QbbNetDevice::IsLocal(const Ipv4Address& addr) const
{
	Ptr<Ipv4> ipv4 = m_node->GetObject<Ipv4>();
	for (unsigned i=0; i < ipv4->GetNInterfaces(); i++) {
		for (unsigned j=0; j < ipv4->GetNAddresses(i); j++) {
			if (ipv4->GetAddress(i,j).GetLocal() == addr) {
				return true;
			};
		};
	};
	return false;
};

uint64_t
QbbNetDevice::Hash(const flowid& f)
{
	md5sum MD5;             // MD5 engine
	MD5 << (char*)f;    // Feed flowid into MD5

	// Convert 128-bit MD5 digest into 64-bit unsigned integer
	unsigned char* b = MD5.getDigest();
	uint64_t val = 0;
	for (int i=0; i<8; i++) {
		val <<= 8;
		val |= b[i] ^ b[15-i];
	};
	return val;
};

uint32_t
QbbNetDevice::GetTxAvailable(void) const
{
	return (m_bufferUsage > m_buffersize) ? 0 : (m_buffersize - m_bufferUsage);
};

void
QbbNetDevice::ConnectWithoutContext(const CallbackBase& callback)
{
	m_sendCb.ConnectWithoutContext(callback);
};

void
QbbNetDevice::DisconnectWithoutContext(const CallbackBase& callback)
{
	m_sendCb.DisconnectWithoutContext(callback);
};

} // namespace ns3
