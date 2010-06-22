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

#include "ns3/abort.h"
#include "ns3/log.h"
#include "ns3/object.h"
#include "ns3/packet.h"
#include "ns3/net-device.h"
#include "ns3/qbb-net-device.h"
#include "ns3/ipv4-route.h"
#include "ns3/ipv4-routing-table-entry.h"
#include "spain-routing.h"
#include "ns3/boolean.h"
#include "ns3/uinteger.h"
#include "ns3/tcp-header.h"
#include "ns3/udp-header.h"
#include "ns3/cn-header.h"
#include "ns3/channel.h"
#include "ns3/node.h"
#include "ns3/random-variable.h"

NS_LOG_COMPONENT_DEFINE ("SpainRouting");

namespace ns3 {

NS_OBJECT_ENSURE_REGISTERED (SpainRouting);

TypeId 
SpainRouting::GetTypeId (void)
{ 
  static TypeId tid = TypeId ("ns3::SpainRouting")
    .SetParent<Ipv4RoutingProtocol> ()
    .AddAttribute ("RerouteScheme",
                   "Reroute scheme to use: 0=no reroute, 1=random, 2=best, 3=biased random",
                   UintegerValue(1),
                   MakeUintegerAccessor (&SpainRouting::m_RR),
                   MakeUintegerChecker<uint32_t> ())
    .AddAttribute ("RerouteThreshold",
                   "Number of congestion signal to be seen before reroute triggered",
                   UintegerValue (2),
                   MakeUintegerAccessor (&SpainRouting::m_rrThresh),
                   MakeUintegerChecker<uint32_t> ())
    .AddAttribute ("CnLifetime",
                   "Lifetime for a congestion signal record",
                   TimeValue (Seconds (0.1)),
                   MakeTimeAccessor (&SpainRouting::m_lifetime),
                   MakeTimeChecker ())
    .AddAttribute ("RouteFreezeTime",
                   "Time to freeze a route after a reroute to prevent too frequent rerouting",
                   TimeValue (Seconds (0)),
                   MakeTimeAccessor (&SpainRouting::m_freeze),
                   MakeTimeChecker ())
    ;
  return tid;
}

SpainRouting::SpainRouting () 
{
  NS_LOG_FUNCTION_NOARGS ();
}

SpainRouting::~SpainRouting ()
{
  NS_LOG_FUNCTION_NOARGS ();
}

void 
SpainRouting::SetIpv4 (Ptr<Ipv4> ipv4)
{
	NS_LOG_FUNCTION(this << ipv4);
	NS_ASSERT (m_ipv4 == 0 && ipv4 != 0);
	m_ipv4 = ipv4;
}

Ptr<Ipv4Route>
SpainRouting::RouteOutput (Ptr<Packet> p, Ipv4Header &header, Ptr<NetDevice> oif, Socket::SocketErrno &sockerr)
{
	NS_LOG_FUNCTION (this << p << header << header.GetSource () << header.GetDestination () << oif);
	// Hash-routing is for unicast destination only
	Ipv4Address a = header.GetDestination();
	if (a.IsMulticast() || a.IsBroadcast()) {
		NS_LOG_LOGIC("Non-unicast destination is not supported");
		sockerr = Socket::ERROR_NOROUTETOHOST;
		return 0;
	};
	// Set the VLAN number into TOS field of IPv4 header
	if (header.GetTos() == 255) {
		flowid fid = GetTuple(p,header);
		uint8_t vlan = GetVlan(fid);
		header.SetTos(vlan);
	};
	// Check for a route, and construct the Ipv4Route object
	sockerr = Socket::ERROR_NOTERROR;
	uint32_t port = GetRoute(a.Get(), header.GetTos());
	Ptr<NetDevice> dev = m_ipv4->GetNetDevice(port); // Convert output port to device
	Ptr<Channel> channel = dev->GetChannel(); // Channel used by the device
	uint32_t otherEnd = (channel->GetDevice(0)==dev)?1:0; // Which end of the channel?
	Ptr<Node> nextHop = channel->GetDevice(otherEnd)->GetNode(); // Node at other end
	uint32_t nextIf = channel->GetDevice(otherEnd)->GetIfIndex(); // Iface num at other end
	Ipv4Address nextHopAddr = nextHop->GetObject<Ipv4>()->GetAddress(nextIf,0).GetLocal(); // Addr of other end
	Ptr<Ipv4Route> r = Create<Ipv4Route> ();
	r->SetOutputDevice(dev);
	r->SetGateway(nextHopAddr);
	r->SetSource(m_ipv4->GetAddress(port,0).GetLocal());
	r->SetDestination(a);
	return r;
}

bool 
SpainRouting::RouteInput (Ptr<const Packet> p, const Ipv4Header &header, Ptr<const NetDevice> idev,
		UnicastForwardCallback ucb, MulticastForwardCallback mcb,
		LocalDeliverCallback lcb, ErrorCallback ecb) 
{ 
	NS_LOG_FUNCTION (this << p << header << header.GetSource () << header.GetDestination () << idev);
	// Check if input device supports IP
	NS_ASSERT (m_ipv4->GetInterfaceForDevice (idev) >= 0);
	uint32_t iif = m_ipv4->GetInterfaceForDevice (idev);
	Ipv4Address a = header.GetDestination();

	// Congestion signal processing
	if (header.GetProtocol() == 0xFF && IsLocal(a)) {
		NS_LOG_LOGIC("CN to "<< a <<" at host "<< m_ipv4->GetAddress(1,0).GetLocal());
		// We are routing a congestion control signal at an edge switch
		CnHeader cnh;
		p->PeekHeader(cnh);
		flowid tuple = cnh.GetFlow();
		uint8_t vlan = header.GetTos();
		// Then check if we need to do rerouting
		if (m_RR && NeedReroute(tuple, header.GetSource().Get(), vlan)) {
			// If the flow needs reroute, then do the reroute and return
			uint8_t newvlan = 0;
			newvlan = Reroute(tuple, vlan);
			NS_LOG_INFO("Rerouted "<< tuple <<" from "<< vlan <<" to "<< newvlan);
		};
		NS_LOG_LOGIC("CN for "<<tuple<<" recorded");
		return false;
	};

	// Hash-routing is for unicast destination only
	if (a.IsMulticast() || a.IsBroadcast()) {
		NS_LOG_LOGIC("Non-unicast destination is not supported");
		return false;
	};

	// Check if the destination is local
	if (IsLocal(a)) {
		NS_LOG_LOGIC ("local destination- calling local callback");
		lcb (p, header, iif);
		return true;
	};
	// Check if input device supports IP forwarding
	if (m_ipv4->IsForwarding (iif) == false) {
		NS_LOG_LOGIC ("Forwarding disabled for this interface");
		ecb (p, header, Socket::ERROR_NOROUTETOHOST);
		return false;
	}
	// Next, try to find a route
	uint32_t outPort = GetRoute(a.Get(), header.GetTos());
   	Ptr<NetDevice> dev = m_ipv4->GetNetDevice(outPort); // Convert output port to device
   	Ptr<Channel> channel = dev->GetChannel(); // Channel used by the device
	uint32_t otherEnd = (channel->GetDevice(0)==dev)?1:0; // Which end of the channel?
	Ptr<Node> nextHop = channel->GetDevice(otherEnd)->GetNode(); // Node at other end
   	uint32_t nextIf = channel->GetDevice(otherEnd)->GetIfIndex(); // Iface num at other end
	Ipv4Address nextHopAddr = nextHop->GetObject<Ipv4>()->GetAddress(nextIf,0).GetLocal(); // Addr of other end
	Ptr<Ipv4Route> r = Create<Ipv4Route> ();
	r->SetOutputDevice(dev);
	r->SetGateway(nextHopAddr);
	r->SetSource(m_ipv4->GetAddress(outPort,0).GetLocal());
	r->SetDestination(a);
	NS_LOG_LOGIC ("Found unicast destination- calling unicast callback");
	ucb(r, p, header);
	return true;
}

/* Get the VLAN number for an outgoing flow */
uint8_t
SpainRouting::GetVlan(flowid fid)
{
	// Check flow table if a VLAN number is fixed
	SpainFlowTable::iterator it = m_flowTable.begin();
	while (it != m_flowTable.end()) {
		// Erase expired entry
		if ((*it)->last + m_lifetime < Simulator::Now()) {
			it = m_flowTable.erase(it);
			continue;
		};
		// Return VLAN number if flow is found
		if (fid == (*it)->fid) {
			(*it)->last = Simulator::Now();
			return (*it)->vlan;
		};
		it++;
	};
	// If flow not in flow table, make a random number by hashing flowid
	uint32_t addr = fid.GetDAddr();
	uint32_t option = Hash(fid) % m_fib.count(addr);
	SpainRoutingTable::const_iterator i = m_fib.equal_range(addr).first;
	while (option) { option--; i++; };
	uint8_t vlan = (*i).second.vlan;
	NS_LOG_LOGIC("Packet of "<< fid <<" assigned VLAN "<< (uint32_t)vlan);
	return vlan;
};

/* Retrieve the output port according to the routing table */
uint32_t
SpainRouting::GetRoute(uint32_t addr, uint8_t vlan)
{
	RouteEntries r = m_fib.equal_range(addr);
	for (SpainRoutingTable::const_iterator i = r.first; i != r.second; ++i) {
		if ((*i).second.vlan == vlan) {
			return (*i).second.port;
		};
	};
	NS_ABORT_MSG("Route failed on address " << std::hex << addr << std::dec << " VLAN " << (uint16_t) vlan << " at node " << std::hex << m_ipv4->GetAddress (1, 0).GetLocal().Get() << std::dec);
	return 0xFFFFFFFF;
};

/* Extract the five tuples from L3 and L4 headers */
flowid
SpainRouting::GetTuple(Ptr<const Packet> packet, const Ipv4Header& header)
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

/* Add a route into the routing table */
void
SpainRouting::AddRoute (uint32_t dest, uint8_t vlan, uint32_t interface)
{
	m_fib.insert(std::pair<uint32_t,VlanPort>(dest, VlanPort(vlan,interface)));
	NS_LOG_LOGIC("New route for iface "<<interface<<": "<<std::hex<<dest<<std::dec<<"/VLAN "<<(uint32_t)vlan);
};

/* Tell if the specified address is local */
bool
SpainRouting::IsLocal (const Ipv4Address& dest)
{
	if (dest.IsBroadcast()) {
		NS_LOG_LOGIC (dest <<" is broadcast address");
		return true;
	};
	uint32_t destAddr = dest.Get();
	if (localAddrCache.size() == 0) {
		for (uint32_t j = 0; j < m_ipv4->GetNInterfaces (); j++) {
			for (uint32_t i = 0; i < m_ipv4->GetNAddresses (j); i++) {
				localAddrCache.insert( m_ipv4->GetAddress (j, i).GetLocal().Get() );
			}
		}
	};
	if (localAddrCache.find(destAddr) != localAddrCache.end()) {
		NS_LOG_LOGIC ("Address "<< dest << " is local");
		return true;
	};
	NS_LOG_LOGIC ("Address "<< dest << " is not local");
	return false;
}

/* Return the hash value of the specified flowid according to m_hash */
uint32_t
SpainRouting::Hash(const flowid& tuple) const
{
	return (*m_hash)(m_ipv4->GetAddress(1,0).GetLocal().Get(), tuple);
};

/* Clean up function */
void
SpainRouting::DoDispose (void)
{
	m_ipv4 = 0;
	if (!m_congRecord.empty()) {
		m_congRecord.clear();
	};
	if (!m_fib.empty()) {
		m_fib.clear();
	};
	if (!m_flowTable.empty()) {
		m_flowTable.clear();
	};
	Ipv4RoutingProtocol::DoDispose ();
};

/* Tell if we need to reroute a flow upon receipt of its CN */
bool
SpainRouting::NeedReroute(const flowid& fid, uint32_t cp, uint8_t vlan)
{
	// Linear search the congestion record table
	CongRecordTable::iterator i = m_congRecord.begin();
	while (i != m_congRecord.end()) {
		if ((*i)->cn.front()->time + m_lifetime < Simulator::Now()) {
			// Erase expired entry
			i = m_congRecord.erase(i);
			continue;
		};
		if ((*i)->fid == fid) {
			// If a record is found, insert the CP into the record and erase expired entries.
			// Then check if threshold is met.
			if (vlan == GetVlan(fid)) {
				(*i)->cn.push_front(Create<SpainCnRec>(cp, vlan));
			};
			while((*i)->cn.back()->time + m_lifetime < Simulator::Now()) {
				(*i)->cn.pop_back();
				if ((*i)->zero > 0) { --(*i)->zero; };
			};
			NS_LOG_INFO("Flow "<< fid <<" has "<< (*i)->cn.size() <<" CNs, thresh="<< m_rrThresh << ", CP=" << std::hex << cp << std::dec);
			if ((*i)->cn.size() >= m_rrThresh + (*i)->zero) {
				// Next reroute triggered at (*i)->cn.size() + m_rrThresh
				(*i)->zero = (*i)->cn.size();
				return true;
			} else {
				return false;
			};
		};
		i++;
	};
	NS_LOG_INFO("Flow "<< fid <<" not found. Create new record. CP=" << std::hex << cp << std::dec);
	// The current flow is not on the congestion record table, add to it
	Ptr<SpainCongRecord> rec = Create<SpainCongRecord>(fid);
	rec->cn.push_front(Create<SpainCnRec>(cp, vlan));
	m_congRecord.push_back(rec);
	return false;
}

/* Compute the new VLAN upon to which to reroute */
uint8_t
SpainRouting::DoReroute(const flowid& fid, uint8_t vlan)
{
	const unsigned N = m_fib.count(fid.GetDAddr());
	std::map<uint8_t,std::set<uint32_t> > cp;
	std::vector<double> problist;
	// Short cut: If N == 1, no alternative available
	if (N == 1) return vlan;
	// Collect information from the congestion record table
	CongRecordTable::iterator i = m_congRecord.begin();
	while (i != m_congRecord.end()) {
		// Kill all expired record
		if ((*i)->cn.front()->time + m_lifetime < Simulator::Now()) {
			i = m_congRecord.erase(i);
			continue;
		};
		while((*i)->cn.back()->time + m_lifetime < Simulator::Now()) {
			(*i)->cn.pop_back();
			if ((*i)->zero > 0) { --(*i)->zero; };
		};
		// Honours only the information of the same priority
		if ((QbbNetDevice::Hash((*i)->fid) - QbbNetDevice::Hash(fid)) % QbbNetDevice::qCnt == 0) {
			// Count the CPs for each VLAN
			for (std::list<Ptr<SpainCnRec> >::iterator j = (*i)->cn.begin(); j != (*i)->cn.end(); j++) {
				cp[(*j)->vlan].insert((*j)->cp);
			};
		};
		// Check next record
		++i;
	};
	// Convert the CP information into likelihood metric, computed as
	// 1/(1+c) where c is the count of CNs in a VLAN.
	std::map<uint8_t, double> metric;	// VLAN -> Metric
	for (std::map<uint8_t,std::set<uint32_t> >::iterator it = cp.begin(); it != cp.end(); ++it) {
		double m = 1.0/(1+(*it).second.size());
		metric[(*it).first] = m;
	};
	// Find the set of applicable VLANs, i.e. those that can reach the destination
	std::set<uint8_t> vlans;
	RouteEntries r = m_fib.equal_range(fid.GetDAddr());
	double metricsum = 0;
	uint8_t maxmetric = r.first->second.vlan;
	for (SpainRoutingTable::const_iterator i = r.first; i != r.second; ++i) {
		uint8_t v = i->second.vlan;
		vlans.insert(v);
		if (v == vlan) {	// Enforce a new VLAN to be chosen
			metric[v] = 0;
		} else if (metric.count(v) == 0) {
			metric[v] = 1;
		};
		metricsum += metric[v];
		if (metric[v] > metric[maxmetric]) maxmetric = v;
	};
	// Find the new VLAN based on different method
	if (m_RR == 3) {
		// Method: Weighted random of likelihood
		double p = UniformVariable(0,1).GetValue();
		std::set<uint8_t>::iterator i = vlans.begin();
		uint8_t newvlan = 0;
		while (p > 0) {
			newvlan = *i;
			p -= metric[*i]/metricsum;
			if (++i == vlans.end()) break;
		};
		return newvlan;
	} else if (m_RR == 2) {
		// Method: The maximum likelihood of no congestion
		return maxmetric;
	} else if (m_RR == 1) {
		// Method: Uniform random
		uint8_t n = UniformVariable(0,N).GetValue();
		std::set<uint8_t>::iterator i = vlans.begin();
		while (n != 0) { n--; i++; };
		return *i;
	} else {
		// No reroute, always return the old VLAN number
		return vlan;
	};
};

/* Reroute a flow to a new VLAN */
uint8_t
SpainRouting::Reroute(const flowid& fid, uint8_t oldVlan)
{
	// Compute a new port
	uint8_t newVlan = DoReroute(fid, oldVlan);

	// Linear search for matching entry in m_flowTable
	SpainFlowTable::iterator it = m_flowTable.begin();
	while (it != m_flowTable.end()) {
		// Erase expired entry
		if ((*it)->last + m_lifetime < Simulator::Now()) {
			it = m_flowTable.erase(it);
			continue;
		};
		// Change the VLAN number if flow is found
		if (fid == (*it)->fid) {
			if ((*it)->lastreroute + m_freeze >= Simulator::Now()) { return oldVlan; };
			NS_LOG_INFO("Reroute flow " << fid << " from VLAN " << oldVlan << " to " << newVlan);
			(*it)->vlan = newVlan;
			(*it)->lastreroute = Simulator::Now();
			return newVlan;
		};
		it++;
	};
	// Linear search failed, the flow is not in the flow table, create new
	Ptr<SpainFlowRoute> f = Create<SpainFlowRoute>(fid, newVlan);
	m_flowTable.push_back(f);
	NS_LOG_INFO("Reroute flow " << fid << " from VLAN " << oldVlan << " to " << newVlan);
	return newVlan;
};

}//namespace ns3
