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

#include "ns3/abort.h"
#include "ns3/node.h"
#include "ns3/inet-socket-address.h"
#include "ns3/log.h"
#include "ns3/ipv4.h"
#include "ns3/ipv4-interface-address.h"
#include "ns3/ipv4-route.h"
#include "ns3/ipv4-routing-protocol.h"
#include "ns3/simulation-singleton.h"
#include "ns3/simulator.h"
#include "ns3/packet.h"
#include "ns3/uinteger.h"
#include "ns3/trace-source-accessor.h"
#include "tcp-typedefs.h"
#include "tcp-socket-impl.h"
#include "tcp-l4-protocol.h"
#include "ipv4-end-point.h"
#include "tcp-header.h"
#include "rtt-estimator.h"

#include <algorithm>

NS_LOG_COMPONENT_DEFINE ("TcpSocketImpl");

using namespace std;

namespace ns3 {

NS_OBJECT_ENSURE_REGISTERED (TcpSocketImpl);

TypeId
TcpSocketImpl::GetTypeId ()
{
	static TypeId tid = TypeId("ns3::TcpSocketImpl")
		.SetParent<TcpSocket> ()
		.AddAttribute ("Blocking",
			"Set the socket's send function blocking",
			BooleanValue (false),
			MakeBooleanAccessor (&TcpSocketImpl::m_blocking),
			MakeBooleanChecker ())
		;
	return tid;
}

TcpSocketImpl::TcpSocketImpl ()
  : m_dupAckCount (0),
    m_delAckCount (0),
    m_persistTime (Seconds(6)), //XXX hook this into attributes?
    m_endPoint (0),
    m_node (0),
    m_tcp (0),
    m_localAddress (Ipv4Address::GetZero ()),
    m_localPort (0),
    m_rtt (0),
    m_nextTxSequence (0),
    m_highTxMark (0),
    m_rxBuffer (0),
    m_txBuffer (0),
    m_state (CLOSED),
    m_errno (ERROR_NOTERROR),
    m_closeNotified (false),
    m_closeOnEmpty (false),
    m_pendingClose (false),
    m_shutdownSend (false),
    m_shutdownRecv (false),
    m_connected (false),
    m_segmentSize (0),          // For attribute initialization consistency (quiet valgrind)
    m_rxWindowSize (0)
{
	NS_LOG_FUNCTION (this);
}

TcpSocketImpl::TcpSocketImpl(const TcpSocketImpl& sock)
  : TcpSocket(sock), //copy object::m_tid, copy socket::callbacks
    m_dupAckCount (sock.m_dupAckCount),
    m_delAckCount (0),
    m_delAckMaxCount (sock.m_delAckMaxCount),
    m_cnCount (sock.m_cnCount),
    m_delAckTimeout (sock.m_delAckTimeout),
    m_persistTime (sock.m_persistTime),
    m_cnTimeout (sock.m_cnTimeout),
    m_endPoint (0),
    m_node (sock.m_node),
    m_tcp (sock.m_tcp),
    m_remoteAddress (sock.m_remoteAddress),
    m_remotePort (sock.m_remotePort),
    m_localAddress (sock.m_localAddress),
    m_localPort (sock.m_localPort),
    m_rtt (0),
    m_nextTxSequence (sock.m_nextTxSequence),
    m_highTxMark (sock.m_highTxMark),
    m_rxBuffer (sock.m_rxBuffer),
    m_txBuffer (sock.m_txBuffer),
    m_state (sock.m_state),
    m_errno (sock.m_errno),
    m_closeNotified (sock.m_closeNotified),
    m_closeOnEmpty (sock.m_closeOnEmpty),
    m_pendingClose (sock.m_pendingClose),
    m_shutdownSend (sock.m_shutdownSend),
    m_shutdownRecv (sock.m_shutdownRecv),
    m_connected (sock.m_connected),
    m_segmentSize (sock.m_segmentSize),
    m_rxWindowSize (sock.m_rxWindowSize)
{
	NS_LOG_FUNCTION (this);
	NS_LOG_LOGIC("Invoked the copy constructor");
	// Copy the rtt estimator if it is set
	if (sock.m_rtt) {
		m_rtt = sock.m_rtt->Copy();
	}
	// Reset all callbacks to null
	Callback<void, Ptr< Socket > > vPS =
		MakeNullCallback<void, Ptr<Socket> > ();
	Callback<void, Ptr<Socket>, const Address &> vPSA =
		MakeNullCallback<void, Ptr<Socket>, const Address &> ();
	Callback<void, Ptr<Socket>, uint32_t> vPSUI =
		MakeNullCallback<void, Ptr<Socket>, uint32_t> ();
	SetConnectCallback (vPS, vPS);
	SetDataSentCallback (vPSUI);
	SetSendCallback (vPSUI);
	SetRecvCallback (vPS);
}

TcpSocketImpl::~TcpSocketImpl ()
{
	NS_LOG_FUNCTION(this);
	m_node = 0;
	if (m_endPoint != 0) {
		NS_ASSERT (m_tcp != 0);
		/*
		 * Note that this piece of code is seriously convoluted: When we do a 
		 * Bind we allocate an Ipv4Endpoint.  Immediately thereafter we always do
		 * a FinishBind which sets the DestroyCallback of that endpoint to be
		 * TcpSocketImpl::Destroy, below.  When m_tcp->DeAllocate is called, it
		 * will in turn call into Ipv4EndpointDemux::DeAllocate with the endpoint
		 * (m_endPoint).  The demux will look up the endpoint and destroy it (the
		 * corollary is that we don't own the object pointed to by m_endpoint, we
		 * just borrowed it).  The destructor for the endpoint will call the
		 * DestroyCallback which will then invoke TcpSocketImpl::Destroy below.
		 * Destroy will zero m_node, m_tcp and m_endpoint.  The zero of m_node and
		 * m_tcp need to be here also in case the endpoint is deallocated before
		 * shutdown.
		 */
		NS_ASSERT (m_endPoint != 0);
		m_tcp->DeAllocate (m_endPoint);
		NS_ASSERT (m_endPoint == 0);
	}
	m_tcp = 0;
	CancelAllTimers();
}

void
TcpSocketImpl::SetNode (Ptr<Node> node)
{
	m_node = node;
}

void 
TcpSocketImpl::SetTcp (Ptr<TcpL4Protocol> tcp)
{
	m_tcp = tcp;
}

void 
TcpSocketImpl::SetRtt (Ptr<RttEstimator> rtt)
{
	m_rtt = rtt;
}

enum Socket::SocketErrno
TcpSocketImpl::GetErrno (void) const
{
	NS_LOG_FUNCTION_NOARGS ();
	return m_errno;
}

Ptr<Node>
TcpSocketImpl::GetNode (void) const
{
	NS_LOG_FUNCTION_NOARGS ();
	return m_node;
}

int
TcpSocketImpl::Bind (void)
{
	NS_LOG_FUNCTION_NOARGS ();
	m_endPoint = m_tcp->Allocate ();
	return CommonBind ();
}

int 
TcpSocketImpl::Bind (const Address &address)
{
	NS_LOG_FUNCTION (this<<address);
	if (!InetSocketAddress::IsMatchingType (address)) {
		m_errno = ERROR_INVAL;
		return -1;
	};
	InetSocketAddress transport = InetSocketAddress::ConvertFrom (address);
	Ipv4Address ipv4 = transport.GetIpv4 ();
	uint16_t port = transport.GetPort ();
	if (ipv4 == Ipv4Address::GetAny () && port == 0) {
		m_endPoint = m_tcp->Allocate ();
	} else if (ipv4 == Ipv4Address::GetAny () && port != 0) {
		m_endPoint = m_tcp->Allocate (port);
	} else if (ipv4 != Ipv4Address::GetAny () && port == 0) {
		m_endPoint = m_tcp->Allocate (ipv4);
	} else if (ipv4 != Ipv4Address::GetAny () && port != 0) {
		m_endPoint = m_tcp->Allocate (ipv4, port);
	};
	NS_LOG_LOGIC ("TcpSocketImpl "<<this<<" got an endpoint: "<<m_endPoint);

	return CommonBind ();
}

int
TcpSocketImpl::Close (void)
{
	NS_LOG_FUNCTION (this);
	// First we check to see if there is any unread rx data
	// Bug number 426 claims we should send reset in this case.
	if (m_rxBuffer.Size() != 0) {
		SendRST();
		return 0;
	}
	if (m_txBuffer.SizeFromSeq(m_nextTxSequence) > 0) {
		// App close with pending data must wait until all data transmitted
		m_closeOnEmpty = true;
		NS_LOG_LOGIC("Socket " << this << " deferring close, state " << m_state);
		return 0;
	};
	Actions_t action  = ProcessEvent (APP_CLOSE);
	ProcessAction (action);
	return 0;
}

int 
TcpSocketImpl::ShutdownSend (void)
{
	NS_LOG_FUNCTION (this);
	m_shutdownSend = true;
	return 0;
}

int 
TcpSocketImpl::ShutdownRecv (void)
{
	NS_LOG_FUNCTION (this);
	m_shutdownRecv = true;
	return 0;
}

int
TcpSocketImpl::Connect (const Address & address)
{
	NS_LOG_FUNCTION (this << address);

	// If haven't do so, Bind() this socket first
	if (m_endPoint == 0) {
		if (Bind () == -1) {
			NS_ASSERT (m_endPoint == 0);
			return -1; // Bind() failed
		}
		NS_ASSERT (m_endPoint != 0);
	}

	InetSocketAddress transport = InetSocketAddress::ConvertFrom (address);
	m_remoteAddress = transport.GetIpv4 ();
	m_remotePort = transport.GetPort ();

	// Get the appropriate local address and port number from the routing protocol and set up endpoint
	if (SetupEndpoint() != 0) {
		// Route to destination does not exist
		return -1;
	};

	// Real connection is done in ProcessEvent() and ProcessAction()
	Actions_t action = ProcessEvent (APP_CONNECT);
	bool success = ProcessAction (action);
	return success ? 0 : -1;
}

int
TcpSocketImpl::Listen (void)
{
	NS_LOG_FUNCTION (this);
	// Linux quits EINVAL if we're not closed, so match what they do
	if (m_state != CLOSED) {
		m_errno = ERROR_INVAL;
		return -1;
	}
	Actions_t action = ProcessEvent (APP_LISTEN);
	ProcessAction (action);
	return 0;
}

// p is the data from upper layers, no header
int 
TcpSocketImpl::Send (Ptr<Packet> p, uint32_t flags) 
{
	NS_LOG_FUNCTION (this << p);
	if (m_state == ESTABLISHED || m_state == SYN_SENT || m_state == CLOSE_WAIT) {
		if (m_txBuffer.Size()==0) {
			// Initialize buffer on first use
			m_txBuffer.SetHeadSeq(m_nextTxSequence);
		}
		// Store the packet into Tx buffer
		if (! m_txBuffer.Add (p)) {
			// TxBuffer overflow, send failed
			m_errno = ERROR_MSGSIZE;
			return -1;
		};
		// Try to send to lower layers
		NS_LOG_DEBUG("txBufSize="<< m_txBuffer.Size() <<" state "<< m_state);
		Actions_t action = ProcessEvent (APP_SEND);
		NS_LOG_DEBUG(" action " << action);
		if (ProcessAction (action)) {
			return p->GetSize(); // Success, return packet size
		};
		return -1; // ProcessAction() failure, shall never happens
	} else { // Connection not established yet
		m_errno = ERROR_NOTCONN;
		return -1; // Send failure
	}
}

int 
TcpSocketImpl::SendTo (Ptr<Packet> p, uint32_t flags, const Address &address)
{
	NS_LOG_FUNCTION (this << address << p);
	return Send(p, flags); // SendTo() and Send() are the same
}

uint32_t
TcpSocketImpl::GetTxAvailable (void) const
{
	NS_LOG_FUNCTION (this);
	return m_txBuffer.Available();
}

uint32_t
TcpSocketImpl::GetRxAvailable (void) const
{
	NS_LOG_FUNCTION (this);
	return m_rxBuffer.Available();
}

Ptr<Packet>
TcpSocketImpl::Recv (uint32_t maxSize, uint32_t flags)
{
	NS_LOG_FUNCTION (this);
	if(m_rxBuffer.Size()==0 && m_state == CLOSE_WAIT) {
		return Create<Packet>(); // Send EOF on connection close
	}
	Ptr<Packet> outPacket = m_rxBuffer.Extract(maxSize);
	if (outPacket != 0 && outPacket->GetSize() != 0) {
		SocketAddressTag tag;
		tag.SetAddress (InetSocketAddress (m_remoteAddress, m_remotePort));
		outPacket->AddPacketTag (tag);
	}
	return outPacket;
}

Ptr<Packet>
TcpSocketImpl::RecvFrom (uint32_t maxSize, uint32_t flags, Address &fromAddress)
{
	NS_LOG_FUNCTION (this << maxSize << flags);
	Ptr<Packet> packet = Recv (maxSize, flags);
	// Null packet means no data to read, and an empty packet indicates EOF
	if (packet != 0 && packet->GetSize() != 0) {
		// Peek the socket address tag from the packet returned and set the
		// remote address to fromAddress
		SocketAddressTag tag;
		bool found = packet->PeekPacketTag (tag);
		found = found;
		NS_ASSERT (found);
		fromAddress = tag.GetAddress ();
	}
	return packet;
}

int
TcpSocketImpl::GetSockName (Address &address) const
{
	NS_LOG_FUNCTION (this);
	address = InetSocketAddress(m_localAddress, m_localPort);
	return 0;
}

void
TcpSocketImpl::BindToNetDevice (Ptr<NetDevice> netdevice)
{
	NS_LOG_FUNCTION (netdevice);
	Socket::BindToNetDevice (netdevice); // Includes sanity check
	if (m_endPoint == 0) {
		if (Bind () == -1) {
			NS_ASSERT (m_endPoint == 0);
			return;
		}
		NS_ASSERT (m_endPoint != 0);
	}
	m_endPoint->BindToNetDevice (netdevice);
	return;
}

int
TcpSocketImpl::CommonBind (void)
{
	NS_LOG_FUNCTION (this);
	if (m_endPoint == 0) {
		return -1;
	}
	m_endPoint->SetRxCallback (MakeCallback (&TcpSocketImpl::ForwardUp, Ptr<TcpSocketImpl>(this)));
	m_endPoint->SetDestroyCallback (MakeCallback (&TcpSocketImpl::Destroy, Ptr<TcpSocketImpl>(this)));
	m_localAddress = m_endPoint->GetLocalAddress ();
	m_localPort = m_endPoint->GetLocalPort ();
	return 0;
}

// Function called by the L3 protocol when it received a packet to pass on to the TCP
// This function is registered as the "RxCallback" function in CommonBind() and CompleteFork()
void
TcpSocketImpl::ForwardUp (Ptr<Packet> packet, Ipv4Address ipv4, uint16_t port)
{
	NS_LOG_FUNCTION (this << packet << ipv4 << port);
	NS_LOG_DEBUG("Socket "<< this <<" got forward up"<<
				" saddr "<< m_endPoint->GetPeerAddress() <<
				" sport "<< m_endPoint->GetPeerPort() <<
				" daddr "<< m_endPoint->GetLocalAddress() <<
				" dport "<< m_endPoint->GetLocalPort());

	if (m_shutdownRecv) return;  // No more Recv allowed

	// Peel off TCP header, and check flags
	TcpHeader tcpHeader;
	packet->RemoveHeader (tcpHeader);
	if (tcpHeader.GetFlags () & TcpHeader::ACK) {
		// TODO: This RTT function shall be changed to handle timestamp options
		// One solution is to pass the whole header instead of just the number
		m_rtt->AckSeq (tcpHeader.GetAckNumber () );
	}

	// Update Rx window size, i.e. the flow control window
	if (m_rxWindowSize == 0 && tcpHeader.GetWindowSize () != 0) {
		// persist probes end
		NS_LOG_LOGIC (this<<" Leaving zerowindow persist state");
		m_persistEvent.Cancel ();
	}
	m_rxWindowSize = tcpHeader.GetWindowSize ();

	// Lookup the event base on the flags received, and execute corresponding actions
	Events_t event = SimulationSingleton<TcpStateMachine>::Get()->FlagsEvent(tcpHeader.GetFlags());
	Actions_t action = ProcessEvent (event);
	Address address = InetSocketAddress (ipv4, port);
	NS_LOG_DEBUG("Socket "<< this <<" processing pkt action, "<< action <<" current state "<< m_state);
	ProcessPacketAction (action, packet, tcpHeader, address);
}

void 
TcpSocketImpl::Destroy (void)
{
	NS_LOG_FUNCTION (this);
	m_node = 0;
	m_endPoint = 0;
	m_tcp = 0;
	NS_LOG_LOGIC (this<<" Cancelled ReTxTimeout event which was set to expire at "
		<< (Simulator::Now () + Simulator::GetDelayLeft (m_retxEvent)).GetSeconds());
	CancelAllTimers();
}

void TcpSocketImpl::SendEmptyPacket (uint8_t flags)
{
	NS_LOG_FUNCTION (this << (uint32_t)flags);
	Ptr<Packet> p = Create<Packet> ();
	TcpHeader header;

	if (flags & TcpHeader::FIN) {
		flags |= TcpHeader::ACK;
	}

	header.SetFlags (flags);
	header.SetSequenceNumber (m_nextTxSequence);
	header.SetAckNumber (m_rxBuffer.NextRxSeq());
	header.SetSourcePort (m_endPoint->GetLocalPort ());
	header.SetDestinationPort (m_remotePort);
	header.SetWindowSize (AdvertisedWindowSize());
	m_tcp->SendPacket (p, header, m_endPoint->GetLocalAddress(), m_remoteAddress, m_boundnetdevice);
	Time rto = m_rtt->RetransmitTimeout ();
	bool hasSyn = flags & TcpHeader::SYN;
	bool hasFin = flags & TcpHeader::FIN;
	bool isAck = flags == TcpHeader::ACK;
	if (hasSyn) {
		// Exponential backoff of connection time out
		rto = m_cnTimeout;
		m_cnTimeout = m_cnTimeout + m_cnTimeout;
		m_cnCount--;
	}
	if (flags & TcpHeader::ACK) {
		// If sending an ACK, cancel the delay ACK as well
		m_delAckEvent.Cancel();
		m_delAckCount = 0;
	}
	if (m_retxEvent.IsExpired () && (hasSyn || hasFin) && !isAck ) {
		// Setup ReTx timer if not have one at the moment
		NS_LOG_LOGIC ("Schedule retransmission timeout at time " 
				<< Simulator::Now ().GetSeconds () << " to expire at time " 
				<< (Simulator::Now () + rto).GetSeconds ());
		m_retxEvent = Simulator::Schedule (rto, &TcpSocketImpl::ReTxTimeout, this);
	}
}

// This function closes the endpoint completely
void TcpSocketImpl::SendRST()
{
	SendEmptyPacket(TcpHeader::RST);
	NotifyErrorClose();
	CancelAllTimers();
	m_endPoint->SetDestroyCallback(MakeNullCallback<void>());
	m_tcp->DeAllocate (m_endPoint);
	m_endPoint = 0;
}

int TcpSocketImpl::SetupEndpoint()
{
	// Look up the source address and then set up endpoint
	Ptr<Ipv4> ipv4 = m_node->GetObject<Ipv4> ();
	if (ipv4->GetRoutingProtocol () != 0) {
		Ipv4Header header;
		header.SetDestination (m_remoteAddress);
		Socket::SocketErrno errno_;
		Ptr<Ipv4Route> route;
		Ptr<NetDevice> oif = m_boundnetdevice;
		route = ipv4->GetRoutingProtocol ()->RouteOutput (Ptr<Packet> (), header, oif, errno_);
		if (route == 0) {
			NS_LOG_LOGIC ("TcpSocketImpl::SetupEndpoint(): Route to " << m_remoteAddress << " does not exist");
			NS_LOG_ERROR (errno_);
			m_errno = errno_;
			return -1;
		}
		NS_LOG_LOGIC ("Route exists");
		m_endPoint->SetLocalAddress (route->GetSource ());
	} else {
		NS_FATAL_ERROR ("No Ipv4RoutingProtocol in the node");
	}
	return 0;
};

// After TcpSocketImpl cloned, allocate a new end point to handle the incoming connection
void TcpSocketImpl::CompleteFork(Ptr<Packet> p, const TcpHeader& h, const Address& fromAddress)
{
	// Get port and address from peer (connecting host)
	m_remotePort = InetSocketAddress::ConvertFrom(fromAddress).GetPort ();
	m_remoteAddress = InetSocketAddress::ConvertFrom(fromAddress).GetIpv4 ();
	m_endPoint = m_tcp->Allocate(m_localAddress, m_localPort, m_remoteAddress, m_remotePort);

	// Change the cloned socket from LISTEN state to SYN_RCVD
	m_state = SYN_RCVD;
	// Setup callback and call ProcessPacketAction to continue the handshake
	m_endPoint->SetRxCallback (MakeCallback (&TcpSocketImpl::ForwardUp, Ptr<TcpSocketImpl>(this)));
	m_endPoint->SetDestroyCallback (MakeCallback (&TcpSocketImpl::Destroy, Ptr<TcpSocketImpl>(this)));
	ProcessPacketAction(SYN_ACK_TX, p, h, fromAddress);
}

void TcpSocketImpl::ConnectionSucceeded()
{	// We would preferred to have scheduled an event directly to
	// NotifyConnectionSucceeded, but (sigh) these are protected
	// and we can get the address of it :(
	NotifyConnectionSucceeded();
}

void
TcpSocketImpl::DeviceUnblocked(Ptr<NetDevice> nd, uint32_t avail)
{
	NS_LOG_FUNCTION (this << nd << avail);
	Ptr<QbbNetDevice> qbb = nd->GetObject<QbbNetDevice>();
	if (qbb->GetTxAvailable() >= m_segmentSize) {
		Simulator::ScheduleNow(&TcpSocketImpl::CancelNetDeviceCallback, this, qbb);
		SendPendingData(m_connected);
	};
};

void
TcpSocketImpl::CancelNetDeviceCallback(Ptr<QbbNetDevice> qbb)
{
	NS_LOG_FUNCTION (this << qbb);
	qbb->DisconnectWithoutContext(MakeCallback(&TcpSocketImpl::DeviceUnblocked, this));
};

// Send as much pending data as possible according to the Tx window. Note that
// this function did not implement the PSH flag
bool
TcpSocketImpl::SendPendingData (bool withAck)
{
	NS_LOG_FUNCTION (this << withAck);
	NS_LOG_LOGIC ("ENTERING SendPendingData");
	if (m_txBuffer.Size()==0) return false; // Nothing to send
	uint32_t nPacketsSent = 0;
	while (m_txBuffer.SizeFromSeq (m_nextTxSequence)) {
		uint32_t w = AvailableWindow ();// Get available window size
		NS_LOG_LOGIC ("TcpSocketImpl " << this << " SendPendingData"
						<< " w " << w
						<< " rxwin " << m_rxWindowSize
						<< " segsize " << m_segmentSize
						<< " nextTxSeq " << m_nextTxSequence
						<< " highestRxAck " << m_txBuffer.HeadSeq()
						<< " pd->Size " << m_txBuffer.Size ()
						<< " pd->SFS " << m_txBuffer.SizeFromSeq (m_nextTxSequence));
		// Quit if send disallowed
		if (m_shutdownSend) {
			m_errno = ERROR_SHUTDOWN;
			return false;
		}
		// Stop sending if we need to wait for a larger Tx window
		if (w < m_segmentSize && m_txBuffer.SizeFromSeq (m_nextTxSequence) > w) {
			break; // No more
		}
		// Check if we need to wait for netdevice buffer
		if (m_blocking) {
			// Assumed we called SetupEndPoint, now we get the route to destination
			Ptr<Ipv4RoutingProtocol> rp = m_node->GetObject<Ipv4>()->GetRoutingProtocol();
			Ipv4Header header;
			header.SetDestination (m_remoteAddress);
			Socket::SocketErrno errno_;
			Ptr<Ipv4Route> route = m_node->GetObject<Ipv4>()->GetRoutingProtocol ()->RouteOutput (Ptr<Packet> (), header, 0, errno_);
			// From the route, get the netdevice
			Ptr<NetDevice> nd = route->GetOutputDevice();
			Ptr<QbbNetDevice> qbb = nd->GetObject<QbbNetDevice>();
			if (qbb != 0 && qbb->GetTxAvailable() < m_segmentSize) {
				NS_LOG_LOGIC("NetDevice buffer full. Not sending.");
				qbb->ConnectWithoutContext(MakeCallback(&TcpSocketImpl::DeviceUnblocked, this));
				break;
			};
		};
		uint32_t s = std::min (w, m_segmentSize);  // Send no more than window
		Ptr<Packet> p = m_txBuffer.CopyFromSeq (s, m_nextTxSequence);
		NS_LOG_LOGIC("TcpSocketImpl " << this << " SendPendingData"
						<< " txseq " << m_nextTxSequence
						<< " s " << s 
						<< " datasize " << p->GetSize() );
		uint8_t flags = 0;
		uint32_t sz = p->GetSize (); // Size of packet
		uint32_t remainingData = m_txBuffer.SizeFromSeq(m_nextTxSequence + SequenceNumber (sz));
		if (m_closeOnEmpty && (remainingData == 0)) {
			flags = TcpHeader::FIN;
			m_state = FIN_WAIT_1;
		}
		if (withAck) {
			flags |= TcpHeader::ACK;
		}
		TcpHeader header;
		header.SetFlags (flags);
		header.SetSequenceNumber (m_nextTxSequence);
		header.SetAckNumber (m_rxBuffer.NextRxSeq());
		header.SetSourcePort (m_endPoint->GetLocalPort());
		header.SetDestinationPort (m_remotePort);
		header.SetWindowSize (AdvertisedWindowSize());
		if (m_retxEvent.IsExpired () ) {
			// Schedule retransit
			Time rto = m_rtt->RetransmitTimeout (); 
			NS_LOG_LOGIC (this<<" SendPendingData Schedule ReTxTimeout at time " << 
						Simulator::Now ().GetSeconds () << " to expire at time " <<
						(Simulator::Now () + rto).GetSeconds () );
			m_retxEvent = Simulator::Schedule (rto,&TcpSocketImpl::ReTxTimeout,this);
		}
		NS_LOG_LOGIC ("About to send a packet with flags: " << flags);
		m_tcp->SendPacket (p, header, m_endPoint->GetLocalAddress (), m_remoteAddress, m_boundnetdevice);
		m_rtt->SentSeq(m_nextTxSequence, sz);       // notify the RTT
		// Notify the application of the data being sent
		Simulator::ScheduleNow(&TcpSocketImpl::NotifyDataSent, this, sz);
		nPacketsSent++;                             // Count sent this loop
		m_nextTxSequence += sz;                     // Advance next tx sequence
		// Update highTxMark
		m_highTxMark = std::max (m_nextTxSequence, m_highTxMark);
	}
	NS_LOG_LOGIC ("SendPendingData Sent "<<nPacketsSent<<" packets");
	NS_LOG_LOGIC("RETURN SendPendingData");
	return (nPacketsSent>0);
}

Actions_t TcpSocketImpl::ProcessEvent (Events_t e)
{
	NS_LOG_FUNCTION (this << e);
	States_t saveState = m_state;
	NS_LOG_LOGIC ("TcpSocketImpl " << this << " processing event " << e);

	// From (Current State, Event), lookup (New State, Action)
	SA stateAction = SimulationSingleton<TcpStateMachine>::Get ()->Lookup (m_state,e);
	NS_LOG_LOGIC ("TcpSocketImpl::ProcessEvent stateAction " << stateAction.action);
	if (stateAction.action == RST_TX) {
		// We have to send a RST, and this connection will be killed
		NS_LOG_LOGIC("TcpSocketImpl "<< this <<" sending RST from state "<< saveState <<" event "<< e);
		SendRST();
		return NO_ACT;
	}

	// Update the current state
	bool needCloseNotify = (stateAction.state == CLOSED && m_state != CLOSED && e != TIMEOUT);
	m_state = stateAction.state;
	NS_LOG_LOGIC("TcpSocketImpl "<< this <<" moved from state "<< saveState <<" to state "<<m_state);

	// Special processing for some RX events
	if (saveState == SYN_SENT && m_state == ESTABLISHED) {
		// e = SYN_ACK_RX
		// My (connection initiator) portion of handshaking completed
		Simulator::ScheduleNow(&TcpSocketImpl::ConnectionSucceeded, this);
		m_connected = true;
		m_endPoint->SetPeer (m_remoteAddress, m_remotePort);
		NS_LOG_LOGIC ("TcpSocketImpl " << this << " Connected!");
	} else if (saveState < CLOSING && (m_state == CLOSING || m_state == TIMED_WAIT) ) {
		// Peer closing
		NS_LOG_LOGIC ("TcpSocketImpl peer closing, send EOF to application");
		NotifyDataRecv ();
	}
	if (needCloseNotify && !m_closeNotified) {
		// Tell upper layer to close if necessary
		NS_LOG_LOGIC ("TcpSocketImpl " << this << " transition to CLOSED from state " 
					<< m_state << " origState " << saveState << " event " << e
					<< " closeNot " << m_closeNotified
					<< " action " << stateAction.action);
		NotifyNormalClose();
		m_closeNotified = true;
	}
	if (m_state == CLOSED && saveState != CLOSED && m_endPoint != 0) {
		// Close finished, do the clean up
		NS_ASSERT (m_tcp != 0);
		/*
		 * We want to deallocate the endpoint now.  We can't just naively call
		 * Deallocate (see the comment in TcpSocketImpl::~TcpSocketImpl), we 
		 * have to turn off the DestroyCallback to keep it from calling back 
		 * into TcpSocketImpl::Destroy and closing pretty much everything down.
		 * Once we have the callback disconnected, we can DeAllocate the
		 * endpoint which actually deals with destroying the actual endpoint,
		 * and then zero our member varible on general principles.
		 */
		m_endPoint->SetDestroyCallback(MakeNullCallback<void>());
		m_tcp->DeAllocate (m_endPoint);
		m_endPoint = 0;
		CancelAllTimers();
	}
    
	return stateAction.action;
}

// Process those actions that do not require a packet nor the TCP header
// The rest is handled by another ProcessAction() function
bool TcpSocketImpl::ProcessAction (Actions_t a)
{
	NS_LOG_FUNCTION (this << a);
	switch (a) {
		case NO_ACT:  // No action
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action: NO_ACT");
			break;
		case ACK_TX:  // Send an ACK
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action ACK_TX");
			SendEmptyPacket (TcpHeader::ACK);
			break;
		case ACK_TX_1: // Send an ACK as the final step in 3-way handshake
			NS_ASSERT (false); // processed by another ProcessAction
			break;
		case RST_TX: // Send a RST
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action RST_TX");
			SendEmptyPacket (TcpHeader::RST);
			break;
		case SYN_TX: // Send a SYN to initiate handshake
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action SYN_TX");
			SendEmptyPacket (TcpHeader::SYN);
			break;
		case SYN_ACK_TX: // Send a SYN+ACK to respond a handshake request
			// This is the special handler that correspond to the TCP not in LISTEN state
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action SYN_ACK_TX");
			// TCP SYN Flag consumes one byte
			m_rxBuffer.IncNextRxSeq();
			SendEmptyPacket (TcpHeader::SYN | TcpHeader::ACK);
			break;
		case FIN_TX: // Send FIN to request a close
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action FIN_TX");
			SendEmptyPacket (TcpHeader::FIN);
			break;
		case FIN_ACK_TX: // Send FIN+ACK to respond to a close
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action FIN_ACK_TX");
			SendEmptyPacket (TcpHeader::FIN | TcpHeader::ACK);
			break;
		case NEW_ACK: // New ACK received
		case NEW_SEQ_RX: // New sequence number received
			NS_ASSERT (false); // This should be processed in ProcessPacketAction
			break;
		case RETX: // Retransmit
			// RETX event is included here for completeness, since a retransmit
			// event cannot be triggered by a receipt of packet but by a timer.
			// This is handled by the ReTxTimeout() call, by the scheduler.
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action RETX");
			ReTxTimeout();
			break;
		case TX_DATA: // Send data, triggered by the APP_SEND event in Send()
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action TX_DATA");
			SendPendingData (m_connected);
			break;
		case PEER_CLOSE: // Peer sent FIN
			NS_ASSERT (false); // This should be processed in ProcessPacketAction
			break;
		case APP_CLOSED: // Received ACK upon LAST_ACK
			// Application can peacefully close, nothing needs to do
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action APP_CLOSED");
			break;
		case CANCEL_TM: // Receipt of RST on established states
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action CANCEL_TM");
			NotifyErrorClose();
			CancelAllTimers();
			m_endPoint->SetDestroyCallback(MakeNullCallback<void>());
			m_tcp->DeAllocate (m_endPoint);
			m_endPoint = 0;
			break;
		case APP_NOTIFY: // Got reset upon SYN_SENT, i.e. connection attempt failed
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action APP_NOTIFY");
			NotifyErrorClose();
			CancelAllTimers();
			m_endPoint->SetDestroyCallback(MakeNullCallback<void>());
			m_tcp->DeAllocate (m_endPoint);
			m_endPoint = 0;
			break;
		case SERV_NOTIFY: // Receipt of ACK that completed a handshake
			NS_ASSERT (false); // This should be processed in ProcessPacketAction
			break;
		case LAST_ACTION: // This is not a real action, but a placeholder indeed
			break;
	}
	return true;
}

// Process those actions that require a packet or TCP header
bool TcpSocketImpl::ProcessPacketAction (Actions_t a, Ptr<Packet> p,
		const TcpHeader& tcpHeader, const Address& fromAddress)
{
	NS_LOG_FUNCTION (this << a << p  << fromAddress);

	switch (a) {
		case ACK_TX: // Respond with an ACK
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action ACK_TX");
			if(tcpHeader.GetFlags() & TcpHeader::FIN) {
				// Increment the sequence number to account for the FIN
				m_rxBuffer.IncNextRxSeq();
			}
			SendEmptyPacket (TcpHeader::ACK);
			break;
		case ACK_TX_1: // Send ACK to complete a handshake
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action ACK_TX_1");
			// TCP SYN consumes one byte
			m_rxBuffer.SetNextRxSeq(tcpHeader.GetSequenceNumber() + SequenceNumber(1));
			NS_LOG_DEBUG ("TcpSocketImpl "<< this <<" ACK_TX_1 nextRxSeq "<< m_rxBuffer.NextRxSeq());
			m_nextTxSequence = tcpHeader.GetAckNumber ();
			SendEmptyPacket (TcpHeader::ACK);
			if ( m_txBuffer.SetHeadSeq(m_nextTxSequence) ) {
				// Data freed from the send buffer; notify any blocked sender
				if (GetTxAvailable () > 0) {
					NotifySend (GetTxAvailable ());
				}
			}
			SendPendingData (m_connected); //send acks if we are connected
			break;
		case SYN_ACK_TX: // Send SYN+ACK to respond to a handshake request
			// This is for the normal case that the TCP is in LISTEN state
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action SYN_ACK_TX");
			if (m_state == LISTEN) { //this means we should fork a new TcpSocketImpl
				NS_LOG_DEBUG("In SYN_ACK_TX, m_state is LISTEN, this " << this);
				// Call socket's notify function to let server know we got a SYN
				// If server refuses connection, do nothing
				if (!NotifyConnectionRequest(fromAddress)) return true;
				// Clone the socket, simulate fork
				Ptr<TcpSocketImpl> newSock = Fork();
				NS_LOG_LOGIC ("Cloned a TcpSocketImpl " << newSock);
				Simulator::ScheduleNow (&TcpSocketImpl::CompleteFork, newSock, p, tcpHeader,fromAddress);
				return true;
			};
			// CompleteFork will change the state and call ProcessAction again.
			// Only the cloned endpoint will arrive here
			m_endPoint->SetPeer (m_remoteAddress, m_remotePort);

			// Look up the source address and then set up endpoint
			if (SetupEndpoint() != 0) {
				// Route to destination does not exist
				return -1;
			};
			// TCP SYN consumes one byte
			m_rxBuffer.SetNextRxSeq(tcpHeader.GetSequenceNumber() + SequenceNumber(1));
			SendEmptyPacket (TcpHeader::SYN | TcpHeader::ACK);
			break;
		case NEW_ACK: // Receipt of ACK
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action NEW_ACK_TX");
			// If the ACK has data piggybacked, call NEW_SEQ_RX action
			if(p->GetSize () > 0) {
				Simulator::ScheduleNow (&TcpSocketImpl::ProcessPacketAction, this,
						NEW_SEQ_RX, p, tcpHeader, fromAddress);
			}
			// Check what kind of ACK is received
			if (tcpHeader.GetAckNumber () < m_txBuffer.HeadSeq()) {
				// Case 1: Old ACK, not useful
			} else if (tcpHeader.GetAckNumber () == m_txBuffer.HeadSeq()) {
				// Case 2: Potentially a duplicated ACK
				if (tcpHeader.GetAckNumber ()  < m_nextTxSequence) {
					DupAck (tcpHeader, ++m_dupAckCount);
				}
				// otherwise, the ACK is precisely equal to the nextTxSequence
				NS_ASSERT(tcpHeader.GetAckNumber () <= m_nextTxSequence);
			} else if (tcpHeader.GetAckNumber () > m_txBuffer.HeadSeq()) {
				// Case 3: New ACK, reset m_dupAckCount and update m_txBuffer
				m_dupAckCount = 0;
				NewAck (tcpHeader.GetAckNumber ());
			};
			break;
		case NEW_SEQ_RX: // Receipt of new data
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action NEW_SEQ_RX");
			NewRx (p, tcpHeader, fromAddress); // Process new data received
			break;
		case PEER_CLOSE: {// Peer sent FIN
			NS_LOG_LOGIC("Got Peer Close");
			// If FIN is out of sequence, assert pending close and process new sequence rx
			if (tcpHeader.GetSequenceNumber() != m_rxBuffer.NextRxSeq()) {
				if (tcpHeader.GetSequenceNumber() > m_rxBuffer.NextRxSeq()) {
					m_pendingClose = true;
					NS_LOG_LOGIC ("TcpSocketImpl " << this << " setting pendingClose" 
								<< " rxseq " << tcpHeader.GetSequenceNumber () 
								<< " nextRxSeq " << m_rxBuffer.NextRxSeq());
					NewRx (p, tcpHeader, fromAddress);
				};
				return true;
			}
			// Here the FIN is in sequence. Call NewRx if any **new** data came with the FIN
			// Make this unconditional to get back the old behavior
			if (tcpHeader.GetSequenceNumber() + SequenceNumber(p->GetSize()) > m_rxBuffer.NextRxSeq()) {
				NewRx (p, tcpHeader, fromAddress);
			};
			m_rxBuffer.IncNextRxSeq(); //bump this to account for the FIN
			States_t saveState = m_state; // Used to see if app responds
			NS_LOG_LOGIC ("TcpSocketImpl "<< this <<" peer close, state "<< m_state);
			if (!m_closeNotified) {
				NS_LOG_LOGIC ("TCP "<< this <<" calling AppCloseRequest");
				NotifyNormalClose();
				m_closeNotified = true;
			}
			NS_LOG_LOGIC ("TcpSocketImpl "<< this <<" peer close, state after "<< m_state);
			if (m_state == saveState) {
				// Need to ack, the application will close later
				SendEmptyPacket (TcpHeader::ACK);
			}
			if (m_state == LAST_ACK) {
				NS_LOG_LOGIC ("TcpSocketImpl " << this << " scheduling LATO1");
				m_lastAckEvent = Simulator::Schedule (m_rtt->RetransmitTimeout (),
											&TcpSocketImpl::LastAckTimeout,this);
			};
			} // Enclosure for using the "saveState" variable in switch structure
			break;
		case SERV_NOTIFY: // Receipt of the ACK that completed a handshake
			NS_LOG_LOGIC ("TcpSocketImpl " << this <<" Action SERV_NOTIFY");
			NS_LOG_LOGIC ("TcpSocketImpl " << this << " Connected!");
			m_connected = true; // ! This is bogus; fix when we clone the tcp
			m_endPoint->SetPeer (m_remoteAddress, m_remotePort);
			// This is also a new ACK indeed, process it
			NewAck (tcpHeader.GetAckNumber(), true);
			NotifyNewConnectionCreated (this, fromAddress);
			break;
		default: // Let another ProcessAction() to handle all other actions
			return ProcessAction (a);
	}
	return true;
}

uint32_t  TcpSocketImpl::UnAckDataCount ()
{
	NS_LOG_FUNCTION(this);
	return m_nextTxSequence - m_txBuffer.HeadSeq();
}

uint32_t  TcpSocketImpl::BytesInFlight ()
{
	NS_LOG_FUNCTION(this);
	return m_highTxMark - m_txBuffer.HeadSeq();
}

uint32_t  TcpSocketImpl::Window ()
{
	NS_LOG_FUNCTION(this);
	return m_rxWindowSize;
}

uint32_t  TcpSocketImpl::AvailableWindow ()
{
	NS_LOG_FUNCTION_NOARGS ();
	uint32_t unack = UnAckDataCount (); // Number of outstanding bytes
	uint32_t win = Window (); // Number of bytes allowed to be outstanding
	NS_LOG_LOGIC("UnAckCount="<< unack <<", Win="<< win);
	return (win < unack) ? 0 : (win - unack);
}

uint16_t TcpSocketImpl::AdvertisedWindowSize()
{
	uint32_t max = 0xffff;
	return std::min(m_rxBuffer.MaxBufferSize() - m_rxBuffer.Size(), max);
}

// Receipt of new packet, put into Rx buffer
void TcpSocketImpl::NewRx (Ptr<Packet> p, const TcpHeader& tcpHeader, const Address& fromAddress)
{
	NS_LOG_FUNCTION (this << p << "tcpHeader " << fromAddress);
	NS_LOG_LOGIC ("TcpSocketImpl " << this << " NewRx,"
				<< " seq " << tcpHeader.GetSequenceNumber()
				<< " ack " << tcpHeader.GetAckNumber()
				<< " p.size is " << p->GetSize () );

	// Put into Rx buffer
	States_t origState = m_state;
	SequenceNumber origSeq = m_rxBuffer.NextRxSeq();
	if (!m_rxBuffer.Add(p, tcpHeader)) {
		// Insert failed: No data or RX buffer full
		SendEmptyPacket (TcpHeader::ACK);
		return;
	};
	// Now send a new ACK packet acknowledging all received and delivered data
	if(++m_delAckCount >= m_delAckMaxCount) {
		SendEmptyPacket (TcpHeader::ACK);
	} else if (m_delAckEvent.IsExpired()) {
		m_delAckEvent = Simulator::Schedule (m_delAckTimeout, &TcpSocketImpl::DelAckTimeout, this);
	}
	// Notify app to receive if necessary
	if (origSeq < m_rxBuffer.NextRxSeq()) {
		// NextRxSeq advanced, we have something to send to the app
		NotifyDataRecv ();
		// Handle exceptions
		if (m_closeNotified) {
			NS_LOG_LOGIC ("Tcp " << this << " HuH?  Got data after closeNotif");
		}
		if ((m_pendingClose || (origState > ESTABLISHED)) &&
		    (m_rxBuffer.Size() == 0)) {
			// No more data to forward to app, we can close now
			ProcessPacketAction (PEER_CLOSE, p, tcpHeader, fromAddress);
		}
	};
}

// Called for all **new** ACKs, by the NewAck() and also by the
// ProcessPacketAction() upon 3-way handshake completed. This cancels
// retransmission timer and advances Tx window
void TcpSocketImpl::NewAck (SequenceNumber const& ack, bool skipTimer)
{
	NS_LOG_FUNCTION (this << ack << skipTimer); 

	if (!skipTimer) {
		NS_LOG_LOGIC (this<<" Cancelled ReTxTimeout event which was set to expire at "
				<< (Simulator::Now() + Simulator::GetDelayLeft(m_retxEvent)).GetSeconds());
		m_retxEvent.Cancel ();
		//On recieving a "New" ack we restart retransmission timer .. RFC 2988
		Time rto = m_rtt->RetransmitTimeout ();
		NS_LOG_LOGIC (this<<" Schedule ReTxTimeout at time "
				<< Simulator::Now ().GetSeconds () << " to expire at time " 
				<< (Simulator::Now () + rto).GetSeconds ());
		m_retxEvent = Simulator::Schedule (rto, &TcpSocketImpl::ReTxTimeout, this);
	}
	if (m_rxWindowSize == 0 && m_persistEvent.IsExpired ()) {
		// Zero window: Enter persist state to send 1 byte to probe
		NS_LOG_LOGIC (this<<"Enter zerowindow persist state");
		NS_LOG_LOGIC (this<<" Cancelled ReTxTimeout event which was set to expire at "
				<< (Simulator::Now() + Simulator::GetDelayLeft(m_retxEvent)).GetSeconds());
		m_retxEvent.Cancel ();
		NS_LOG_LOGIC ("Schedule persist timeout at time " 
				<<Simulator::Now ().GetSeconds () << " to expire at time "
				<< (Simulator::Now () + m_persistTime).GetSeconds());
		m_persistEvent = Simulator::Schedule (m_persistTime, &TcpSocketImpl::PersistTimeout, this);
		NS_ASSERT (m_persistTime == Simulator::GetDelayLeft (m_persistEvent));
	}
	// Note the highest ACK and tell app to send more
	NS_LOG_LOGIC("TCP " << this << " NewAck "
			<< ack << " numberAck " << (ack - m_txBuffer.HeadSeq())); // Number bytes ack'ed
	m_txBuffer.SetHeadSeq(ack);
	if (GetTxAvailable () > 0) {
		NotifySend (GetTxAvailable ());
	}
	if (ack > m_nextTxSequence) {
		m_nextTxSequence = ack; // If advanced
	}
	if (m_txBuffer.Size() == 0) {
		// No retransmit timer if no data to retransmit
		NS_LOG_LOGIC (this<<" Cancelled ReTxTimeout event which was set to expire at "
				<< (Simulator::Now() + Simulator::GetDelayLeft(m_retxEvent)).GetSeconds());
		m_retxEvent.Cancel ();
	}
	// Try to send more data
	SendPendingData (m_connected);
}

// Retransmit timeout
void TcpSocketImpl::ReTxTimeout ()
{
	NS_LOG_FUNCTION (this);
	NS_LOG_LOGIC (this<<" ReTxTimeout Expired at time "<<Simulator::Now ().GetSeconds());
	// If erroneous timeout in closed/timed-wait state, just return
	if (m_state == CLOSED || m_state == TIMED_WAIT) return;
	// If all data are received, just return
	if (m_txBuffer.HeadSeq() >= m_nextTxSequence) return;
	
	m_nextTxSequence = m_txBuffer.HeadSeq(); // Start from highest Ack
	m_rtt->IncreaseMultiplier (); // DoubleValue timeout value for next retx timer
	Retransmit ();             // Retransmit the packet
}

void TcpSocketImpl::DelAckTimeout ()
{
	SendEmptyPacket (TcpHeader::ACK);
}

void TcpSocketImpl::LastAckTimeout ()
{
	m_lastAckEvent.Cancel ();
	if (m_state == LAST_ACK) {
		Actions_t action = ProcessEvent (TIMEOUT);
		ProcessAction (action);
	}
	if (!m_closeNotified) {
		m_closeNotified = true;
	}
}

// Send 1-byte data to probe for the window size at the receiver when
// the local knowledge tells that the receiver has zero window size
void TcpSocketImpl::PersistTimeout ()
{
	NS_LOG_LOGIC ("PersistTimeout expired at "<<Simulator::Now ().GetSeconds ());
	m_persistTime = Scalar(2)*m_persistTime;
	m_persistTime = std::min(Seconds(60),m_persistTime); //maxes out at 60 sec
	//the persist timeout sends exactly one byte probes
	//this is explicit in stevens, and kind of in rfc793 p42, rfc1122 sec4.2.2.17
	Ptr<Packet> p = m_txBuffer.CopyFromSeq(1,m_nextTxSequence);
	TcpHeader tcpHeader;
	tcpHeader.SetSequenceNumber (m_nextTxSequence);
	tcpHeader.SetAckNumber (m_rxBuffer.NextRxSeq());
	tcpHeader.SetSourcePort (m_endPoint->GetLocalPort());
	tcpHeader.SetDestinationPort (m_remotePort);
	tcpHeader.SetWindowSize (AdvertisedWindowSize());

	m_tcp->SendPacket(p, tcpHeader, m_endPoint->GetLocalAddress (), m_remoteAddress, m_boundnetdevice);
	NS_LOG_LOGIC ("Schedule persist timeout at time " 
			<<Simulator::Now ().GetSeconds () << " to expire at time "
			<< (Simulator::Now () + m_persistTime).GetSeconds());
	m_persistEvent = Simulator::Schedule (m_persistTime, &TcpSocketImpl::PersistTimeout, this);
}

void TcpSocketImpl::Retransmit ()
{
	NS_LOG_FUNCTION (this);
	uint8_t flags = TcpHeader::NONE;
	// Retransmit SYN packet
	if (m_state == SYN_SENT) {
		if (m_cnCount > 0) {
			SendEmptyPacket (TcpHeader::SYN);
		} else {
			NotifyConnectionFailed ();
		}
		return;
	} 
	// Retransmit non-data packet: Only if in FIN_WAIT_1 state
	if (m_txBuffer.SizeFromSeq(m_nextTxSequence)==0) {
		if (m_state == FIN_WAIT_1) {
			// Must have lost FIN, re-send
			SendEmptyPacket (TcpHeader::FIN);
		}
		return;
	}
	// Retransmit a data packet: Extract data
	NS_ASSERT(m_nextTxSequence == m_txBuffer.HeadSeq());
	Ptr<Packet> p = m_txBuffer.CopyFromSeq (m_segmentSize, m_nextTxSequence);
	// Close-on-Empty check
	if (m_closeOnEmpty && m_txBuffer.SizeFromSeq(m_nextTxSequence) == p->GetSize()) {
		flags |= TcpHeader::FIN;
	}
	// Reset transmission timeout
	NS_LOG_LOGIC ("TcpSocketImpl " << this << " retxing seq " << m_txBuffer.HeadSeq());
	if (m_retxEvent.IsExpired () ) {
		Time rto = m_rtt->RetransmitTimeout ();
		NS_LOG_LOGIC (this<<" Schedule ReTxTimeout at time "
				<< Simulator::Now ().GetSeconds () << " to expire at time "
				<< (Simulator::Now () + rto).GetSeconds ());
		m_retxEvent = Simulator::Schedule (rto,&TcpSocketImpl::ReTxTimeout,this);
	}
	m_rtt->SentSeq (m_txBuffer.HeadSeq(), p->GetSize ());
	// And send the packet
	TcpHeader tcpHeader;
	tcpHeader.SetSequenceNumber (m_nextTxSequence);
	tcpHeader.SetAckNumber (m_rxBuffer.NextRxSeq());
	tcpHeader.SetSourcePort (m_endPoint->GetLocalPort());
	tcpHeader.SetDestinationPort (m_remotePort);
	tcpHeader.SetFlags (flags);
	tcpHeader.SetWindowSize (AdvertisedWindowSize());

	m_tcp->SendPacket (p, tcpHeader, m_endPoint->GetLocalAddress (), m_remoteAddress, m_boundnetdevice);
}

void TcpSocketImpl::CancelAllTimers()
{
	m_retxEvent.Cancel ();
	m_persistEvent.Cancel ();
	m_delAckEvent.Cancel();
	m_lastAckEvent.Cancel ();
}

void
TcpSocketImpl::SetSndBufSize (uint32_t size)
{
	m_txBuffer.SetMaxBufferSize(size);
}

uint32_t
TcpSocketImpl::GetSndBufSize (void) const
{
	return m_txBuffer.MaxBufferSize();
}

void
TcpSocketImpl::SetRcvBufSize (uint32_t size)
{
	m_rxBuffer.SetMaxBufferSize(size);
}

uint32_t
TcpSocketImpl::GetRcvBufSize (void) const
{
	return m_rxBuffer.MaxBufferSize();
}

void
TcpSocketImpl::SetSegSize (uint32_t size)
{
	m_segmentSize = size;
	NS_ABORT_MSG_UNLESS (m_state == CLOSED, "Cannot change segment size dynamically.");
}

uint32_t
TcpSocketImpl::GetSegSize (void) const
{
	return m_segmentSize;
}

void 
TcpSocketImpl::SetConnTimeout (Time timeout)
{
	m_cnTimeout = timeout;
}

Time
TcpSocketImpl::GetConnTimeout (void) const
{
	return m_cnTimeout;
}

void 
TcpSocketImpl::SetConnCount (uint32_t count)
{
	m_cnCount = count;
}

uint32_t 
TcpSocketImpl::GetConnCount (void) const
{
	return m_cnCount;
}

void 
TcpSocketImpl::SetDelAckTimeout (Time timeout)
{
	m_delAckTimeout = timeout;
}

Time
TcpSocketImpl::GetDelAckTimeout (void) const
{
	return m_delAckTimeout;
}

void
TcpSocketImpl::SetDelAckMaxCount (uint32_t count)
{
	m_delAckMaxCount = count;
}

uint32_t
TcpSocketImpl::GetDelAckMaxCount (void) const
{
	return m_delAckMaxCount;
}

}//namespace ns3
