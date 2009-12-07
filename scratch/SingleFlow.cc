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
#include "ns3/global-routing-module.h"

using namespace ns3;

NS_LOG_COMPONENT_DEFINE ("SimulationScript");

const char outputfile[] = "SimulationOutput.tr";
const uint16_t port = 9;   // Discard port (RFC 863)

std::vector<ApplicationContainer> apps(54);

int main (int argc, char *argv[])
{
	// Turn on logging
	LogComponentEnable("SimulationScript", LOG_LEVEL_ALL);
	LogComponentEnableAll(LOG_PREFIX_TIME);
	LogComponentEnableAll(LOG_PREFIX_FUNC);
//	LogComponentPrintList();

	uint32_t bc = 50e3;
	bool tcp=0;
	bool rr=1;
	double linkBw = 100e6;		// Link bandwidth in bps
	double linkDelay = 250e-9;	// Link delay in seconds (5ns = 1m wire)
	unsigned size = 3;		// Fat tree size
	double percent = 0.8;		// Percent of bandwidth to use per sending host
	uint64_t bytes = 5e6;		// Number of bytes to send per flow
	int maxflow = 10;		// Maximum number of flows per node
	int pausetime = 300;		// Pause duration in us
	bool dryrun=0;			// Fake the simulation or not

	CommandLine cmd;
	cmd.AddValue("bc","BC value of RP device",bc);
	cmd.AddValue("tcp","Use TCP (1 or 0)",tcp);
	cmd.AddValue("rr","Enable reroute (1 or 0)",rr);
	cmd.AddValue("bw","Link bandwidth",linkBw);
	cmd.AddValue("delay","Link delay",linkDelay);
	cmd.AddValue("dryrun","Fake the simulation",dryrun);
	cmd.AddValue("size","Fat tree size",size);
	cmd.AddValue("bytes","Number of bytes to send per flow",bytes);
	cmd.AddValue("pc","Percentage of bandwidth to use per sending host",percent);
	cmd.AddValue("maxflow","Maximum number of flows per node",maxflow);
	cmd.AddValue("pt","Pause duration in microseconds",pausetime);
	cmd.Parse (argc, argv);

	const char* socketSpec = (tcp)?"ns3::TcpSocketFactory":"ns3::UdpSocketFactory";

	Config::SetDefault ("ns3::TcpSocket::SegmentSize", UintegerValue(1000));
	Config::SetDefault ("ns3::RpNetDevice::BC", UintegerValue(bc));
	Config::SetDefault ("ns3::QbbNetDevice::PauseTime", UintegerValue(pausetime));
	Config::SetDefault ("ns3::QbbNetDevice::QbbThreshold", UintegerValue(5));
	if (!rr) Config::SetDefault ("ns3::HashRoute::RoutingTable::EnableReroute", BooleanValue(false));

	// Build the fat tree network
	Ptr<FatTreeHelper> fattree = CreateObject<FatTreeHelper>(size);
	fattree->SetAttribute("HeDataRate", DataRateValue(DataRate(linkBw)));
	fattree->SetAttribute("EaDataRate", DataRateValue(DataRate(linkBw)));
	fattree->SetAttribute("AcDataRate", DataRateValue(DataRate(linkBw/2)));
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

	// Set up source-destination mapping (not done here because of random OD pair)
	std::vector<Ipv4Address> addrs;	// Host addresses
	const unsigned numHosts = size*size*size*2;
	Ipv4InterfaceContainer hostIfs = fattree->HostInterfaces();
	for(unsigned i=0; i<numHosts; i++) {
		addrs.push_back(hostIfs.GetAddress(i));
	};
	NS_ASSERT_MSG(addrs.size() == numHosts,
		"Number of hosts mismatch the size of fat tree.");
	std::list<uint64_t> partition;	//< A partition of link bandwidth
	std::list<uint64_t> flowsizes;	//< Flows sizes according to partition

	NS_LOG_INFO ("Create Application.");
	bool needSink[numHosts];
	for(unsigned i=0; i<numHosts; i++) needSink[i] = false;
	for(unsigned src=0; src<1 /*numHosts*/; src++) {
		NS_LOG_LOGIC("source = " << src);

		// Partition bandwidth into random number of flows
		/*for (int flownum = UniformVariable(0,20).GetValue() + 1; flownum > 1; flownum--) {
			partition.push_back(UniformVariable(0,static_cast<uint64_t>(linkBw*percent)).GetValue());
		};
		partition.sort();*/
		partition.push_back(static_cast<uint64_t>(linkBw*percent));
		uint64_t first = 0;
		uint64_t second;	// Flow size = second - first
		while (!partition.empty()) {
			second = partition.front();
			partition.pop_front();
			if (second == first) { continue; };	// Ignore empty flow
			flowsizes.push_back(second - first);
			first = second;
		};
		NS_LOG_INFO("There will be "<< flowsizes.size() << " flows from " << addrs[src]);

		// Assign a flow for a source-destination pair
		while (!flowsizes.empty()) {
			// Randomly pick the destination different from myself
			unsigned dest = unsigned(UniformVariable(0, numHosts-1).GetValue());
			if (dest >= src) dest ++;
			needSink[dest] = true;

			// Use MMPP helper to create an MMPP traffic generator
#if 1
			OnOffHelper mmpp (socketSpec, Address (InetSocketAddress (addrs[dest], port)));
			mmpp.SetAttribute ("DataRate", DataRateValue(DataRate(flowsizes.front())));
			mmpp.SetAttribute ("PacketSize", UintegerValue(1000));
			mmpp.SetAttribute ("OffTime", RandomVariableValue (ConstantVariable (0.0)));
			mmpp.SetAttribute ("MaxBytes", UintegerValue(bytes));
#else
			Ptr<RateVector> rateVector = CreateObject<RateVector>();
			rateVector->push_back(DataRate(1.0*flowsizes.front()*percent));
			rateVector->push_back(DataRate(2.0*flowsizes.front()*percent));
			rateVector->push_back(DataRate(0.5*flowsizes.front()*percent));
			MmppHelper mmpp(socketSpec, Address(InetSocketAddress(addrs[dest], port)));
			mmpp.SetAttribute ("GenMatrix", PointerValue(generator));
			mmpp.SetAttribute ("Rates", PointerValue(rateVector));
			mmpp.SetAttribute ("PacketSizes", PointerValue(pktsizes));
			mmpp.SetAttribute ("MaxBytes", UintegerValue(flowsizes.front()/linkBw*bytes));
#endif
			// Create a flow
			ApplicationContainer app = mmpp.Install(fattree->HostNodes().Get(src));
			double desync = UniformVariable(0,1).GetValue();
			app.Start(Seconds(desync));
			NS_LOG_INFO("Flow "<< addrs[src] <<" -> "<< addrs[dest]
				<<" ("<< src+5*size*size <<" -> "<< dest+5*size*size <<") of rate "
				<< flowsizes.front()/1e6 <<"Mbps starts at "<< desync <<"s");
			//app.Stop(Seconds(desync+DURATION));
			//
			flowsizes.pop_front();
		};
	};
	for(unsigned i=0; i<numHosts; i++) {
		// Assign the packet sink at every receiver node
		if (needSink[i] == false) continue;
		PacketSinkHelper sink(socketSpec, Address(InetSocketAddress(Ipv4Address::GetAny(), port)));
		ApplicationContainer app = sink.Install(fattree->HostNodes().Get(i));
		app.Start(Seconds(0));
	};

	// Collect packet trace
//	PointToPointHelper::EnablePcapAll ("FatTreeSimulation");
//	std::ofstream ascii;
//	ascii.open (outputfile);
//	PointToPointHelper::EnableAsciiAll (ascii);
	std::cout << std::setprecision(9) << std::fixed;
	std::clog << std::setprecision(9) << std::fixed;
	FatTreeHelper::EnableAsciiAll (std::cout);
//	LogComponentEnableAll(LOG_LEVEL_ALL);
	LogComponentEnable("OnOffApplication", LOG_LEVEL_ALL);
	LogComponentEnable("Simulator", LOG_LEVEL_ALL);
	LogComponentEnable("MapScheduler", LOG_LEVEL_ALL);
	LogComponentEnable("Buffer", LOG_LEVEL_ALL);
	LogComponentEnable("RpNetDevice", LOG_LEVEL_ALL);
	LogComponentEnable("CpNetDevice", LOG_LEVEL_ALL);
	LogComponentEnable("QbbNetDevice", LOG_LEVEL_ALL);
	LogComponentEnable("PointToPointNetDevice", LOG_LEVEL_ALL);

	// Run the simulation
	NS_LOG_INFO("Run Simulation.");
	Simulator::Stop(Seconds(15000));
	Simulator::Run ();
	Simulator::Destroy ();
	NS_LOG_INFO("Done.");
	return 0;
}
