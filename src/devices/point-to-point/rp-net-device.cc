/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2009 Polytechnic Institute of NYU
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

#define __STDC_LIMIT_MACROS 1
#include <stdint.h>
#include <limits>

#include "ns3/log.h"
#include "ns3/uinteger.h"
#include "ns3/data-rate.h"
#include "ns3/pointer.h"
#include "ns3/double.h"
#include "ns3/ipv4-header.h"
#include "ns3/simulator.h"
#include "ns3/rp-net-device.h"
#include "ns3/cn-header.h"
#include "ns3/queue.h"
#include "ns3/random-variable.h"

NS_LOG_COMPONENT_DEFINE ("RpNetDevice");

namespace ns3 {

const unsigned TIMER_PERIOD=5;
const unsigned FAST_RECOVERY_TH=5;

NS_OBJECT_ENSURE_REGISTERED (RpNetDevice);

const TypeId&
RpNetDevice::GetTypeId (void)
{
  static TypeId tid = TypeId ("ns3::RpNetDevice")
    .SetParent<QbbNetDevice> ()
    .AddConstructor<RpNetDevice> ()
    .AddAttribute ("GD",
                   "Control gain parameter which determines the level of rate decrease",
                   DoubleValue (0.0078125), /* 1/128 */
                   MakeDoubleAccessor (&RpNetDevice::m_gd),
                   MakeDoubleChecker<double> ())
    .AddAttribute ("MinDecFactor",
                   "Minimum rate decrease factor",
                   DoubleValue (0.5),
                   MakeDoubleAccessor (&RpNetDevice::m_minDec),
                   MakeDoubleChecker<double> ())
    .AddAttribute ("MinRate",
                   "Minimum rate of a throttled flow",
                   DataRateValue (DataRate ("10Mb/s")),
                   MakeDataRateAccessor (&RpNetDevice::m_minRate),
                   MakeDataRateChecker ())
    .AddAttribute ("BC",
                   "Byte counter constant for increment process.",
                   UintegerValue (10e3),
                   MakeUintegerAccessor (&RpNetDevice::m_bc),
                   MakeUintegerChecker<uint32_t> ())
    .AddAttribute ("RateAI",
                   "Rate increment unit in AI period",
                   DataRateValue (DataRate ("1Mb/s")),
                   MakeDataRateAccessor (&RpNetDevice::m_rai),
                   MakeDataRateChecker ())
    .AddAttribute ("RateHAI",
                   "Rate increment unit in hyperactive AI period",
                   DataRateValue (DataRate ("5Mb/s")),
                   MakeDataRateAccessor (&RpNetDevice::m_rhai),
                   MakeDataRateChecker ())
    ;
  return tid;
}


RpNetDevice::RpNetDevice ()
{
	NS_LOG_FUNCTION (this);
	for (unsigned i=0; i<qCnt; i++) {
		m_credits[i] = 0;
	};
}

RpNetDevice::~RpNetDevice ()
{
}

void
RpNetDevice::Receive (Ptr<Packet> packet)
{
	NS_LOG_FUNCTION (this << packet);
	uint16_t protocol = 0;

	Ptr<Packet> p = packet->Copy();
	ProcessHeader(p, protocol);
	Ipv4Header ipv4h;
	p->PeekHeader(ipv4h);

	if (ipv4h.GetProtocol() != 0xFF) {
		// Not CN packet, let parent class handle it
		QbbNetDevice::Receive(packet);
	} else {
		// This is a Congestion signal
		// Firstly, hit the trace hooks
		m_snifferTrace (packet);
		m_promiscSnifferTrace (packet);
		m_phyRxEndTrace (packet);
		m_macRxTrace(p);

		// Then, extract data from the congestion packet.
		// We assume, without verify, the packet is destinated to me
		p->RemoveHeader(ipv4h);
		CnHeader cnHead;
		p->RemoveHeader(cnHead);
		flowid fid = cnHead.GetFlow();
		unsigned qIndex = Hash(fid) % qCnt;
		NS_LOG_INFO("CN for flow " << fid <<" received");
		if (cnHead.GetQfb() == 0) return;	// Unuseful CN

		// Modify the flow speed
		if (m_rate[qIndex] == m_bps || m_incCount[qIndex] != 0) {
			m_txBytes[qIndex] = m_bc;
			m_targetRate[qIndex] = m_rate[qIndex];
		};
		m_timeCount[qIndex] = m_incCount[qIndex] = 0;
		double dec = std::max(m_minDec, 1-m_gd*cnHead.GetQfb());
		m_rate[qIndex] = std::max(m_minRate, m_rate[qIndex] * dec);
		NS_LOG_INFO("Rate for flow "<< fid <<" set from "<< m_targetRate[qIndex]
						<<" to "<< m_rate[qIndex] <<", txCount="<< m_txBytes[qIndex]);
		// Reset timer
		m_timer[qIndex] = Simulator::Now() + Seconds(TIMER_PERIOD);
	};
}

void
RpNetDevice::DequeueAndTransmit()
{
	NS_LOG_FUNCTION(this);

	// Quit if channel busy
	if (m_txMachineState == BUSY) return;

	// Water-filling method: Calculate the required credits to send a
	// packet. Packets from different queues are sent using deficit
	// round robin.
	double creditsDue = std::numeric_limits<double>::infinity();
	unsigned qIndex = m_lastQ;
	Time t = Simulator::GetMaximumSimulationTime();
	for (unsigned i=0; i<qCnt; i++) {
		// Looping queue index
		if (++qIndex >= qCnt) qIndex = 0;
		// Skip this queue if it is unable to send packet
		if (m_paused[qIndex] && m_qbbEnabled) continue;
		if (m_queue[qIndex]->GetNPackets() == 0) continue;
		NS_LOG_LOGIC("Good queue "<< qIndex << " avail at " << m_nextAvail[qIndex] << " t=" << t);
		// Lazy initialization
		if (m_rate[qIndex] == 0) m_rate[qIndex] = m_bps;
		// Do the water filling method to find the credits due
		t = Min(m_nextAvail[qIndex], t);
		NS_LOG_LOGIC("t=" << t);
		if (m_nextAvail[qIndex] <= Simulator::Now()) {
			uint32_t pktSize = m_queue[qIndex]->Peek()->GetSize();
			creditsDue = std::min(m_bps/m_rate[qIndex] * (pktSize-m_credits[qIndex]), creditsDue);
		};
	};
	NS_LOG_LOGIC("Credits due = " << creditsDue);
	// If nothing to send, reschedule DequeueAndTransmit()
	if (creditsDue == std::numeric_limits<double>::infinity()) {
		NS_LOG_LOGIC("Nothing to send");
		if (m_nextSend.IsExpired()) {
			if (t > Simulator::Now()) {
				NS_LOG_LOGIC("Next DequeueAndTransmit at "<< t <<" or "<<(t-Simulator::Now())<<" later");
				NS_ASSERT(t > Simulator::Now());
				m_nextSend = Simulator::Schedule(t-Simulator::Now(), &RpNetDevice::DequeueAndTransmit, this);
			};
		};
		return;
	};
	// Distribute credits and dequeue the packet
	Ptr<Packet> packet = 0;
	qIndex = m_lastQ;
	for (unsigned i=0; i<qCnt; i++) {
		// Looping queue index
		if (++qIndex >= qCnt) qIndex = 0;
		// Skip this queue if it is unable to send packet
		if (m_paused[qIndex] && m_qbbEnabled) continue;
		if (m_queue[qIndex]->GetNPackets() == 0) continue;
		if (m_nextAvail[qIndex] > Simulator::Now()) continue;
		// Distribute credits
		m_credits[qIndex] += m_rate[qIndex]/m_bps * creditsDue;
		if (packet != 0) {
			// The packet to send is found, continue distributing credits
			continue;
		};
		// Proceed to next queue if not enough credits to send a packet
		uint32_t pktSize = m_queue[qIndex]->Peek()->GetSize();
		NS_ASSERT(sizeof(double)==sizeof(unsigned long long));
		union { double d; unsigned long long l;} c;
		c.d = m_credits[qIndex];
		c.l++;
		if (pktSize > c.d) continue;
		// Credit is enough, dequeue
		packet = m_queue[qIndex]->Dequeue();
		m_credits[qIndex] = 0;
		m_lastQ = qIndex;
		// Update state variables if necessary
		if (m_rate[qIndex] == m_bps) continue;
		m_txBytes[qIndex] -= pktSize;
		NS_LOG_INFO("txCount for flow "<< qIndex <<" is "<< m_txBytes[qIndex]);
		Time nextSend = m_tInterframeGap + Seconds(m_bps.CalculateTxTime(creditsDue));
		m_nextAvail[qIndex] = Simulator::Now() + nextSend;
		NS_LOG_LOGIC("Dequeued from queue "<< qIndex <<" of rate "<< m_rate[qIndex]
					<<", next send at "<< m_nextAvail[qIndex].GetSeconds());
		// If we have sent enough bytes from this queue, increase the rate
		while (m_timer[qIndex] <= Simulator::Now()) {
			m_timeCount[qIndex] ++;
			m_timer[qIndex] += Seconds(UniformVariable(0.85,1.15).GetValue() * ((m_timeCount[qIndex]>FAST_RECOVERY_TH)?0.5:1) * TIMER_PERIOD);
			RateIncrease(qIndex);
		};
		if (m_txBytes[qIndex] < 0) {
			m_incCount[qIndex] ++;
			m_txBytes[qIndex] = UniformVariable(0.85,1.15).GetValue() * m_bc * ((m_incCount[qIndex]>FAST_RECOVERY_TH)?0.5:1);
			RateIncrease(qIndex);
		};
	};
	// Send the packet by calling TransmitStart(p)
	m_snifferTrace (packet);
	m_promiscSnifferTrace (packet);
	TransmitStart (packet);
};

void
RpNetDevice::RateIncrease(unsigned qIndex)
{
	// Cf: The self_increase(qIndex) function in the pseudocode v2.2
	uint32_t minCount = std::min(m_incCount[qIndex], m_timeCount[qIndex]);
	DataRate increment = 0;
	if (minCount > FAST_RECOVERY_TH) {
		increment = m_rhai * (minCount - FAST_RECOVERY_TH);
	} else if (std::max(m_incCount[qIndex], m_timeCount[qIndex]) > FAST_RECOVERY_TH) {
		increment = m_rai;
	};
	if ((m_incCount[qIndex]==1 || m_timeCount[qIndex]==1) && m_targetRate[qIndex] > 10*m_rate[qIndex]) {
		m_targetRate[qIndex] /= 8;
	} else {
		m_targetRate[qIndex] += increment;
	};
	m_rate[qIndex] = std::min(m_bps, (m_rate[qIndex] + m_targetRate[qIndex])/2);
	NS_LOG_INFO("Rate for flow "<< qIndex <<" set to "<< m_rate[qIndex] <<" target "<< m_targetRate[qIndex]);
};

} // namespace ns3