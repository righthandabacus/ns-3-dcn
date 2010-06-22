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

	uint32_t bc = 10e3;
	double tcp=0;
	int rr=1;
	double linkBw = 1e9;		// Link bandwidth in bps
	double linkDelay = 5e-9;	// Link delay in seconds (5ns = 1m wire)
	unsigned size = 3;		// Fat tree size
	double percent = 0.8;		// Percent of bandwidth to use per sending host
	uint64_t bytes = 0;		// Number of bytes to send per flow
	int maxflow = 15;		// Maximum number of flows per node
	int minflow = 5;		// Minimum number of flows per node
	int pausetime = 250;		// Pause duration in us
	bool dryrun=0;			// Fake the simulation or not
	bool cbr=0;			// Use CBR traffic?
	uint32_t speedup = 1;		// Speedup factor
	double stoptime = 0;		// Time to stop applications
	int bb = 100;			// Qbb threshold
	int qeq = 20;			// QueueEq

	CommandLine cmd;
	cmd.AddValue("speedup","Speed up factor of 802.1Qau",speedup);
	cmd.AddValue("bc","BC value of RP device",bc);
	cmd.AddValue("tcp","Percentage of TCP (1 to 0)",tcp);
	cmd.AddValue("cbr","Use CBR traffic gen (1 or 0)",cbr);
	cmd.AddValue("rr","Reroute scheme (0=no reroute, 1=random, 2=max prob, 3=biased random)",rr);
	cmd.AddValue("bw","Link bandwidth",linkBw);
	cmd.AddValue("delay","Link delay",linkDelay);
	cmd.AddValue("dryrun","Fake the simulation",dryrun);
	cmd.AddValue("size","Fat tree size",size);
	cmd.AddValue("bytes","Number of bytes to send per flow",bytes);
	cmd.AddValue("pc","Percentage of bandwidth to use per sending host",percent);
	cmd.AddValue("maxflow","Maximum number of flows per node",maxflow);
	cmd.AddValue("pt","Pause duration in microseconds",pausetime);
	cmd.AddValue("stop","Time to stop the flows", stoptime);
	cmd.AddValue("bb","Threshold for Qbb", bb);
	cmd.AddValue("qeq", "Equilibrium of queue in Qau", qeq);
	cmd.Parse (argc, argv);

	Config::SetDefault ("ns3::TcpSocket::SegmentSize", UintegerValue(1000));
	Config::SetDefault ("ns3::RpNetDevice::BC", UintegerValue(bc));
	Config::SetDefault ("ns3::QbbNetDevice::PauseTime", UintegerValue(pausetime));
	Config::SetDefault ("ns3::QbbNetDevice::QbbThreshold", UintegerValue(bb));
	Config::SetDefault ("ns3::QbbNetDevice::QbbEnabled", BooleanValue(true));
	Config::SetDefault ("ns3::QbbNetDevice::BufferSize", UintegerValue(65536));	// 64KiB
	Config::SetDefault ("ns3::RpNetDevice::MinRate", DataRateValue(DataRate("1Mbps")));
	Config::SetDefault ("ns3::CpNetDevice::SpeedUp", UintegerValue(speedup));
	Config::SetDefault ("ns3::CpNetDevice::QueueEq", UintegerValue(qeq));
	Config::SetDefault ("ns3::HashRouting::RerouteScheme", UintegerValue(rr));
	Config::SetDefault ("ns3::HashRouting::RerouteThreshold", UintegerValue(2));
	Config::SetDefault ("ns3::HashRouting::CnLifetime", TimeValue(Seconds(0.01)));

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
	std::list<uint64_t> partition;	//< A partition of link bandwidth
	std::list<uint64_t> flowsizes;	//< Flows sizes according to partition

	NS_LOG_INFO ("Create Application.");
	bool needTcpSink[numHosts];
	bool needUdpSink[numHosts];
	bool big = false;
	for(unsigned i=0; i<numHosts; i++) needTcpSink[i] = needUdpSink[i] = false;
	for(unsigned src=0; src<numHosts; src++) {
		// Partition bandwidth into random number of flows
		big = !big;
		for (int flownum = UniformVariable(minflow,maxflow+1).GetValue()*(big?1:10); flownum > 1; flownum--) {
			partition.push_back(UniformVariable(0,uint64_t(linkBw*percent)).GetValue());
		};
		partition.sort();
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
			unsigned dest = unsigned(UniformVariable(0, addrs.size()-1).GetValue());
			if (dest >= src) dest ++;
			bool useTcp = UniformVariable(0,1).GetValue() < tcp;
			const char* socketSpec = (useTcp)?"ns3::TcpSocketFactory":"ns3::UdpSocketFactory";
			if (useTcp) {
				needTcpSink[dest] = true;
			} else {
				needUdpSink[dest] = true;
			};

			ApplicationContainer app;
			if (cbr) {
				OnOffHelper onoff (socketSpec, Address (InetSocketAddress (addrs[dest], port)));
				onoff.SetAttribute ("DataRate", DataRateValue(DataRate(flowsizes.front())));
				onoff.SetAttribute ("PacketSize", UintegerValue(1000));
				onoff.SetAttribute ("OffTime", RandomVariableValue(ConstantVariable(0.0)));
				onoff.SetAttribute ("MaxBytes", UintegerValue(bytes));
				app = onoff.Install(fattree->HostNodes().Get(src));
			} else {
				// Use MMPP helper to create an MMPP traffic generator
				Ptr<RateVector> rateVector = CreateObject<RateVector>();
				rateVector->push_back(DataRate(1.0*flowsizes.front()));
				rateVector->push_back(DataRate(1.5*flowsizes.front()));
				rateVector->push_back(DataRate(0.5*flowsizes.front()));
				MmppHelper mmpp(socketSpec, Address(InetSocketAddress(addrs[dest], port)));
				mmpp.SetAttribute ("GenMatrix", PointerValue(generator));
				mmpp.SetAttribute ("Rates", PointerValue(rateVector));
				mmpp.SetAttribute ("PacketSizes", PointerValue(pktsizes));
				mmpp.SetAttribute ("MaxBytes", UintegerValue(bytes));
				app = mmpp.Install(fattree->HostNodes().Get(src));
			};
			// Create a flow
			//double desync = UniformVariable(0,1).GetValue();
			app.Start(Seconds(0));
			NS_LOG_INFO((useTcp?"TCP":"UDP") << " flow "<< addrs[src] <<" -> "<< addrs[dest]
				<<" ("<< src+5*size*size <<" -> "<< dest+5*size*size <<") of rate "
				<< flowsizes.front()/1e6 <<"Mbps starts at "<< 0 <<"s");
			if (stoptime > 0) app.Stop(Seconds(stoptime));

			flowsizes.pop_front();
		};
	};
	for(unsigned i=0; i<numHosts; i++) {
		// Assign the packet sink at every receiver node
		if (needTcpSink[i] == true) {
			PacketSinkHelper sink("ns3::TcpSocketFactory", Address(InetSocketAddress(Ipv4Address::GetAny(), port)));
			ApplicationContainer app = sink.Install(fattree->HostNodes().Get(i));
			app.Start(Seconds(0));
		} else if (needUdpSink[i] == true) {
			PacketSinkHelper sink("ns3::UdpSocketFactory", Address(InetSocketAddress(Ipv4Address::GetAny(), port)));
			ApplicationContainer app = sink.Install(fattree->HostNodes().Get(i));
			app.Start(Seconds(0));
		};
	};

	// Collect packet trace
	std::cout << std::setprecision(9) << std::fixed;
	std::cerr << std::setprecision(9) << std::fixed;
	std::clog << std::setprecision(9) << std::fixed;
