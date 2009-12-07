/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/* vim: set cin sw=4 syn=cpp ru nu ts=4 cul cuc lbr: */
//
// Copyright (c) 2006 Georgia Tech Research Corporation
// Copyright (c) 2009 Adrian Sai-wah Tam
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
// Author: Rajib Bhattacharjea<raj.b@gatech.edu>
//         Adrian S.-W. Tam <adrian.sw.tam@gmail.com>
//

#ifndef __tcp_tx_buffer_h__
#define __tcp_tx_buffer_h__

#include <list>
#include "sequence-number.h"
#include "ns3/ptr.h"

namespace ns3
{
class Packet;

/**
 * \ingroup tcp
 *
 * \brief class for keeping the data sent by the application to the TCP socket, i.e.
 *        the sending buffer.
 */
class TcpTxBuffer {
public:
	TcpTxBuffer (uint32_t n=0);
	virtual ~TcpTxBuffer ();
	// Accessors
	SequenceNumber const& HeadSeq () const { return firstByteSeq; }
	uint32_t Size () const { return size; }
	uint32_t MaxBufferSize () const { return maxBuffer; }
	void SetMaxBufferSize (uint32_t n) { maxBuffer = n; }
	uint32_t Available() const { return maxBuffer - size; }
	// Append a data packet to the end of the buffer
	bool Add (Ptr<Packet> p);
	// Inquire available data from the sequence number
	uint32_t SizeFromSeq (const SequenceNumber& seq) const;
	// Copy data of size numBytes into a packet, starting from the specified seq num
	Ptr<Packet> CopyFromSeq (uint32_t numBytes, const SequenceNumber& seq);
	// Discard data up to this seq num
	bool SetHeadSeq(const SequenceNumber& seq);
private:
	SequenceNumber firstByteSeq;   //< Sequence number of the first byte in data
	uint32_t size;                 //< Number of data bytes
	uint32_t maxBuffer;            //< Max number of data bytes in buffer
	std::list<Ptr<Packet> > data;  //< Corresponding data (may be null)
	bool unused;                   //< Not yet extracted any buffered data
};

}//namepsace ns3

#endif
