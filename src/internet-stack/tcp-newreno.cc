/* -*-  Mode: C++; c-file-style: "gnu"; indent-tabs-mode:nil; -*- */
/* vim: set cin sw=4 syn=cpp ru nu ts=4 cul cuc lbr: */
/*
 * Copyright (c) 2007 Georgia Tech Research Corporation
 * Copyright (c) 2009 Adrian Sai-wah Tam
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
 * Author: Raj Bhattacharjea <raj.b@gatech.edu>
 *         Adrian Sai-wah Tam <adrian.sw.tam@gmail.com>
 */

#include "tcp-newreno.h"
#include "ns3/log.h"
#include "ns3/trace-source-accessor.h"
#include "ns3/simulator.h"
#include "ns3/abort.h"
#include "ns3/node.h"

NS_LOG_COMPONENT_DEFINE ("TcpNewReno");

using namespace std;

namespace ns3 {

NS_OBJECT_ENSURE_REGISTERED (TcpNewReno);

TypeId
TcpNewReno::GetTypeId ()
{
	static TypeId tid = TypeId("ns3::TcpNewReno")
		.SetParent<TcpSocketImpl> ()
		.AddConstructor<TcpNewReno> ()
		.AddTraceSource ("CongestionWindow",
						"The TCP connection's congestion window",
						MakeTraceSourceAccessor (&TcpNewReno::m_cWnd))
		;
	return tid;
}

TcpNewReno::TcpNewReno () : m_initialCWnd (0)
{
	NS_LOG_FUNCTION (this);
}

TcpNewReno::TcpNewReno(const TcpNewReno& sock)
  : TcpSocketImpl(sock),
    m_cWnd (sock.m_cWnd),
    m_ssThresh (sock.m_ssThresh),
    m_initialCWnd (sock.m_initialCWnd)
{
	NS_LOG_FUNCTION (this);
	NS_LOG_LOGIC("Invoked the copy constructor");
}

TcpNewReno::~TcpNewReno ()
{
}

void
TcpNewReno::SetNode (Ptr<Node> node)
{
	TcpSocketImpl::SetNode(node);
	/*
	 * Set the congestion window to IW.  This method is called from the L4 
	 * Protocol after it creates the socket.  The Attribute system takes
	 * care of setting m_initialCWnd and m_segmentSize to their default
	 * values.  m_cWnd depends on m_initialCwnd and m_segmentSize so it
	 * also needs to be updated in SetInitialCwnd and SetSegSize.
	 */
	m_cWnd = m_initialCWnd * m_segmentSize;
}

uint32_t  TcpNewReno::Window ()
{
	NS_LOG_FUNCTION(this);
	return std::min (m_rxWindowSize, m_cWnd.Get());
}

Ptr<TcpSocketImpl> TcpNewReno::Fork ()
{
	return CopyObject<TcpNewReno> (this);
}

// Increase cwnd and call CommonNewAck() upon a new seqnum received
void TcpNewReno::NewAck (SequenceNumber const& seq, bool skipTimer)
{	// New acknowledgement up to sequence number "seq"
	// Adjust congestion window in response to new ack's received
	NS_LOG_FUNCTION (this << seq);
	NS_LOG_LOGIC ("TcpNewReno " << this << " NewAck "
		<< " seq " << seq
		<< " cWnd " << m_cWnd
		<< " ssThresh " << m_ssThresh);
	if (m_cWnd < m_ssThresh) {
		// Slow start mode, add one segSize to cWnd
		m_cWnd += m_segmentSize;
		NS_LOG_LOGIC("TcpNewReno "<< this <<" NewCWnd SlowStart, cWnd "<< m_cWnd <<" sst "<< m_ssThresh);
	} else {
		// Congestion avoidance mode, adjust by (ackBytes*segSize) / cWnd XXX: How can you get ackBytes?
		double adder =  double(m_segmentSize*m_segmentSize)/m_cWnd.Get();
		adder =  std::max(1.0, adder);
		m_cWnd += (uint32_t) adder;
		NS_LOG_LOGIC("NewCWnd CongAvoid, cWnd "<< m_cWnd <<" sst "<< m_ssThresh);
	}
	TcpSocketImpl::NewAck (seq, skipTimer);           // Complete newAck processing
}

// Cut down cwnd and reset m_nextTxSequence to retransmit upon triple dupack
void TcpNewReno::DupAck (const TcpHeader& t, uint32_t count)
{
	NS_LOG_FUNCTION (this << "t " << count);
	NS_LOG_LOGIC ("TcpNewReno " << this << " DupAck " <<  t.GetAckNumber ()
		<< ", count " << count
		<< ", time " << Simulator::Now ());
	if (count == 3) {
		// Count of three indicates triple duplicate ack
		m_ssThresh = std::max(2*m_segmentSize, Window ()/2); // Per RFC2581
		NS_LOG_LOGIC("TcpNewReno " << this << "Tahoe TDA, time " << Simulator::Now ()
			<< " seq " << t.GetAckNumber ()
			<< " in flight " << BytesInFlight ()
			<< " new ssthresh " << m_ssThresh);
		m_cWnd = m_segmentSize; // Collapse cwnd (re-enter slowstart)
		// For Tahoe, we also reset nextTxSeq
		m_nextTxSequence = m_txBuffer.HeadSeq();
		SendPendingData (m_connected);
	}
}

// Retransmit timeout
void TcpNewReno::ReTxTimeout ()
{
	NS_LOG_FUNCTION (this);
	NS_LOG_LOGIC (this<<" ReTxTimeout Expired at time "<<Simulator::Now ().GetSeconds());
	// If erroneous timeout in closed/timed-wait state, just return
	if (m_state == CLOSED || m_state == TIMED_WAIT) return;
	// If all data are received, just return
	if (m_txBuffer.HeadSeq() >= m_nextTxSequence) return;
	
	m_ssThresh = Window () / 2; // Per RFC2581
	m_ssThresh = std::max (m_ssThresh, 2 * m_segmentSize);
	// Set cWnd to segSize on timeout,  per rfc2581
	// Collapse congestion window (re-enter slowstart)
	m_cWnd = m_segmentSize;           
	m_nextTxSequence = m_txBuffer.HeadSeq(); // Start from highest Ack
	m_rtt->IncreaseMultiplier (); // DoubleValue timeout value for next retx timer
	Retransmit ();             // Retransmit the packet
}

void
TcpNewReno::SetSegSize (uint32_t size)
{
	m_segmentSize = size;
	/*
	 * Make sure that the congestion window is initialized for IW properly.  We
	 * can't do this after the connection starts up or would would most likely 
	 * change m_cWnd out from under the protocol.  That would be Bad (TM).
	 */
	NS_ABORT_MSG_UNLESS (m_state == CLOSED, "TcpNewReno::SetSegSize(): Cannot change segment size dynamically.");
	m_cWnd = m_initialCWnd * m_segmentSize;
}

void
TcpNewReno::SetSSThresh (uint32_t threshold)
{
	m_ssThresh = threshold;
}

uint32_t
TcpNewReno::GetSSThresh (void) const
{
	return m_ssThresh;
}

void
TcpNewReno::SetInitialCwnd (uint32_t cwnd)
{
	m_initialCWnd = cwnd;
	/*
	 * Make sure that the congestion window is initialized for IW properly.  We
	 * can't do this after the connection starts up or would would most likely 
	 * change m_cWnd out from under the protocol.  That would be Bad (TM).
	 */
	NS_ABORT_MSG_UNLESS (m_state == CLOSED, "TcpNewReno::SetInitialCwnd(): Cannot change initial cwnd dynamically.");
	m_cWnd = m_initialCWnd * m_segmentSize;
}

uint32_t
TcpNewReno::GetInitialCwnd (void) const
{
	return m_initialCWnd;
}

}//namespace ns3