//	PointToPointHelper::EnablePcapAll ("FatTreeSimulation");
//	std::ofstream ascii;
	fattree->EnableAsciiAll (std::cout);
//	LogComponentEnableAll(LOG_LEVEL_ALL);
	LogComponentDisable("Buffer", LOG_LEVEL_ALL);
	LogComponentDisable("PacketMetadata", LOG_LEVEL_ALL);
	LogComponentDisable("ByteTagList", LOG_LEVEL_ALL);
	LogComponentDisable("Queue", LOG_LEVEL_ALL);
	LogComponentDisable("MapScheduler", LOG_LEVEL_ALL);
//	LogComponentEnable("QbbNetDevice", LOG_LEVEL_ALL);
//	LogComponentEnable("QbbNetDevice", LOG_LEVEL_INFO);
//	LogComponentEnable("UdpSocketImpl", LOG_LEVEL_INFO);
//	LogComponentEnable("PointToPointNetDevice", LOG_LEVEL_ALL);
//	LogComponentEnable("RpNetDevice", LOG_LEVEL_ALL);
//	LogComponentEnable("CpNetDevice", LOG_LEVEL_ALL);
//	LogComponentEnable("MmppApplication", LOG_LEVEL_ALL);
//	LogComponentEnable("TcpSocketImpl", LOG_LEVEL_ALL);
//	LogComponentEnable("TcpRxBuffer", LOG_LEVEL_ALL);

	// Run the simulation
	NS_LOG_INFO("Run Simulation.");
	//Simulator::Stop(Seconds(stoptime?2*stoptime:1000));
	Simulator::Stop(Seconds(stoptime + 0.001));
//	PrintStat(fattree,&std::clog);
	if (!dryrun) Simulator::Run ();
	Simulator::Destroy ();
	NS_LOG_INFO("Done.");
	return 0;
}
