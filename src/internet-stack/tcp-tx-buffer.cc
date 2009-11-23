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
//         Adrian Sai-wah Tam <adrian.sw.tam@gmail.com>
//

#include <iostream>
#include <algorithm>
#include <string.h>
#include "ns3/packet.h"
#include "tcp-tx-buffer.h"
#include "ns3/fatal-error.h"
#include "ns3/log.h"

NS_LOG_COMPONENT_DEFINE ("TcpTxBuffer");

namespace ns3
{

TcpTxBuffer::TcpTxBuffer (uint32_t n) : firstByteSeq(n), size (0), maxBuffer(32768), data (0), unused(true)
{
}

TcpTxBuffer::~TcpTxBuffer()
{
}

bool TcpTxBuffer::Add (Ptr<Packet> p)
{
	NS_LOG_LOGIC("Inserting packet of size "<< p->GetSize() << " at headSeq=" << firstByteSeq << " availSize=" << Available());
	if ( p->GetSize() <= Available() ) {
		if (p->GetSize() > 0) {
			data.push_back(p);
			size += p->GetSize();
			NS_LOG_LOGIC("Added pkt of size "<< p->GetSize()<<", size=" << size <<" headSeq="<< firstByteSeq <<" lastSeq="<< firstByteSeq+SequenceNumber(size));
		};
		return true;
	};
	return false;
}

uint32_t TcpTxBuffer::SizeFromSeq (const SequenceNumber& seq) const
{
	NS_LOG_FUNCTION(this << seq);
	// Sequence of last byte in buffer
	SequenceNumber lastSeq = firstByteSeq + SequenceNumber(size);
	// Non-negative size
	NS_LOG_LOGIC("HeadSeq="<< firstByteSeq <<", lastSeq=" << lastSeq <<", size=" << size << ", returns " << lastSeq - seq);
	return (lastSeq - seq);
}

Ptr<Packet> TcpTxBuffer::CopyFromSeq(uint32_t numBytes, const SequenceNumber& seq)
{
	NS_LOG_FUNCTION(this << numBytes << seq);
	uint32_t s = std::min(numBytes, SizeFromSeq(seq)); // Insure not beyond end of data
	if (s == 0) {
		return Create<Packet>(); // Empty packet returned
	};
	if (data.size() == 0) {
		// No actual data, just return dummy-data packet of correct size
		return Create<Packet> (s);
	};

	// Extract data from the buffer and return
	uint32_t offset = seq - firstByteSeq;
	uint32_t count = 0;      //< Offset of the first byte of a packet in the buffer
	uint32_t pktSize = 0;
	bool beginFound = false;
	int pktCount = 0;
	Ptr<Packet> outPacket;
	NS_LOG_LOGIC("There are "<< data.size() <<" number of packets in buffer");
	for (std::list<Ptr<Packet> >::const_iterator i=data.begin(); i!=data.end(); ++i) {
		pktCount++;
		pktSize = (*i)->GetSize();
		if (!beginFound) {
			// Look for first fragment
			if (count + pktSize > offset) {
				NS_LOG_LOGIC("First byte found at packet #"<<pktCount<<" of offset "<< count <<" len="<< pktSize);
				beginFound = true;
				unused = false;
				uint32_t packetOffset = offset - count;
				uint32_t fragmentLength = count + pktSize - offset;
				if (fragmentLength >= s) {
					// Data to be copied falls entirely in this packet
					return (*i)->CreateFragment (packetOffset, s);
				} else {
					outPacket = (*i)->CreateFragment (packetOffset, fragmentLength);
				}
				NS_LOG_LOGIC("Output packet is now of size " << outPacket->GetSize());
			}
		} else if (count + pktSize >= offset + s) {
			// Last packet fragment found
			NS_LOG_LOGIC("Last byte found at packet #"<<pktCount<<" of offset "<< count <<" len="<< pktSize);
			uint32_t fragmentLength = offset + s - count;
			Ptr<Packet> endFragment = (*i)->CreateFragment(0, fragmentLength);
			outPacket->AddAtEnd(endFragment);
			NS_LOG_LOGIC("Output packet is now of size " << outPacket->GetSize());
			break;
		} else {
			NS_LOG_LOGIC("Appending to output the packet #"<<pktCount<<" of offset "<< count <<" len="<< pktSize);
			outPacket->AddAtEnd(*i);
			NS_LOG_LOGIC("Output packet is now of size " << outPacket->GetSize());
		}
		count += pktSize;
	}
	NS_ASSERT(outPacket->GetSize() == s);
	return outPacket;
}

bool TcpTxBuffer::SetHeadSeq(const SequenceNumber& seq)
{
	NS_LOG_FUNCTION(this << seq);
	NS_LOG_LOGIC("size="<< size <<" headSeq="<< firstByteSeq <<" maxBuffer="<< maxBuffer <<" numPkts="<< data.size() << " unused=" << unused);
	// Cases that we don't need to scan the buffer
	if (firstByteSeq >= seq) return false;
	if (unused) {
		firstByteSeq = seq;
		return false;
	};

	// Scan the buffer and discard packets
	uint32_t offset = seq - firstByteSeq;
	uint32_t pktSize;
	NS_LOG_LOGIC("Offset="<< offset);
	std::list<Ptr<Packet> >::iterator i=data.begin();
	while (i != data.end()) {
		if (offset > (*i)->GetSize()) {
			// This packet is behind the seqnum. Remove this packet from the buffer
			pktSize = (*i)->GetSize();
			size -= pktSize;
			offset -= pktSize;
			i = data.erase(i);
			firstByteSeq += pktSize;
			NS_LOG_LOGIC("Removed one packet of size "<< pktSize <<", offset="<< offset);
		} else if (offset > 0) {
			// Part of the packet is behind the seqnum. Fragment
			pktSize = (*i)->GetSize() - offset;
			*i = (*i)->CreateFragment(offset, pktSize);
			size -= offset;
			firstByteSeq += offset;
			NS_LOG_LOGIC("Fragmented one packet by size "<< offset << ", new size=" << pktSize);
			break;
		};
	}
	// Catching the case of ACKing a FIN
	if (size == 0) {
		firstByteSeq = seq;
		unused = true;
	};
	NS_LOG_LOGIC("size="<< size <<" headSeq="<< firstByteSeq <<" maxBuffer="<< maxBuffer <<" numPkts="<< data.size());
	NS_ASSERT(firstByteSeq == seq);
	// Stupid scan to make sure size is correct
	pktSize = 0;
	offset = 0;
	for (i=data.begin(); i!= data.end(); ++i) {
		offset++;
		pktSize += (*i)->GetSize();
	};
	NS_ASSERT(offset == data.size());
	NS_ASSERT(size == pktSize);
	return true;
}

}//namepsace ns3
