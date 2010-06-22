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

#define __STDC_LIMIT_MACROS 1
#include <stdint.h>
#include "ns3/qbb-net-device.h"
#include "ns3/md5sum.h"
#include "ns3/hsieh.h"
#include "ns3/log.h"
#include "ns3/boolean.h"
#include "ns3/uinteger.h"
#include "ns3/object-vector.h"
#include "ns3/pause-header.h"
#include "ns3/infinite-queue.h"
#include "ns3/drop-tail-queue.h"
#include "ns3/assert.h"
#include "ns3/ipv4.h"
#include "ns3/simulator.h"
#include "ns3/point-to-point-channel.h"
#include "ns3/random-variable.h"
#include "ns3/flow-id-tag.h"

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
			UintegerValue (100),
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


QbbNetDevice::QbbNetDevice () : m_bufferUsage(0), m_lastQ(qCnt-1)
{
	NS_LOG_FUNCTION (this);

	// Set all the queues used are infinite queues
	for (unsigned i=0; i<qCnt; i++) {
		m_queue.push_back( CreateObject<InfiniteQueue>() );
//		m_queue.push_back( CreateObject<DropTailQueue>() );
		m_paused[i] = false;
	};
}

QbbNetDevice::~QbbNetDevice ()
{
	NS_LOG_FUNCTION(this);
}

void 
QbbNetDevice::DoDispose()
{
	NS_LOG_FUNCTION(this);
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
	NS_LOG_FUNCTION(this);
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
	NS_LOG_FUNCTION(this);

	// Quit if channel busy
	if (m_txMachineState == BUSY) return;

	bool empty = true;

	// Look for a packet in a round robin
	unsigned qIndex = m_lastQ;
	for (unsigned i=0; i<qCnt; i++) {
		if (++qIndex >= qCnt) qIndex = 0;
		if (m_queue[qIndex]->GetNPackets()) empty = false;
		if (m_paused[qIndex] && m_qbbEnabled) continue;
		Ptr<Packet> p = m_queue[qIndex]->Dequeue();
		if (p != 0) {
			NS_LOG_INFO("Dequeue from queue " << qIndex << ", now has len=" << m_queue[qIndex]->GetNPackets());
			m_snifferTrace (p);
			m_promiscSnifferTrace (p);
			TransmitStart(p);
			m_lastQ = qIndex;
			m_bufferUsage -= p->GetSize();
			uint32_t avail = GetTxAvailable(qIndex);
			NS_LOG_INFO("Current TxAvailable=" << avail);
			if (avail) m_sendCb(this, avail);
			return;
		};
	};
	// No queue can deliver any packet, so we just exit
	if (! empty) {
		NS_LOG_INFO("PAUSE prohibits send at node " << m_node->GetId());
		//PrintStatus(std::clog);
	};
	return;
}

