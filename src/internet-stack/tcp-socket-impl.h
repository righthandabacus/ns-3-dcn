/* vim: set cin ts=4 sw=4 syn=cpp ru nu cuc cul lbr: */
/* -*-  Mode: C++; c-file-style: "gnu"; indent-tabs-mode:nil; -*- */
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
#ifndef TCP_SOCKET_IMPL_H
#define TCP_SOCKET_IMPL_H

#include <stdint.h>
#include <queue>
#include "ns3/callback.h"
#include "ns3/traced-value.h"
#include "ns3/tcp-socket.h"
#include "ns3/ptr.h"
#include "ns3/ipv4-address.h"
#include "ns3/event-id.h"
#include "tcp-typedefs.h"
#include "tcp-tx-buffer.h"
#include "tcp-rx-buffer.h"
#include "rtt-estimator.h"
#include "ns3/qbb-net-device.h"


namespace ns3 {

class Ipv4EndPoint;
class Node;
class Packet;
class TcpL4Protocol;
class TcpHeader;

/**
 * \ingroup socket
 * \ingroup tcp
 *
 * \brief An implementation of a stream socket using TCP.
 *
 * This class contains an RFC793 implementation of TCP, as well as a sockets
 * interface for talking to TCP.  This serves as a base for other TCP functions
 * where the sliding window mechanism is handled here.  This class provides
 * connection orientation and sliding window flow control.
 */
class TcpSocketImpl : public TcpSocket
{
public:
	static TypeId GetTypeId (void);
	/**
	 * Create an unbound tcp socket.
	 */
	TcpSocketImpl ();
	TcpSocketImpl (const TcpSocketImpl& sock);
	virtual ~TcpSocketImpl ();

	// Set associated Node, TcpL4Protocol, RttEstimator to this socket
	virtual void SetNode (Ptr<Node> node);
	virtual void SetTcp (Ptr<TcpL4Protocol> tcp);
	virtual void SetRtt (Ptr<RttEstimator> rtt);

	// Necessary implementations of null functions from ns3::Socket
	virtual enum SocketErrno GetErrno (void) const;	// returns m_errno
	virtual Ptr<Node> GetNode (void) const;	// returns m_node
	virtual int Bind (void);	// Bind a socket by setting up endpoint in TcpL4Protocol
	virtual int Bind (const Address &address);	// ... endpoint of specific addr or port
	virtual int Close (void);	// Close by app: Kill socket upon tx buffer emptied
	virtual int ShutdownSend (void);	// Assert the m_shutdownSend flag to prevent send to network
	virtual int ShutdownRecv (void);	// Assert the m_shutdownRecv flag to prevent forward to app
	virtual int Connect(const Address &address); // Setup endpoint and call ProcessAction() to connect
	virtual int Listen(void); // Verify the socket is in a correct state and call ProcessAction() to listen
	virtual int Send (Ptr<Packet> p, uint32_t flags); // Call by app to send data to network
	virtual int SendTo(Ptr<Packet> p, uint32_t flags, const Address &toAddress); // Same as Send(), toAddress is insignificant
	virtual uint32_t GetTxAvailable (void) const; // Available Tx buffer size
	virtual uint32_t GetRxAvailable (void) const; // Available-to-read data size, i.e. value of m_rxAvailable
	virtual Ptr<Packet> Recv (uint32_t maxSize, uint32_t flags); // Return a packet to be forwarded to app
	virtual Ptr<Packet> RecvFrom (uint32_t maxSize, uint32_t flags, Address &fromAddress); // ... and write the remote address at fromAddress
	virtual int GetSockName (Address &address) const; // Return local addr:port in address
	virtual void BindToNetDevice (Ptr<NetDevice> netdevice);

protected:
	// Helper functions
	int CommonBind (void); // Common part of the two Bind(), i.e. set callback and remembering local addr:port
	void ForwardUp (Ptr<Packet> p, Ipv4Address ipv4, uint16_t port); // For L3 protocol to send back the received pkt
	void Destroy (void); // Kill this socket by zeroing its attributes
	void SendEmptyPacket(uint8_t flags); // Send a empty packet that carries a flag, e.g. ACK
	void SendRST(); // Send reset and tear down this socket
	int SetupEndpoint(); // Configure m_endpoint for local addr for given remote addr
	void CompleteFork(Ptr<Packet>, const TcpHeader&, const Address& fromAddress);
	void ConnectionSucceeded(); // Schedule-friendly wrapper for Socket::NotifyConnectionSucceeded()
	void DeviceUnblocked(Ptr<NetDevice> nd, uint32_t avail); // To be called by the QbbNetDevice upon tx buffer available again
	void CancelNetDeviceCallback(Ptr<QbbNetDevice> qbb);
	bool SendPendingData(bool withAck = false);

	// State transition functions
	Actions_t ProcessEvent (Events_t e); // Given an event happened, check current state, tell corr. actions
	bool ProcessAction (Actions_t a); // Action handlers
	bool ProcessPacketAction (Actions_t a, Ptr<Packet> p, const TcpHeader& tcpHeader, const Address& fromAddress);

