/* -*-  Mode: C++; c-file-style: "gnu"; indent-tabs-mode:nil; -*- */
//
// Copyright (c) 2009 New York University
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License version 2 as
// published by the Free Software Foundation;
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
//
// Author: Adrian S. Tam <adrian.sw.tam@gmail.com>
//

/*
#include "ns3/node.h"
*/
#include "mmpp-application.h"
#include "ns3/pointer.h"
#include "ns3/address.h"
#include "ns3/socket.h"
#include "ns3/packet.h"
#include "ns3/random-variable.h"
#include "ns3/log.h"
#include "ns3/ptr.h"
#include "ns3/socket-factory.h"
#include "ns3/udp-socket-factory.h"
#include "ns3/trace-source-accessor.h"
#include "ns3/simulator.h"
#include "ns3/nstime.h"
#include "ns3/data-rate.h"
#include "ns3/uinteger.h"
#include "ns3/boolean.h"

NS_LOG_COMPONENT_DEFINE ("MmppApplication");

using std::vector;

namespace ns3 {

NS_OBJECT_ENSURE_REGISTERED (MmppApplication);

TypeId
MmppApplication::GetTypeId (void)
{
	static TypeId tid = TypeId ("ns3::MmppApplication")
		.SetParent<Application> ()
		.AddConstructor<MmppApplication> ()
		.AddAttribute ("GenMatrix", "Generator matrix for the markov process",
		               PointerValue (),
		               MakePointerAccessor (&MmppApplication::m_matrix),
		               MakePointerChecker<GenMatrix> ())
		.AddAttribute ("Rates", "Vector of sending rates in bps",
		               PointerValue (),
		               MakePointerAccessor (&MmppApplication::m_rate),
		               MakePointerChecker<RateVector> ())
		.AddAttribute ("PacketSizes", "Vector of packet sizes in bytes",
		               PointerValue (),
		               MakePointerAccessor (&MmppApplication::m_pktSize),
		               MakePointerChecker<SizeVector> ())
		.AddAttribute ("Remote", "The address of the destination",
		               AddressValue (),
		               MakeAddressAccessor (&MmppApplication::m_peer),
		               MakeAddressChecker ())
		.AddAttribute ("MaxBytes", 
		               "The total number of bytes to send. Once these bytes are sent, "
		               "no packet is sent again, even in on state. The value zero means "
		               "that there is no limit.",
		               UintegerValue (0),
		               MakeUintegerAccessor (&MmppApplication::m_maxBytes),
		               MakeUintegerChecker<uint32_t> ())
		.AddAttribute ("Protocol", "The type of protocol to use.",
		               TypeIdValue (UdpSocketFactory::GetTypeId ()),
		               MakeTypeIdAccessor (&MmppApplication::m_tid),
		               MakeTypeIdChecker ())
		.AddTraceSource ("Tx", "A new packet is created and is sent",
		                 MakeTraceSourceAccessor (&MmppApplication::m_txTrace))
		;
	return tid;
}


MmppApplication::MmppApplication () :
	m_matrix(0),
	m_rate(0),
	m_pktSize(0),
	m_state(0),
	m_socket(0),
	m_totBytes(0)
{
	NS_LOG_FUNCTION (this);
}

MmppApplication::~MmppApplication()
{
	NS_LOG_FUNCTION (this);
}

void 
MmppApplication::SetMaxBytes(uint32_t maxBytes)
{
	NS_LOG_FUNCTION (this << maxBytes);
	m_maxBytes = maxBytes;
}


void
MmppApplication::DoDispose (void)
{
	NS_LOG_FUNCTION (this);

	m_socket = 0;
	// chain up
	Application::DoDispose ();
}

// Application Methods
void MmppApplication::StartApplication() // Called at time specified by Start
{
	NS_LOG_FUNCTION (this);

	// Create the socket if not already
	if (!m_socket) {
		m_socket = Socket::CreateSocket (GetNode(), m_tid);
		m_socket->SetAttribute("Blocking", BooleanValue(true));
		m_socket->Bind ();
		m_socket->Connect (m_peer);
		m_socket->SetSendCallback(MakeCallback(&MmppApplication::ResumeSend,this));
	}
	// Insure no pending event
	CancelEvents ();
#ifdef NS3_ASSERT_ENABLE
	// Verify we are in a valid state and have a good matrix
	NS_ASSERT_MSG(m_matrix, "Undefined generator matrix");
	NS_ASSERT_MSG(m_pktSize, "Undefined packet size vector");
	NS_ASSERT_MSG(m_rate, "Undefined rate vector");
	NS_ASSERT_MSG(m_state < m_matrix->size(), "Invalid state");
	NS_ASSERT_MSG(m_matrix->size() == m_rate->size(), "Dimension mismatch: generator matrix and rate vector");
	NS_ASSERT_MSG(m_matrix->size() == m_pktSize->size(), "Dimension mismatch: generator matrix and packet size vector");
	for (uint32_t i=0; i<m_matrix->size(); i++) {
		NS_ASSERT_MSG(m_matrix->size() == (*m_matrix)[i].size(), "Generator matrix is not square");
		NS_ASSERT_MSG((*m_matrix)[i][i] <= 0, "Positive diagonal entry in generator matrix");
		double sum=0;
		for (uint32_t j=0; j<m_matrix->size(); j++) {
			sum += (*m_matrix)[i][j];
		};
		NS_ASSERT_MSG(sum*sum == 0, "Invalid generator matrix");
	};
#endif
	// Schedule for packet transmission and state transition
	ScheduleNextTx();
	ScheduleNextTransition();
}

void MmppApplication::StopApplication() // Called at time specified by Stop
{
	NS_LOG_FUNCTION (this);

	CancelEvents ();
	if(m_socket != 0) {
		m_socket->Close ();
	} else {
		NS_LOG_WARN("MmppApplication found null socket to close in StopApplication");
	}
}

void MmppApplication::CancelEvents ()
{
	NS_LOG_FUNCTION (this);
	Simulator::Cancel(m_sendEvent);
	Simulator::Cancel(m_stateEvent);
}

// Private helpers
void MmppApplication::ScheduleNextTx()
{
	NS_LOG_FUNCTION (this);

	if (m_maxBytes == 0 || m_totBytes < m_maxBytes) {
		double PoissonRate = static_cast<double>((*m_rate)[m_state].GetBitRate());
		if (PoissonRate > 0) { // Rate of 0 means no packets shall be sent
			Time nextTx(Seconds(ExponentialVariable(8*(*m_pktSize)[m_state]/PoissonRate).GetValue()));
			NS_LOG_LOGIC ("nextTime = " << nextTx);
			m_sendEvent = Simulator::Schedule(nextTx, &MmppApplication::SendPacket, this);
		};
	} else { // All done, cancel any pending events
		NS_LOG_LOGIC ("m_totBytes >= m_maxBytes. Application closed.");
		StopApplication();
	}
}

void MmppApplication::ScheduleNextTransition()
{
	NS_LOG_FUNCTION (this);

	Time nextTransition(Seconds(ExponentialVariable(-1/static_cast<double>((*m_matrix)[m_state][m_state])).GetValue()));
	NS_LOG_LOGIC ("nextTransition = " << nextTransition);
	m_stateEvent = Simulator::Schedule(nextTransition, &MmppApplication::StateChange, this);
}

void MmppApplication::ResumeSend(Ptr<Socket> sock, uint32_t txAvail)
{
	NS_LOG_FUNCTION(this << sock << txAvail);
	if (m_pendingPkts.size() == 0 || m_pendingPkts.front()->GetSize() > txAvail) {
		return;
	};

	// ScheduleNow to prevent a huge calling stack build up
	Simulator::ScheduleNow(&MmppApplication::SendPendingPacket, this);
}

void MmppApplication::SendPendingPacket()
{
	while (m_pendingPkts.size()) {
		Ptr<Packet> packet = m_pendingPkts.front();
		if (m_socket->Send (packet) == 0) {
			return;
		};
		m_txTrace (packet);
		m_totBytes += packet->GetSize();
		m_pendingPkts.pop_front();
		NS_LOG_LOGIC ("Send resumed. Pending pkts =" << m_pendingPkts.size());
	};
}
	
void MmppApplication::SendPacket()
{
	NS_LOG_FUNCTION (this);
	NS_ASSERT (m_sendEvent.IsExpired ());
	NS_LOG_LOGIC ("sending packet at " << Simulator::Now());
	Ptr<Packet> packet = Create<Packet> ((*m_pktSize)[m_state]);
	if (m_socket->Send (packet) >= 0) {
		m_txTrace (packet);
		m_totBytes += (*m_pktSize)[m_state];
	} else {
		m_pendingPkts.push_back(packet);
		NS_LOG_LOGIC ("Send blocked. Wait for notification. Pending pkts =" << m_pendingPkts.size());
	};
	ScheduleNextTx();
}

void MmppApplication::StateChange()
{
	NS_LOG_FUNCTION (this);
	NS_ASSERT (m_stateEvent.IsExpired ());
	if ((*m_matrix)[m_state][m_state] == 0) {
		return;	// We're in a got-stuck state
	};
	double random = UniformVariable().GetValue();	// A random value of [0,1)
	uint32_t newState = 0;
	for (; newState < m_matrix->size() ; newState++) {
		if (m_state != newState) {
			random += (*m_matrix)[m_state][newState]/(*m_matrix)[m_state][m_state];
		};
		if (random <= 0) break;
	};
	NS_LOG_LOGIC ("changing state at " << Simulator::Now() << " from " << m_state << " to " << newState);
	m_state = newState;
	Simulator::Cancel(m_sendEvent);
	ScheduleNextTx();
	ScheduleNextTransition();
};

} // Namespace ns3
