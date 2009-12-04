/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/* vim:set cin cino=>4n-2f0{2^-2 sw=2 syn=cpp ru nu lbr:*/
/*
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
 */

#include "ns3/core-module.h"

using namespace ns3;

int
main (int argc, char *argv[])
{
	int X;
	double v;
	CommandLine cmd;
	cmd.AddValue("x","just an integer",X);
	cmd.AddValue("v","just a double",v);
	cmd.Parse (argc, argv);
	std::cout << X << std::endl;
	std::cout << v << std::endl;
}

/* Now you can:
 *   $ ./waf --run="scratch/cmdline --x=5"
 *   5
 *
 *   $ ./waf --run="scratch/cmdline --PrintHelp"
 *   --PrintHelp: Print this help message.
 *   --PrintGroups: Print the list of groups.
 *   --PrintTypeIds: Print all TypeIds.
 *   --PrintGroup=[group]: Print all TypeIds of group.
 *   --PrintAttributes=[typeid]: Print all attributes of typeid.
 *   --PrintGlobals: Print the list of globals.
 *   User Arguments:
 *       --x: just an integer
 *       --s: just a string
 */
