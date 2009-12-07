/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/* vim: set cin sw=4 syn=cpp ru nu ts=4 cul cuc lbr: */
//
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
// Author: Adrian S.-W. Tam <adrian.sw.tam@gmail.com>
//

#ifndef __tcp_rx_buffer_h__
#define __tcp_rx_buffer_h__

#include <map>
#include "sequence-number.h"
#include "ns3/ptr.h"
#include "ns3/tcp-header.h"

namespace ns3
{
class Packet;

/**
 * \ingroup tcp
 *
 * \brief class for the reordering buffer that keeps the data from lower layer, i.e.
 *        TcpL4Protocol, sent to the application
 */
class TcpRxBuffer {
public:
	TcpRxBuffer (uint32_t n=0);
	virtual ~TcpRxBuffer ();
	// Accessors
	SequenceNumber const& NextRxSeq () const { return nextRxSeq; }
	void IncNextRxSeq ();
	void SetNextRxSeq (const SequenceNumber& s) { nextRxSeq = s; }
	uint32_t MaxBufferSize () const { return maxBuffer; }
	void SetMaxBufferSize (uint32_t  s) { maxBuffer = s; }
	uint32_t Size () const { return size; }
	uint32_t Available () const { return availBytes; }
	// Insert a data packet to the buffer in a correct position 
	bool Add (Ptr<Packet> p, TcpHeader const& tcph);
	// Update the counters to a correct value after an insert
	void CleanUpCounters();
	// Extract data from the head of the buffer
	Ptr<Packet> Extract(uint32_t maxSize);
public:
	typedef std::map<SequenceNumber, Ptr<Packet> >::iterator BufIterator;
	SequenceNumber nextRxSeq;   //< Sequence number of the first byte in data
	uint32_t size;              //< Number of total data bytes in the buffer, not necessarily contiguous
	uint32_t maxBuffer;         //< Upper bound of the number of data bytes in buffer
	uint32_t availBytes;        //< Number of bytes available to read, i.e. contiguous block at head
	std::map<SequenceNumber, Ptr<Packet> > data;
	                            //< Corresponding data (may be null)
};

}//namepsace ns3

#endif
