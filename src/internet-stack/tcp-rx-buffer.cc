/* vim:set cin ts=4 cul syn=cpp: */
/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
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

#include "tcp-rx-buffer.h"
#include "ns3/packet.h"
#include "ns3/fatal-error.h"
#include "ns3/log.h"

NS_LOG_COMPONENT_DEFINE ("TcpRxBuffer");

namespace ns3
{

TcpRxBuffer::TcpRxBuffer(uint32_t n) : nextRxSeq(n), size(0), maxBuffer(32768), availBytes(0)
{
}

TcpRxBuffer::~TcpRxBuffer()
{
}

void TcpRxBuffer::IncNextRxSeq ()
{
	// Increment nextRxSeq is valid only if we don't have any data buffered
	NS_ASSERT(size == 0);
	nextRxSeq++;
}

// Add a packet into the buffer and update the availBytes counter to reflect
// the number of bytes ready to send to the application. This function handles
// overlap by triming the head of the inputted packet and removing data from
// the buffer that overlaps the tail of the inputted packet
bool
TcpRxBuffer::Add(Ptr<Packet> p, TcpHeader const& tcph)
{
	uint32_t pktSize = p->GetSize();
	SequenceNumber pktSeq = tcph.GetSequenceNumber();
	NS_LOG_LOGIC("Add pkt " << p << " len=" << pktSize << " seq=" << pktSeq
					<< ", when NextRxSeq=" << nextRxSeq << ", buffsize=" << size);

	// Remove overlapped part at packet head
	uint32_t head = 0;
	if (pktSeq < nextRxSeq) {
		head = nextRxSeq - pktSeq;
		pktSize = (head < pktSize)? pktSize-head : 0;
		pktSeq = nextRxSeq;
	} else {
		BufIterator prev = data.lower_bound(pktSeq);
		if (prev != data.begin()) {
			NS_ASSERT(prev->first >= pktSeq);
			--prev;
			SequenceNumber prevSeq = prev->first + SequenceNumber(prev->second->GetSize());
			if (prevSeq > pktSeq) {
				head = prevSeq - pktSeq;
				pktSize = (head < pktSize)? pktSize-head : 0;
				pktSeq = prevSeq;
			};
		};
	};
	// Cap pktSize to prevent exceeding window
	if (data.size()) {
		SequenceNumber maxSeq = data.begin()->first + SequenceNumber(maxBuffer);
		NS_LOG_LOGIC("MaxSeq=" << maxSeq << " while pktSeq=" << pktSeq);
		if (maxSeq > pktSeq) {
			pktSize = std::min(pktSize, uint32_t(maxSeq - pktSeq));
			NS_LOG_LOGIC("pktSize updated to " << pktSize);
		} else {
			pktSize = 0;
		};
	};
	// We now know how much we are going to store, trim the packet
	if (pktSize == 0) {
		NS_LOG_LOGIC("Nothing to buffer");
		return false;	// Nothing to buffer anyway
	} else {
		p = p->CreateFragment(head, pktSize);
		NS_ASSERT(pktSize == p->GetSize());
		NS_LOG_LOGIC("Trimed packet from " << pktSeq <<"(+"<< head <<") to size " << pktSize);
	};
	// Search for overlapped data in buffer and remove them
	SequenceNumber lastSeq = pktSeq + SequenceNumber(pktSize);
	BufIterator next = data.upper_bound(pktSeq);
	while (next != data.end()) {
		if (lastSeq <= next->first) break;
		if (next->first + SequenceNumber(next->second->GetSize()) <= lastSeq) {
			// Totally redundant
			NS_LOG_LOGIC("Removed packet of seqno=" << next->first << " len=" << next->second->GetSize());
			data.erase(next++);
		} else {
			// Partially redundant
			uint32_t h = lastSeq - next->first;
			uint32_t s = next->second->GetSize() - h;
			NS_LOG_LOGIC("Fragmented packet of seqno=" << next->first << " len=" << next->second->GetSize() << " to len=" << s);
			data [ lastSeq ] = next->second->CreateFragment(h,s);
			data.erase(next);
			break;
		};
	};
	// Insert packet into buffer
	NS_ASSERT(data.find(pktSeq) == data.end()); // Shouldn't be there yet
	data [ pktSeq ] = p;
	NS_LOG_LOGIC("Buffered packet of seqno=" << pktSeq << " len=" << p->GetSize());
	next = data.upper_bound(pktSeq);
	if (next != data.end()) {
		// Verify: shall never be overlap in case there is a packet follows it
		NS_ASSERT( next->first >= pktSeq + SequenceNumber(pktSize) );
	};
	// Update variables
	if (pktSeq == nextRxSeq) {
		// In-sequence: Advance the next expected sequence
		nextRxSeq += pktSize;
		size += pktSize;
		availBytes += pktSize;
		NS_LOG_LOGIC("Advanced nextRxSeq to "<< nextRxSeq <<", bufsize=" << size);
		CleanUpCounters();
	} else if (pktSeq > nextRxSeq) {
		// Out-of-sequence: Update the occupancy only
		size += pktSize;
		NS_LOG_LOGIC("Packet buffered without advancing nextRxSeq, bufsize=" << size);
	};
	return true;
};

// Update the nextRxSeq and other counters to reflect the existence of
// a new contiguous chuck
void
TcpRxBuffer::CleanUpCounters()
{
	NS_LOG_FUNCTION(this);
	NS_LOG_LOGIC("NextRxSeq = "<< nextRxSeq);
	BufIterator i = data.find(nextRxSeq);
	while (i != data.end()) {
		NS_LOG_LOGIC("Checking packet of seqno=" << i->first <<", size=" << i->second->GetSize());
		// Any gap here?
		if (i->first > nextRxSeq) {
			break;
		};
		// No gap, update counters
		uint32_t pktSize = i->second->GetSize();
		nextRxSeq += pktSize;
		availBytes += pktSize;
		++i;
		NS_LOG_LOGIC("Advanced nextRxSeq to " << nextRxSeq);
	};
};

// Extract no more than maxSize byte from the head of the buffer
// as indicated by nextRxSeq and send to the application.
Ptr<Packet>
TcpRxBuffer::Extract(uint32_t maxSize)
{
	uint32_t extractSize = std::min(maxSize, availBytes);
	NS_LOG_LOGIC("Requested to extract "<< extractSize <<" bytes from TcpRxBuffer of size="<< size);
	if (extractSize == 0) return 0;  // No contiguous block to return
	NS_ASSERT(data.size()); // At least we have something to extract
	Ptr<Packet> outPkt = Create<Packet>(); // The packet that contains all the data to return
	BufIterator i;
	while (extractSize) {
		// Check the buffered data for delivery
		i = data.begin ();
		if (i->first > nextRxSeq) break; // No more in-sequence data exists
		// Check if we send the whole pkt or just a partial
		uint32_t pktSize = i->second->GetSize();
		if (pktSize <= extractSize) {
			// Whole packet is extracted
			outPkt->AddAtEnd(i->second);
			data.erase(i);
			size -= pktSize;
			availBytes -= pktSize;
			extractSize -= pktSize;
		} else {
			// Partial is extracted and done
			outPkt->AddAtEnd(i->second->CreateFragment(0, extractSize));
			data[i->first + SequenceNumber(extractSize)] = i->second->CreateFragment(extractSize, pktSize-extractSize);
			data.erase(i);
			size -= extractSize;
			availBytes -= extractSize;
			extractSize = 0;
		};
	};
	if (outPkt->GetSize() == 0) {
		NS_LOG_LOGIC("Nothing extracted.");
		return 0;
	};
	NS_LOG_LOGIC("Extracted "<< outPkt->GetSize() <<" bytes, bufsize="<< size <<", num pkts in buffer="<< data.size());
	return outPkt;
};

}//namepsace ns3