void
QbbNetDevice::Resume (unsigned qIndex)
{
	NS_LOG_FUNCTION(this << qIndex);
	NS_ASSERT_MSG(m_paused[qIndex], "Must be PAUSEd");
	m_paused[qIndex] = false;
	NS_LOG_INFO("Node "<< m_node->GetId() <<" dev "<< m_ifIndex <<" queue "<< qIndex <<
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
	p->PeekHeader(ipv4h);

	// If this is a Pause, stop the corresponding queue
	if (ipv4h.GetProtocol() != 0xFE) {
		packet->AddPacketTag(FlowIdTag(m_ifIndex));
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
		p->RemoveHeader(ipv4h);
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
		NS_LOG_INFO("Node "<< m_node->GetId() <<" dev "<< m_ifIndex <<" deliver PAUSE");
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
	
	// Gather statistics on the input port number
	FlowIdTag t;
	packet->RemovePacketTag(t);
	uint32_t inDev = t.GetFlowId();
	if (inDev > 0 && inDev < 1000 && /* prevent bug after optimization */
			inDev < m_node->GetObject<Ipv4>()->GetNInterfaces()) {
		if ( true || m_recheckEvt[qIndex].IsExpired()) {
#if 0
			for (unsigned i = 0; i < m_arrival[qIndex].size(); ++i) {
				m_arrival[qIndex][i] *= 0.75;
			};
			while (m_arrival[qIndex].size() <= inDev) {
				m_arrival[qIndex].push_back(0);
			};
			m_arrival[qIndex][inDev] += 1;
#endif
			for (std::list<uint32_t>::iterator i = m_arrival[qIndex].begin(); i != m_arrival[qIndex].end(); ++i) {
				if (*i == inDev) {
					m_arrival[qIndex].erase(i);
					break;
				};
			};
			m_arrival[qIndex].push_front(inDev);
		} else {
			std::list<uint32_t>::iterator i = m_arrival[qIndex].begin();
			for (; i != m_arrival[qIndex].end(); ++i) {
				if (*i == inDev) break;
			};
			if (i == m_arrival[qIndex].end()) {
				m_arrival[qIndex].push_back(inDev);
			};
		};
	};

	// Enqueue, call DequeueAndTransmit(), and check for queue overflow
	AddHeader(packet, protocolNumber);
	m_macTxTrace (packet);
	m_queue[qIndex]->Enqueue(packet);
	m_bufferUsage += packet->GetSize();
	NS_LOG_INFO("Queue "<< qIndex <<" length " << m_queue[qIndex]->GetNPackets());
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
	NS_LOG_INFO("Queue "<< qIndex <<" length " << m_queue[qIndex]->GetNPackets());
  
	if (m_queue[qIndex]->GetNPackets() > m_threshold) {
		// Create the PAUSE packet
		Ptr<Packet> p = Create<Packet>(0);
		PauseHeader pauseh(m_pausetime /* in usec */, m_queue[qIndex]->GetNPackets(), qIndex);
		p->AddHeader(pauseh);
		Ipv4Header ipv4h;  // Prepare IPv4 header
		ipv4h.SetProtocol(0xFE);
		ipv4h.SetSource(m_node->GetObject<Ipv4>()->GetAddress(m_ifIndex,0).GetLocal());
		ipv4h.SetDestination(Ipv4Address("255.255.255.255"));
  		ipv4h.SetPayloadSize (p->GetSize());
		ipv4h.SetTtl(1); 
		ipv4h.SetIdentification(UniformVariable(0,65536).GetValue());
		p->AddHeader(ipv4h);
		// Loop through every net device and send
		NS_LOG_INFO("Node "<< m_node->GetId() <<" device "<< m_ifIndex <<" queue "<< qIndex <<
				" send PAUSE at "<< Simulator::Now().GetSeconds());
		Ptr<Ipv4> m_ipv4 = m_node->GetObject<Ipv4>();
#if 1
		std::list<uint32_t>::iterator i = m_arrival[qIndex].begin();
		for(uint32_t j = m_queue[qIndex]->GetNPackets(); j > m_threshold; j-=2) {
			Ptr<NetDevice> device = m_ipv4->GetNetDevice(*i);
			Ptr<Packet> pCopy = p->Copy();
			device->Send(pCopy, Mac48Bcast, 0x0800);
			if (++i == m_arrival[qIndex].end()) {
				break;
			};
		};
#endif
#if 0
		for(uint32_t i=m_node->GetNDevices()-1; i>0; i--) {
			Ptr<NetDevice> device = m_ipv4->GetNetDevice(i);
			if (device == this) {
				continue;
			};
			Ptr<Packet> pCopy = p->Copy();
			device->Send(pCopy, Mac48Bcast, 0x0800);
		};
#endif
#if 0
		std::list<uint32_t> sortedDev;
		std::list<uint32_t>::iterator j;
		for (unsigned i = 0; i < m_arrival[qIndex].size(); ++i) {
			j = sortedDev.begin();
			while(j != sortedDev.end()) {
				if (m_arrival[qIndex][*j] > m_arrival[qIndex][i]) {
					break;
				} else {
					++j;
				};
			};
			sortedDev.insert(j, i);
		};
		j = sortedDev.begin();
		for(uint32_t k = m_queue[qIndex]->GetNPackets(); k > m_threshold; k-=2) {
			if (j == sortedDev.end()) {
				break;
			};
			Ptr<NetDevice> device = m_ipv4->GetNetDevice(*j);
			Ptr<Packet> pCopy = p->Copy();
			device->Send(pCopy, Mac48Bcast, 0x0800);
			++j;
		};
#endif

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
	return HsiehHash((char*)f, 16);
#if 0
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
#endif
};

uint32_t
QbbNetDevice::GetTxAvailable(unsigned qIndex) const
{
	//return (m_bufferUsage > m_buffersize) ? 0 : (m_buffersize - m_bufferUsage);
	uint32_t nbytes = m_queue[qIndex]->GetNBytes();
	return (nbytes > m_buffersize) ? 0 : (m_buffersize - nbytes);
};

uint32_t
QbbNetDevice::GetTxAvailable(const flowid& f) const
{
	return GetTxAvailable(Hash(f) % qCnt);
};

void
QbbNetDevice::ConnectWithoutContext(const CallbackBase& callback)
{
	NS_LOG_FUNCTION(this);
	NS_LOG_LOGIC("callback list of size " << m_sendCb.size());
	m_sendCb.ConnectWithoutContext(callback);
	NS_LOG_LOGIC("callback list size is now " << m_sendCb.size());
};

void
QbbNetDevice::DisconnectWithoutContext(const CallbackBase& callback)
{
	NS_LOG_FUNCTION(this);
	NS_LOG_LOGIC("callback list of size " << m_sendCb.size());
	m_sendCb.DisconnectWithoutContext(callback);
	NS_LOG_LOGIC("callback list size is now " << m_sendCb.size());
};

int32_t
QbbNetDevice::PrintStatus(std::ostream& os)
{
	os << "lastQ=" << m_lastQ;
	for (unsigned i=0; i<qCnt; ++i) {
		os << " " << (m_paused[i]?"q":"Q") << "[" << i << "]=" << m_queue[i]->GetNPackets();
	};
	os << std::endl << "Size:";
	uint32_t sum = 0;
	for (unsigned i=0; i<qCnt; ++i) {
		os << " " << (m_paused[i]?"q":"Q") << "[" << i << "]=" << m_queue[i]->GetNBytes();
		sum += m_queue[i]->GetNBytes();
	};
#if 0
	os << " sum=" << sum << std::endl << "RxStat:";
	sum = 0;
	for (unsigned i=0; i<qCnt; ++i) {
		os << " " << (m_paused[i]?"q":"Q") << "[" << i << "]=" << m_queue[i]->GetTotalReceivedBytes();
		sum += m_queue[i]->GetTotalReceivedBytes();
	};
	os << " sum=" << sum << std::endl << "TxStat:";
	sum = 0;
	for (unsigned i=0; i<qCnt; ++i) {
		os << " " << (m_paused[i]?"q":"Q") << "[" << i << "]=" << m_queue[i]->GetTotalSentBytes();
		sum += m_queue[i]->GetTotalSentBytes();
		m_queue[i]->ResetStatistics();
	};
#endif
	os << " sum=" << sum << std::endl;
	return sum;
};

} // namespace ns3
