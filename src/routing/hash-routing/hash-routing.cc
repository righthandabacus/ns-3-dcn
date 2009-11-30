/* -*- Mode: C++; c-file-style: "gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2008, 2009 Polytechnic Institute of NYU, New York University
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
 * Author: Chang Liu <cliu02@students.poly.edu> and
 *         Adrian S. Tam <adrian.sw.tam@gmail.com>
 */

#include "ns3/log.h"
#include "ns3/object.h"
#include "ns3/packet.h"
#include "ns3/net-device.h"
#include "ns3/ipv4-route.h"
#include "ns3/ipv4-routing-table-entry.h"
#include "hash-routing.h"
#include "ns3/boolean.h"
#include "ns3/uinteger.h"
#include "ns3/tcp-header.h"
#include "ns3/udp-header.h"
#include "ns3/cn-header.h"
#include "ns3/channel.h"
#include "ns3/node.h"
#include "ns3/random-variable.h"

NS_LOG_COMPONENT_DEFINE ("HashRouting");

namespace ns3 {

NS_OBJECT_ENSURE_REGISTERED (HashRouting);

TypeId 
HashRouting::GetTypeId (void)
{ 
  static TypeId tid = TypeId ("ns3::HashRouting")
    .SetParent<Ipv4RoutingProtocol> ()
    .AddAttribute ("EnableReroute",
                   "Enable rerouting upon congestion",
                   BooleanValue (true),
                   MakeBooleanAccessor (&HashRouting::m_enableRR),
                   MakeBooleanChecker ())
    .AddAttribute ("RerouteThreshold",
                   "Number of congestion signal to be seen before reroute triggered",
                   UintegerValue (3),
                   MakeUintegerAccessor (&HashRouting::m_rrThresh),
                   MakeUintegerChecker<uint32_t> ())
    .AddAttribute ("CnLifetime",
                   "Lifetime for a congestion signal record",
                   TimeValue (Seconds (3)),
                   MakeTimeAccessor (&HashRouting::m_lifetime),
                   MakeTimeChecker ())
    ;
  return tid;
}

HashRouting::HashRouting () 
{
  NS_LOG_FUNCTION_NOARGS ();
}

HashRouting::~HashRouting ()
{
  NS_LOG_FUNCTION_NOARGS ();
}

void
HashRouting::AddRoute (const Ipv4Address& dest, const Ipv4Mask& mask, uint32_t interface)
{
	Ptr<DestRoute> r = Create<DestRoute>(dest, mask, interface);
	m_destRouteTable.push_back(r);
	NS_LOG_LOGIC("New route for interface "<< interface <<": "<< dest <<"/"<< mask);
};

flowid
HashRouting::GetTuple(Ptr<const Packet> packet, const Ipv4Header& header)
{
	flowid tuple = flowid(header);
	if (header.GetProtocol() == 17) {
		// UDP packet
		UdpHeader udph;
		packet->PeekHeader(udph);
		tuple.SetSPort(udph.GetSourcePort());
		tuple.SetDPort(udph.GetDestinationPort());
	} else if (header.GetProtocol() == 6) {
		// TCP packet
		TcpHeader tcph;
		packet->PeekHeader(tcph);
		tuple.SetSPort(tcph.GetSourcePort());
		tuple.SetDPort(tcph.GetDestinationPort());
	};
	return tuple;
};

uint32_t
HashRouting::Lookup (flowid fid)
{
	NS_LOG_FUNCTION(this);
	uint32_t outPort;
	const Ipv4Address destAddr = Ipv4Address(fid.GetDAddr());
	if (RequestDestRoute(destAddr, outPort) ) {
		NS_LOG_LOGIC("Destination "<< destAddr << " routed to port "<< outPort);
	} else if (RequestFlowRoute(fid, outPort) ) {
		NS_LOG_LOGIC(fid << " routed as a flow to port "<< outPort);
	} else {
		// Hash-based routing
		uint32_t numUpPorts = (m_ipv4->GetNInterfaces()-1)/2;
		outPort = (Hash(fid) % numUpPorts) + numUpPorts + 1;
		NS_LOG_LOGIC("Packet of "<< fid <<" hash-routed to port "<< outPort);
	};
	return outPort;
}

Ptr<Ipv4Route>
HashRouting::RouteOutput (Ptr<Packet> p, const Ipv4Header &header, uint32_t oif, Socket::SocketErrno &sockerr)
{      
	// Hash-routing is for unicast destination only
	Ipv4Address a = header.GetDestination();
	if (a.IsMulticast() || a.IsBroadcast()) {
		NS_LOG_LOGIC("Non-unicast destination is not supported");
		sockerr = Socket::ERROR_NOROUTETOHOST;
		return 0;
	};
	// Check for a route, and construct the Ipv4Route object
	sockerr = Socket::ERROR_NOTERROR;
	uint32_t iface = Lookup(GetTuple(p, header));
   	Ptr<NetDevice> dev = m_ipv4->GetNetDevice(iface); // Convert output port to device
   	Ptr<Channel> channel = dev->GetChannel(); // Channel used by the device
	uint32_t otherEnd = (channel->GetDevice(0)==dev)?1:0; // Which end of the channel?
	Ptr<Node> nextHop = channel->GetDevice(otherEnd)->GetNode(); // Node at other end
   	uint32_t nextIf = channel->GetDevice(otherEnd)->GetIfIndex(); // Iface num at other end
	Ipv4Address nextHopAddr = nextHop->GetObject<Ipv4>()->GetAddress(nextIf,0).GetLocal(); // Addr of other end
	Ptr<Ipv4Route> r = Create<Ipv4Route> ();
	r->SetOutputDevice(m_ipv4->GetNetDevice(iface));
	r->SetGateway(nextHopAddr);
	r->SetSource(m_ipv4->GetAddress(iface,0).GetLocal());
	r->SetDestination(a);
	return r;
}

bool 
HashRouting::RouteInput  (Ptr<const Packet> p, const Ipv4Header &header, Ptr<const NetDevice> idev,
		UnicastForwardCallback ucb, MulticastForwardCallback mcb,
		LocalDeliverCallback lcb, ErrorCallback ecb) 
{ 
	NS_LOG_FUNCTION (this << p << header << header.GetSource () << header.GetDestination () << idev);
	// Check if input device supports IP
	NS_ASSERT (m_ipv4->GetInterfaceForDevice (idev) >= 0);
	uint32_t iif = m_ipv4->GetInterfaceForDevice (idev);
	uint32_t outPort;
	Ipv4Address a = header.GetDestination();

	// Congestion signal processing
	if (header.GetProtocol() == 0xFF && m_enableRR && IsEdge(m_ipv4->GetAddress(1,0).GetLocal())) {
		// We are routing a congestion control signal at an edge switch
		CnHeader cnh;
		p->PeekHeader(cnh);
		flowid tuple = cnh.GetFlow();
		uint32_t oldPort = Lookup(tuple);
		// Then check if we need to do rerouting
		if (NeedReroute(tuple) &&
				RequestDestRoute(a, outPort) &&
				(header.GetTtl()==64 || !IsEdge(header.GetSource()))) {
			// If the congestion signal is for a host local to this
			// edge switch, and flow needs reroute, and the congestion
			// signal is not from the receiving edge, then do the
			// reroute and return
			outPort = Reroute(tuple, oldPort);
			NS_LOG_INFO("Rerouted "<< tuple <<" from "<< oldPort <<" to "<< outPort);
		};
		NS_LOG_LOGIC("CN for "<<tuple<<" forwarded to host");
	};

	// Hash-routing is for unicast destination only
	if (a.IsMulticast() || a.IsBroadcast()) {
		NS_LOG_LOGIC("Non-unicast destination is not supported");
		return 0;
	};

	// Check if the destination is local
	if (IsLocal(a)) {
		NS_LOG_LOGIC ("local destination- calling local callback");
		lcb (p, header, iif);
	};
	// Check if input device supports IP forwarding
	if (m_ipv4->IsForwarding (iif) == false) {
		NS_LOG_LOGIC ("Forwarding disabled for this interface");
		ecb (p, header, Socket::ERROR_NOROUTETOHOST);
		return false;
	}
	// Next, try to find a route
	outPort = Lookup(GetTuple(p, header));
   	Ptr<NetDevice> dev = m_ipv4->GetNetDevice(outPort); // Convert output port to device
   	Ptr<Channel> channel = dev->GetChannel(); // Channel used by the device
	uint32_t otherEnd = (channel->GetDevice(0)==dev)?1:0; // Which end of the channel?
	Ptr<Node> nextHop = channel->GetDevice(otherEnd)->GetNode(); // Node at other end
   	uint32_t nextIf = channel->GetDevice(otherEnd)->GetIfIndex(); // Iface num at other end
	Ipv4Address nextHopAddr = nextHop->GetObject<Ipv4>()->GetAddress(nextIf,0).GetLocal(); // Addr of other end
	Ptr<Ipv4Route> r = Create<Ipv4Route> ();
	r->SetOutputDevice(m_ipv4->GetNetDevice(outPort));
	r->SetGateway(nextHopAddr);
	r->SetSource(m_ipv4->GetAddress(outPort,0).GetLocal());
	r->SetDestination(a);
	NS_LOG_LOGIC ("Found unicast destination- calling unicast callback");
	ucb(r, p, header);
	return true;
}

bool
HashRouting::IsLocal (const Ipv4Address& dest)
{
	if (dest.IsBroadcast()) {
		NS_LOG_LOGIC (dest <<" is broadcast address");
		return true;
	};
	for (uint32_t j = 0; j < m_ipv4->GetNInterfaces (); j++) {
		for (uint32_t i = 0; i < m_ipv4->GetNAddresses (j); i++) {
			Ipv4Address addr = m_ipv4->GetAddress (j, i).GetLocal();
			if (addr.IsEqual (dest)) {
				NS_LOG_LOGIC (addr <<" is local to iface "<< j <<" addr "<< i);
				return true;
			}
		}
	}
	NS_LOG_LOGIC ("Address "<< dest << " is not local");
	return false;
}

void 
HashRouting::SetIpv4 (Ptr<Ipv4> ipv4)
{
	NS_LOG_FUNCTION(this << ipv4);
	NS_ASSERT (m_ipv4 == 0 && ipv4 != 0);
	m_ipv4 = ipv4;
}

uint32_t
HashRouting::Hash(const flowid& tuple) const
{
	return (*m_hash)(m_ipv4->GetAddress(1,0).GetLocal().Get(), tuple);
};

bool
HashRouting::IsEdge(const Ipv4Address& addr) const
{
        uint32_t a = addr.Get();
	return (((a & 0x00010000)==0) && ((a & 0x00000300) == 0x00000200));
}

void
HashRouting::DoDispose (void)
{
	m_ipv4 = 0;
	while (!m_congRecord.empty()) {
		m_congRecord.pop_back();
	};
	while (!m_destRouteTable.empty()) {
		m_destRouteTable.pop_back();
	};
	while (!m_flowRouteTable.empty()) {
		m_flowRouteTable.pop_back();
	};
	Ipv4RoutingProtocol::DoDispose ();
};

bool
HashRouting::RequestDestRoute(const Ipv4Address& addr, uint32_t& outPort)
{
	NS_LOG_LOGIC("Dest IP to route: "<< std::hex << addr << std::dec);
	// Linear search for matching entry
	for(DestRouteTable::iterator it = m_destRouteTable.begin(); it != m_destRouteTable.end(); it++) {
		NS_LOG_LOGIC("Route in table: "<< std::hex << (*it)->dest << "/" << (*it)->mask << std::dec);
		if((*it)->mask.IsMatch(addr, (*it)->dest)) {
			NS_LOG_LOGIC("Route matched");
			outPort = (*it)->outPort;
			return true;
		};
	};
	return false;
};

bool
HashRouting::RequestFlowRoute(const flowid& tuple, uint32_t& outPort)
{
	NS_LOG_FUNCTION(this);
	// Linear search for matching entry
	FlowRouteTable::iterator it = m_flowRouteTable.begin();
	while (it != m_flowRouteTable.end()) {
		if ((*it)->last + m_lifetime < Simulator::Now()) {
			// Erase expired entry
			it = m_flowRouteTable.erase(it);
			continue;
		};
		if (tuple == (*it)->fid) {
			// Entry found: Update timestamp and return
			outPort = (*it)->outPort;
			(*it)->last = Simulator::Now();
			return true;
		};
		it++;
	};
	return false;
}

bool
HashRouting::NeedReroute(const flowid& fid)
{
	// Linear search the congestion record table
	CongRecordTable::iterator i = m_congRecord.begin();
	while (i != m_congRecord.end()) {
		if ((*i)->last + m_lifetime < Simulator::Now()) {
			// Erase expired entry
			i = m_congRecord.erase(i);
			continue;
		};
		if ((*i)->fid == fid) {
			// If a record is found increase the count and check if
			// threshold is met
			(*i)->count++;
			(*i)->last = Simulator::Now();
			NS_LOG_LOGIC("Flow "<< fid <<" set with count "<< (*i)->count <<", thresh="<< m_rrThresh);
			if ((*i)->count > m_rrThresh) {
				(*i)->count = 0;
				return true;
			} else {
				return false;
			};
		};
		i++;
	};
	NS_LOG_LOGIC("Flow "<< fid <<" not found. Create new record.");
	// The current flow is not on the congestion record table, add to it
	Ptr<CongRecord> rec = Create<CongRecord>(fid, Simulator::Now(), 1);
	m_congRecord.push_back(rec);
	return false;
}

uint32_t
HashRouting::Reroute(const flowid& fid, uint32_t oldPort)
{
	// Compute a new port
	uint16_t newPort;
	uint16_t numDownPorts = (m_ipv4->GetNInterfaces()-1)/2;
	do {
		newPort = 1 + static_cast<uint16_t>(UniformVariable(0,numDownPorts).GetValue());
		if (oldPort > numDownPorts) {
			newPort += numDownPorts;
		};
	} while (newPort == oldPort);

	// Linear search for matching entry in m_flowRouteTable
	FlowRouteTable::iterator it = m_flowRouteTable.begin();
	while (it != m_flowRouteTable.end()) {
		if ((*it)->last + m_lifetime < Simulator::Now()) {
			// Erase expired entry
			it = m_flowRouteTable.erase(it);
			continue;
		};
		if (fid == (*it)->fid) {
			// Entry found: Change output port
			(*it)->outPort = newPort;
			return newPort;
		};
		it++;
	};
	// Linear search failed, the flow is not in the flow table, create new
	Ptr<FlowRoute> f = Create<FlowRoute>(fid, Simulator::Now(), newPort);
	m_flowRouteTable.push_back(f);
	return newPort;
};

}//namespace ns3
