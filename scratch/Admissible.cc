/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
* Copyright (c) 2009 New York University
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
* Author: Adrian S. Tam <adrian.sw.tam@gmail.com>
*/

#include <iostream>
#include <iomanip>
#include <fstream>
#include <assert.h>
#include "ns3/core-module.h"
#include "ns3/simulator-module.h"
#include "ns3/node-module.h"
#include "ns3/helper-module.h"

using namespace ns3;

NS_LOG_COMPONENT_DEFINE ("SimulationScript");

const char outputfile[] = "Admissible.tr";
const uint16_t port = 9;   // Discard port (RFC 863)

std::vector<ApplicationContainer> apps(54);

int main (int argc, char *argv[])
{
	// Turn on logging
//	LogComponentEnable("SimulationScript", LOG_LEVEL_ALL);
	LogComponentEnableAll(LOG_PREFIX_TIME);
	LogComponentEnableAll(LOG_PREFIX_FUNC);
//	LogComponentPrintList();

	uint32_t bc = 50e3;
	double tcp=0;
	bool rr=1;
	double linkBw = 100e6;		// Link bandwidth in bps
	double linkDelay = 5e-9;	// Link delay in seconds (5ns = 1m wire)
	unsigned size = 3;		// Fat tree size
	double percent = 0.8;		// Percent of bandwidth to use per sending host
	uint64_t bytes = 0;		// Number of bytes to send per flow
	int maxflow = 10;		// Maximum number of flows per node
	int pausetime = 25;		// Pause duration in us
	bool dryrun=0;			// Fake the simulation or not
	bool cbr=0;			// Use CBR traffic?
	uint32_t speedup = 1;		// Speedup factor (for 802.1Qau)
	unsigned stoptime = 0;		// Time to stop applications

	CommandLine cmd;
	cmd.AddValue("speedup","Speed up factor of 802.1Qau",speedup);
	cmd.AddValue("bc","BC value of RP device",bc);
	cmd.AddValue("tcp","Percentage of TCP traffic (1 to 0)",tcp);
	cmd.AddValue("cbr","Use CBR traffic gen (1 or 0)",cbr);
	cmd.AddValue("rr","Enable reroute (1 or 0)",rr);
	cmd.AddValue("bw","Link bandwidth",linkBw);
	cmd.AddValue("delay","Link delay",linkDelay);
	cmd.AddValue("dryrun","Fake the simulation",dryrun);
	cmd.AddValue("size","Fat tree size",size);
	cmd.AddValue("bytes","Number of bytes to send per flow",bytes);
	cmd.AddValue("pc","Percentage of bandwidth to use per sending host",percent);
	cmd.AddValue("maxflow","Maximum number of flows per node",maxflow);
	cmd.AddValue("pt","Pause duration in microseconds",pausetime);
	cmd.AddValue("stop","Time to stop the flows", stoptime);
	cmd.Parse (argc, argv);

	Config::SetDefault ("ns3::TcpSocket::SegmentSize", UintegerValue(1000));
	Config::SetDefault ("ns3::RpNetDevice::BC", UintegerValue(bc));
	Config::SetDefault ("ns3::QbbNetDevice::PauseTime", UintegerValue(pausetime));
	Config::SetDefault ("ns3::QbbNetDevice::BufferSize", UintegerValue(131072));	// 128KiB
	Config::SetDefault ("ns3::RpNetDevice::MinRate", DataRateValue(DataRate("1Mbps")));
	Config::SetDefault ("ns3::CpNetDevice::SpeedUp", UintegerValue(speedup));
	Config::SetDefault ("ns3::HashRouting::IntelReroute", BooleanValue(false));
	Config::SetDefault ("ns3::HashRouting::EnableReroute", BooleanValue(rr != 0));

	// Build the fat tree network
	Ptr<FatTreeHelper> fattree = CreateObject<FatTreeHelper>(size);
	fattree->SetAttribute("HeDataRate", DataRateValue(DataRate(linkBw)));
	fattree->SetAttribute("EaDataRate", DataRateValue(DataRate(linkBw)));
	fattree->SetAttribute("AcDataRate", DataRateValue(DataRate(linkBw)));
	fattree->SetAttribute("HeDelay", TimeValue(Seconds(linkDelay)));
	fattree->SetAttribute("EaDelay", TimeValue(Seconds(linkDelay)));
	fattree->SetAttribute("AcDelay", TimeValue(Seconds(linkDelay)));
	fattree->Create();

	// Prepare parameters for MMPP traffic generator
	Ptr<GenMatrix>  generator = CreateObject<GenMatrix>();
	RcVector<double> temp;
	double tempArray[3]={-1,0.5,0.5};

	for(uint16_t i = 0 ; i<3 ; i ++) {
		temp.clear();
		for(uint16_t j = 0 ; j <3 ;j++) {
			temp.push_back(tempArray[(3+j-i)%3]);
		};
		generator->push_back(temp);
	};

	Ptr<SizeVector> pktsizes = CreateObject<SizeVector>();
	pktsizes->push_back(1000);
	pktsizes->push_back(1000);
	pktsizes->push_back(1000);

	// Get a list of source addresses
	std::vector<Ipv4Address> addrs;	// Host addresses
	const unsigned numHosts = size*size*size*2;
	Ipv4InterfaceContainer hostIfs = fattree->HostInterfaces();
	for(unsigned i=0; i<numHosts; i++) {
		addrs.push_back(hostIfs.GetAddress(i));
	};
	NS_ASSERT_MSG(addrs.size() == numHosts,
		"Number of hosts mismatch the size of fat tree.");
	std::list<uint64_t> partition;			//< A partition of link bandwidth, for building flow sizes
	std::list<uint64_t> flowsizes[numHosts];	//< Flow sizes at each sender
	std::list<unsigned> flowdests[numHosts];	//< Flow destinations at each sender
	uint64_t util[numHosts];			//< The bandwidth utilization at each destination

	NS_LOG_INFO ("Create Application.");
	// Set up preliminary source-destination flow relationships
	for(unsigned src=0; src<numHosts; src++) {
		// Partition bandwidth into random number of flows
		util[src]=0;
		for (int flownum = UniformVariable(0,maxflow).GetValue() + 1; flownum > 1; flownum--) {
			partition.push_back(UniformVariable(0,uint64_t(linkBw*percent)).GetValue());
		};
		partition.sort();
		partition.push_back(static_cast<uint64_t>(linkBw*percent));
		uint64_t first = 0;
		uint64_t second;	// Flow size = second - first
		while (!partition.empty()) {
			// Calculate flow size
			second = partition.front();
			partition.pop_front();
			if (second == first) { continue; };	// Ignore empty flow
			flowsizes[src].push_back(second - first);
			first = second;
			// Find destination
			unsigned dest = unsigned(UniformVariable(0, addrs.size()-1).GetValue());
			if (dest >= src) dest++;
			flowdests[src].push_back(dest);
		};
		NS_LOG_INFO("Temporarily assigned "<< flowsizes[src].size() << " flows from " << addrs[src]);
	};
	// Normalize the flows to make the traffic admissible
	for(unsigned src=0; src<numHosts; src++) {
		std::list<uint64_t>::iterator sizeIt = flowsizes[src].begin();
		std::list<unsigned>::iterator destIt = flowdests[src].begin();
		while (sizeIt != flowsizes[src].end()) {
			if (util[*destIt] + *sizeIt <= linkBw) {
				util[*destIt] += *sizeIt;
				++sizeIt;
				++destIt;
			} else {
				// Partition flow size into two
				uint64_t oldSize = *sizeIt;
				uint64_t newSize1 = linkBw - util[*destIt];
				uint64_t newSize2 = oldSize - newSize1;
				// Confirm the first flow (newSize1)
				util[*destIt] += newSize1;
				NS_ASSERT(util[*destIt]==linkBw);
				// Update the flow size information
				if (newSize1 != 0) {
					sizeIt = flowsizes[src].erase(sizeIt);
					flowsizes[src].insert(sizeIt,newSize1);
					flowsizes[src].insert(sizeIt,newSize2);
					--sizeIt;
				};
				// Update the flow destination list
				unsigned newDest = 0;
				while (util[newDest] == linkBw) newDest++;
				if (newSize1 == 0) {
					destIt = flowdests[src].erase(destIt);
				} else {
					++destIt;
				};
				flowdests[src].insert(destIt,newDest);
				--destIt;
			};
		};
		NS_LOG_INFO("There will be "<< flowsizes[src].size() << " flows from " << addrs[src]);
	};
	// Verify the normalization is correct
	for(unsigned dest=0; dest<numHosts; dest++) {
		NS_ASSERT_MSG(util[dest] <= linkBw, "Destination node "<< dest <<" exceeded");
		NS_ASSERT_MSG(flowsizes[dest].size() == flowdests[dest].size(), "Data for flows of node "<< dest <<" mismatch");
	};
	// Set up the flows
	for(unsigned src=0; src<numHosts; src++) {
		// Assign a flow for a source-destination pair
		std::list<uint64_t>::iterator sizeIt = flowsizes[src].begin();
		std::list<unsigned>::iterator destIt = flowdests[src].begin();
		while (sizeIt != flowsizes[src].end()) {
			ApplicationContainer app;
			bool useTcp = UniformVariable(0,1).GetValue() < tcp;
			const char* socketSpec = (useTcp)?"ns3::TcpSocketFactory":"ns3::UdpSocketFactory";

			if (cbr) {
				OnOffHelper onoff (socketSpec, Address (InetSocketAddress (addrs[*destIt], port)));
				onoff.SetAttribute ("DataRate", DataRateValue(DataRate(*sizeIt)));
				onoff.SetAttribute ("PacketSize", UintegerValue(1000));
				onoff.SetAttribute ("OffTime", RandomVariableValue(ConstantVariable(0.0)));
				onoff.SetAttribute ("MaxBytes", UintegerValue(bytes));
				app = onoff.Install(fattree->HostNodes().Get(src));
			} else {
				// Use MMPP helper to create an MMPP traffic generator
				Ptr<RateVector> rateVector = CreateObject<RateVector>();
				rateVector->push_back(DataRate(1.0*(*sizeIt)));
				rateVector->push_back(DataRate(1.5*(*sizeIt)));
				rateVector->push_back(DataRate(0.5*(*sizeIt)));
				MmppHelper mmpp(socketSpec, Address(InetSocketAddress(addrs[*destIt], port)));
				mmpp.SetAttribute ("GenMatrix", PointerValue(generator));
				mmpp.SetAttribute ("Rates", PointerValue(rateVector));
				mmpp.SetAttribute ("PacketSizes", PointerValue(pktsizes));
				mmpp.SetAttribute ("MaxBytes", UintegerValue(bytes));
				app = mmpp.Install(fattree->HostNodes().Get(src));
			};
			// Create a flow
			double desync = UniformVariable(0,0.1).GetValue();
			app.Start(Seconds(desync));
			NS_LOG_INFO((useTcp?"TCP":"UDP") << " flow "<< addrs[src] <<" -> "<< addrs[*destIt]
				<<" ("<< src+5*size*size <<" -> "<< *destIt+5*size*size <<") of rate "
				<< *sizeIt/1e6 <<"Mbps starts at "<< desync <<"s");
			if (stoptime) app.Stop(Seconds(stoptime));

			++sizeIt;
			++destIt;
		};
	};
	for(unsigned i=0; i<numHosts; i++) {
		// Assign the packet sink at every receiver node
		PacketSinkHelper sink("ns3::TcpSocketFactory", Address(InetSocketAddress(Ipv4Address::GetAny(), port)));
		ApplicationContainer app = sink.Install(fattree->HostNodes().Get(i));
		app.Start(Seconds(0));
	};
	for(unsigned i=0; i<numHosts; i++) {
		// Assign the packet sink at every receiver node
		PacketSinkHelper sink("ns3::UdpSocketFactory", Address(InetSocketAddress(Ipv4Address::GetAny(), port)));
		ApplicationContainer app = sink.Install(fattree->HostNodes().Get(i));
		app.Start(Seconds(0));
	};

	// Collect packet trace
	std::cout << std::setprecision(9) << std::fixed;
	std::cerr << std::setprecision(9) << std::fixed;
	std::clog << std::setprecision(9) << std::fixed;
//	PointToPointHelper::EnablePcapAll ("FatTreeSimulation");
//	std::ofstream ascii;
//	ascii.open (outputfile);
	fattree->EnableAsciiAll (std::cout);
//	LogComponentEnableAll(LOG_LEVEL_ALL);
	LogComponentDisable("Buffer", LOG_LEVEL_ALL);
	LogComponentDisable("PacketMetadata", LOG_LEVEL_ALL);
	LogComponentDisable("ByteTagList", LOG_LEVEL_ALL);
	LogComponentDisable("Queue", LOG_LEVEL_ALL);
	LogComponentDisable("MapScheduler", LOG_LEVEL_ALL);
//	LogComponentEnable("QbbNetDevice", LOG_LEVEL_ALL);
//	LogComponentEnable("PointToPointNetDevice", LOG_LEVEL_ALL);
//	LogComponentEnable("RpNetDevice", LOG_LEVEL_ALL);
//	LogComponentEnable("CpNetDevice", LOG_LEVEL_ALL);
//	LogComponentEnable("MmppApplication", LOG_LEVEL_ALL);
//	LogComponentEnable("TcpSocketImpl", LOG_LEVEL_ALL);
//	LogComponentEnable("TcpRxBuffer", LOG_LEVEL_ALL);

	// Run the simulation
	NS_LOG_INFO("Run Simulation.");
	Simulator::Stop(Seconds(stoptime?2*stoptime:1000));
	if (!dryrun) Simulator::Run ();
	Simulator::Destroy ();
	NS_LOG_INFO("Done.");
	return 0;
}
