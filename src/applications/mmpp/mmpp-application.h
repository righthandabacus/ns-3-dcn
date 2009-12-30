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

#ifndef __mmpp_application_h__
#define __mmpp_application_h__

#include <vector>
#include "ns3/application.h"
#include "ns3/event-id.h"
#include "ns3/ptr.h"
#include "ns3/data-rate.h"
#include "ns3/traced-callback.h"
#include "ns3/type-id.h"

namespace ns3 {

using std::vector;

class Address;
class Socket;

// Reference-counted vector
template <typename T>
class RcVector : public std::vector<T>, public Object
{
};

typedef RcVector<RcVector<double> > GenMatrix;
typedef RcVector<DataRate> RateVector;
typedef RcVector<uint32_t> SizeVector;

/**
 * \ingroup applications 
 * \defgroup MMPP MmppApplication
 *
 * This traffic generator produces traffic according to a Markov-
 * Modulated Poisson Process after Application::StartApplication
 * is called. It takes a n-vector of data rates and a n-by-n matrix of
 * double precision values of transition rates. The state space is
 * 1 to n and at state i, the data rate is the i-th rate in the vector.
 * During each state, a CBR traffic is generated with fixed packet size.
 */

 /**
 * \ingroup MMPP
 *
 * \brief Generate traffic to a single destination according to an
 *        MMPP.
 *
 * This traffic generator produces traffic according to a Markov-
 * Modulated Poisson Process after Application::StartApplication
 * is called. It takes a n-vector of data rates and a n-by-n matrix of
 * double precision values of transition rates. The state space is
 * 1 to n and at state i, the data rate is the i-th rate in the vector.
 * During each state, a CBR traffic is generated with fixed packet size.
 *
 * Note:  When an application is started, the first packet transmission
 * occurs _after_ a delay equal to (packet size/bit rate).  Note also,
 * when an application transitions into an off state in between packet
 * transmissions, the remaining time until when the next transmission
 * would have occurred is cached and is used when the application starts
 * up again.  Example:  packet size = 1000 bits, bit rate = 500 bits/sec.
 * If the application is started at time 3 seconds, the first packet
 * transmission will be scheduled for time 5 seconds (3 + 1000/500)
 * and subsequent transmissions at 2 second intervals.  If the above
 * application were instead stopped at time 4 seconds, and restarted at
 * time 5.5 seconds, then the first packet would be sent at time 6.5 seconds,
 * because when it was stopped at 4 seconds, there was only 1 second remaining
 * until the originally scheduled transmission, and this time remaining
 * information is cached and used to schedule the next transmission
 * upon restarting.
 */
class MmppApplication : public Application 
{
public:
	static TypeId GetTypeId (void);
	MmppApplication ();
	virtual ~MmppApplication();

	void SetMaxBytes(uint32_t maxBytes);
	//void SetParameters(GenMatrix* m, vector<DataRate>* r, vector<uint32_t>* s) { m_matrix=m; m_rate=r; m_pktSize=s; };
protected:
	virtual void DoDispose (void);
	void ResumeSend(Ptr<Socket> sock, uint32_t txAvail);
	void SendPendingPacket(uint32_t txAvail);
private:
	// inherited from Application base class.
	virtual void StartApplication (void);    // Called at time specified by Start
	virtual void StopApplication (void);     // Called at time specified by Stop

	// parameters.
	Ptr<GenMatrix>     m_matrix;    // Generator matrix for the Markov process
	Ptr<RateVector>    m_rate;      // Vector of sending rates in bps
	Ptr<SizeVector>    m_pktSize;   // Vector of packet sizes in bytes
	Address            m_peer;      // Peer address
	uint32_t           m_maxBytes;  // Limit total number of bytes sent
	TypeId             m_tid;       // Protocol to use

	// variables for the traffic generator
	uint32_t        m_state;        // Current state of the Markov chain
	Ptr<Socket>     m_socket;       // Associated socket
	uint32_t        m_totBytes;     // Total bytes sent so far
	EventId         m_stateEvent;   // Event Id for next Markov state transition event
	EventId         m_sendEvent;    // Event Id of pending "send packet" event
	uint32_t	m_pendingBytes;	// Number of bytes generated but not sent

	// for trace
	TracedCallback<Ptr<const Packet> > m_txTrace;

	// helpers
	void CancelEvents ();          // Cancel pending functions for application start/stop
	void ScheduleNextTx();         // Schedule next packet
	void ScheduleNextTransition(); // Schedule next state transition

	// Event handlers
	void SendPacket();  // Send a packet and schedule next packet transmission
	void StateChange(); // Change the state and schedule for next change
};

}; // namespace ns3

#endif