	// Window management
	virtual uint32_t UnAckDataCount(); // Return count of number of unacked bytes
	virtual uint32_t BytesInFlight();  // Return total bytes in flight
	virtual uint32_t Window();         // Return the max possible number of unacked bytes
	virtual uint32_t AvailableWindow();// Return unfilled portion of window
	virtual uint16_t AdvertisedWindowSize(); // The amount of Rx window announced to the peer

	// Manage data tx/rx
	virtual void NewRx (Ptr<Packet>, const TcpHeader&, const Address&);	// Recv of a data, put into buffer, call L7 to get it if necessary
	virtual Ptr<TcpSocketImpl> Fork () = 0; // Call CopyObject<> to clone me
	virtual void NewAck (SequenceNumber const& seq, bool skipTimer = false); // Update buffers corr. to ACK
	virtual void DupAck (const TcpHeader& t, uint32_t count) = 0;
	virtual void ReTxTimeout (); // Halving cwnd and call Retransmit()
	virtual void DelAckTimeout ();  // Action upon delay ACK timeout, i.e. send an ACK
	virtual void LastAckTimeout (); // Timeout at LAST_ACK, close the connection
	virtual void PersistTimeout (); // Send 1 byte probe to get an updated window size
	void Retransmit (); // Retransmit the oldest packet
	// All timers are cancelled when the endpoint is deleted, to insure
	// we don't have additional activity
	void CancelAllTimers();

	// Implementing ns3::TcpSocket -- Attribute get/set
	virtual void     SetSndBufSize (uint32_t size);
	virtual uint32_t GetSndBufSize (void) const;
	virtual void     SetRcvBufSize (uint32_t size);
	virtual uint32_t GetRcvBufSize (void) const;
	virtual void     SetSegSize (uint32_t size);
	virtual uint32_t GetSegSize (void) const;
	virtual void     SetSSThresh (uint32_t threshold) = 0;
	virtual uint32_t GetSSThresh (void) const = 0;
	virtual void     SetInitialCwnd (uint32_t cwnd) = 0;
	virtual uint32_t GetInitialCwnd (void) const = 0;
	virtual void     SetConnTimeout (Time timeout);
	virtual Time     GetConnTimeout (void) const;
	virtual void     SetConnCount (uint32_t count);
	virtual uint32_t GetConnCount (void) const;
	virtual void     SetDelAckTimeout (Time timeout);
	virtual Time     GetDelAckTimeout (void) const;
	virtual void     SetDelAckMaxCount (uint32_t count);
	virtual uint32_t GetDelAckMaxCount (void) const;

protected:	// TCP variables
	// Counters and events
	EventId  m_retxEvent;       //< Retransmission event
	EventId  m_lastAckEvent;    //< Last ACK timeout event
	EventId  m_delAckEvent;     //< Delayed ACK timeout event
	EventId  m_persistEvent;    //< Persist event: Send 1-byte probe
	uint32_t m_dupAckCount;     //< Dupack counter
	uint32_t m_delAckCount;     //< Delayed ACK counter
	uint32_t m_delAckMaxCount;  //< Number of packet to fire an ACK before delay timeout
	uint32_t m_cnCount;         //< Count of remaining connection retries
	Time     m_delAckTimeout;   //< Time to delay an ACK
	Time     m_persistTime;     //< Time between sending 1-byte probes
	Time     m_cnTimeout;       //< Timeout for connection retry

	// Connections to other layers of TCP/IP
	Ipv4EndPoint       *m_endPoint;
	Ptr<Node>           m_node;
	Ptr<TcpL4Protocol>  m_tcp;
	Ipv4Address         m_remoteAddress;
	uint16_t            m_remotePort;
	Ipv4Address         m_localAddress;
	uint16_t            m_localPort;

	// Round trip time estimation
	Ptr<RttEstimator> m_rtt;

	// Rx and Tx buffer management
	SequenceNumber m_nextTxSequence; // Next seqno to be sent, ReTx pushes it back
	SequenceNumber m_highTxMark;     // Highest seqno ever sent, regardless of ReTx
	TcpRxBuffer    m_rxBuffer;       // Rx buffer (reordering buffer)
	TcpTxBuffer    m_txBuffer;       // Tx buffer

	// State-related attributes
	States_t          m_state;         // TCP state
	enum SocketErrno  m_errno;         // Socket error code
	bool              m_closeNotified; // Told app to close socket
	bool              m_closeOnEmpty;  // Close socket upon tx buffer emptied
	bool              m_pendingClose;  // Close socket once all packets rx in sequence
	bool              m_shutdownSend;  //< Send no longer allowed
	bool              m_shutdownRecv;  //< Receive no longer allowed
	bool              m_connected;     //< Connection established
	bool              m_blocking;      //< Blocking send calls

	// Window management
	uint32_t               m_segmentSize;  //SegmentSize
	uint32_t               m_rxWindowSize; //Flow control window at remote side
};

}//namespace ns3

#endif /* TCP_SOCKET_IMPL_H */
