/* vim: set cin ts=4 sw=4 syn=cpp ru nu cuc cul lbr: */
/*
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
 * Author: Adrian Sai-wah Tam <adrian.sw.tam@gmail.com>
 */
#ifndef TCP_NEWRENO_H
#define TCP_NEWRENO_H

#include "tcp-rfc793.h"

namespace ns3 {

/**
 * \ingroup socket
 * \ingroup tcp
 *
 * \brief An implementation of a stream socket using TCP.
 *
 * This class contains the NewReno implementation of TCP
 */
class TcpNewReno : public TcpSocketImpl
{
public:
	static TypeId GetTypeId (void);
	/**
	 * Create an unbound tcp socket.
	 */
	TcpNewReno ();
	TcpNewReno (const TcpNewReno& sock);
	virtual ~TcpNewReno ();

	// Set associated Node, TcpL4Protocol, RttEstimator to this socket
	virtual void SetNode (Ptr<Node> node);

protected:
	virtual uint32_t Window();         // Return the max possible number of unacked bytes
	virtual Ptr<TcpSocketImpl> Fork (); // Call CopyObject<TcpNewReno> to clone me
	virtual void NewAck (SequenceNumber const& seq, bool skipTimer = false); // Inc cwnd and call NewAck() of parent
	virtual void DupAck (const TcpHeader& t, uint32_t count);  // Halving cwnd and reset nextTxSequence
	virtual void ReTxTimeout (); // Halving cwnd and call Retransmit()

	// Implementing ns3::TcpSocket -- Attribute get/set
	virtual void     SetSegSize (uint32_t size);
	virtual void     SetSSThresh (uint32_t threshold);
	virtual uint32_t GetSSThresh (void) const;
	virtual void     SetInitialCwnd (uint32_t cwnd);
	virtual uint32_t GetInitialCwnd (void) const;

protected:	// TCP variables
	TracedValue<uint32_t>  m_cWnd;         //Congestion window
	uint32_t               m_ssThresh;     //Slow Start Threshold
	uint32_t               m_initialCWnd;  //Initial cWnd value
};

}//namespace ns3

#endif /* TCP_NEWRENO_H */
