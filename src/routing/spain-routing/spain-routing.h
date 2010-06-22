// -*- Mode: C++; c-file-style: "gnu"; indent-tabs-mode:nil; -*-
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
//

#ifndef SPAIN_ROUTING_H
#define SPAIN_ROUTING_H

#include <list>
#include <set>
#include <map>
#include <stdint.h>
#include "ns3/ipv4-address.h"
#include "ns3/ptr.h"
#include "ns3/ipv4.h"
#include "ns3/simulator.h"
#include "ns3/ipv4-routing-protocol.h"
#include "ns3/ref-count-base.h"
#include "ns3/fivetuple.h"
#include "ns3/hash-function.h"

namespace ns3 {

class Packet;
class NetDevice;
class Ipv4Interface;
class Ipv4Address;
class Ipv4Header;
class Ipv4RoutingTableEntry;
class Ipv4MulticastRoutingTableEntry;
class Node;

// Output port and VLAN Number
class VlanPort
{
public:
	VlanPort(uint8_t v, uint32_t p) : vlan(v), port(p) {};
	uint8_t vlan;
	uint32_t port;
};

// Flow-based routing table indexed by five-tuple
class SpainFlowRoute : public RefCountBase
{
public:
	SpainFlowRoute(const flowid& f, uint8_t v) : fid(f), last(Simulator::Now()), lastreroute(Simulator::Now()), vlan(v) {};
	flowid fid;
	Time last;
	Time lastreroute;
	uint8_t vlan;
};

// Record for a CN packet
class SpainCnRec : public RefCountBase
{
public:
	SpainCnRec(uint32_t cp_, uint8_t v_) : cp(cp_), vlan(v_), time(Simulator::Now()) {};
	uint32_t cp;	// Congestion point address
	uint8_t vlan;	// VLAN number
	Time time;	// Time of receipt
};

// Congestion signal record for a flow
class SpainCongRecord : public RefCountBase
{
public:
	SpainCongRecord(const flowid& f) : fid(f), zero(0) {};
	flowid fid;	// Flow ID
	uint32_t zero;	// The "zero" position in computing reroute threshold
	std::list<Ptr<SpainCnRec> > cn;	// List of all CNs
};

// Class for hash-based routing logic
class SpainRouting : public Ipv4RoutingProtocol
{
	typedef std::multimap<uint32_t, VlanPort> SpainRoutingTable;
	typedef std::pair<SpainRoutingTable::const_iterator, SpainRoutingTable::const_iterator> RouteEntries;
	typedef std::list<Ptr<SpainFlowRoute> > SpainFlowTable;
	typedef std::list<Ptr<SpainCongRecord> > CongRecordTable;
public:
	static TypeId GetTypeId (void);
	SpainRouting ();
	virtual ~SpainRouting ();

	// Functions defined in Ipv4RoutingProtocol
	virtual Ptr<Ipv4Route> RouteOutput (Ptr<Packet> p,
			Ipv4Header &header,
			Ptr<NetDevice> oif, Socket::SocketErrno &sockerr);
	virtual bool RouteInput  (Ptr<const Packet> p,
			const Ipv4Header &header, Ptr<const NetDevice> idev,
			UnicastForwardCallback ucb, MulticastForwardCallback mcb,
			LocalDeliverCallback lcb, ErrorCallback ecb);
	virtual void NotifyInterfaceUp (uint32_t interface) {};
	virtual void NotifyInterfaceDown (uint32_t interface) {};
	virtual void NotifyAddAddress (uint32_t interface, Ipv4InterfaceAddress address) {};
	virtual void NotifyRemoveAddress (uint32_t interface, Ipv4InterfaceAddress address) {};
	virtual void SetIpv4 (Ptr<Ipv4> ipv4);

	/**
	 * \brief Add a route to a destination into the routing table.
	 *
	 * \param dest The IPv4 address of the destination
	 * \param vlan The VLAN number
	 * \param interface The network interface index used to send packets to the
	 * destination.
	 */
	void AddRoute (uint32_t dest, uint8_t vlan, uint32_t interface);

	/**
	 * \brief Set the hash function to be used in the hash-based routing
	 *
	 * \param hash The pointer to a hash function object
	 */
  	void SetHashFunction (Ptr<HashFunction> hash) { m_hash = hash; };
protected:
	/**
	 * \brief Return the VLAN number that this flow should use
	 *
	 * \param fid The flow id in five tuples
	 * \return VLAN number
	 */
	uint8_t GetVlan(flowid fid);

	/**
	 * \brief Retrieve the output port according to the routing table
	 *
	 * \param addr The IPv4 address in uint32_t format
	 * \param vlan The VLAN number
	 * \return output port number
	 */
	uint32_t GetRoute(uint32_t addr, uint8_t vlan);

	/**
	 * Extract the five tuples from L3 and L4 headers
	 */
	flowid GetTuple(Ptr<const Packet> packet, const Ipv4Header& header);

	/**
	 * Tell if the specified address is local
	 */
	bool IsLocal (const Ipv4Address& dest);

	/*
	 * Given the flow Id, return a 32-but hash value
	 *
	 * \param tuple	The flow id as five tuple
	 * \return 32-bit hash value specific to this incarnation of routing module
	 */
	uint32_t Hash(const flowid& tuple) const;

	/*
	 * Check if rerouting shall be triggered for a flow
	 *
	 * \param fid	The flow id as five tuple
	 * \param cp    The IP address of the congestion point
	 * \param vlan  The VLAN number of the cp
	 * \return true if the flow shall be rerouted, false otherwise
	 */
	bool NeedReroute(const flowid& fid, uint32_t cp, uint8_t vlan);

	/*
	 * Reroute a flow by adding/modifying an entry in the flow table
	 *
	 * \param fid	The flow id as five tuple
	 * \param oldVlan Original VLAN number in use
	 * \return New VLAN number to use
	 */
	uint8_t Reroute(const flowid& fid, uint8_t oldVlan);

	/* The function doing the real reroute logic to pick a new VLAN number
	 */
	uint8_t DoReroute(const flowid& fid, uint8_t vlan);

	/*
	 * Clean up everything to make this object virtually dead
	 */
  	virtual void DoDispose (void);
protected:
	Ptr<HashFunction> m_hash;

	SpainRoutingTable m_fib;
	SpainFlowTable m_flowTable;
	CongRecordTable m_congRecord;

	std::set<uint32_t> localAddrCache;
  
	Ptr<Ipv4> m_ipv4;	// Hook to the Ipv4 object of this node
	uint32_t m_RR;		// Reroute scheme to use
	uint32_t m_rrThresh;	// CN threshold for reroute
	Time m_lifetime;	// Lifetime of a CN record
	Time m_freeze;		// Freeze time of a flow to prevent frequent rerouting
};

} // Namespace ns3

#endif /* HASH_ROUTING_H */
