/* -*-  Mode: C++; c-file-style: "gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2006,2007 INRIA
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
 * Author: Mathieu Lacage, <mathieu.lacage@sophia.inria.fr>
 */
#include "ns3/packet.h"
#include "ns3/simulator.h"
#include "ns3/mobility-model.h"
#include "ns3/net-device.h"
#include "ns3/node.h"
#include "wifi-channel.h"
#include "propagation-loss-model.h"
#include "propagation-delay-model.h"


namespace ns3 {

WifiChannel::WifiChannel ()
{}
WifiChannel::~WifiChannel ()
{}

void 
WifiChannel::Add (Ptr<NetDevice> device,  ReceiveCallback callback)
{
  m_deviceList.push_back (std::make_pair (device, callback));
}
void 
WifiChannel::Send (Ptr<NetDevice> sender, const Packet &packet, double txPowerDbm,
                   uint64_t wifiMode) const
{
  Ptr<MobilityModel> senderMobility = sender->GetNode ()->QueryInterface<MobilityModel> (MobilityModel::iid);
  uint32_t j = 0;
  for (DeviceList::const_iterator i = m_deviceList.begin (); i != m_deviceList.end (); i++)
    {
      if (sender != i->first)
        {
          Ptr<MobilityModel> receiverMobility = i->first->GetNode ()->QueryInterface<MobilityModel> (MobilityModel::iid);
          double distance = senderMobility->GetDistanceFrom (receiverMobility);
          Time delay = m_delay->GetDelay (distance);
          double rxPowerDbm = m_loss->GetRxPower (txPowerDbm, distance);
          Simulator::Schedule (delay, &WifiChannel::Receive, this, 
                               j, packet, rxPowerDbm, wifiMode);
        }
      j++;
    }
}

void
WifiChannel::Receive (uint32_t i,
                      const Packet &packet, double rxPowerDbm,
                      uint64_t wifiMode) const
{
  m_deviceList[i].second (packet, rxPowerDbm, wifiMode);
}

uint32_t 
WifiChannel::GetNDevices (void) const
{
  return m_deviceList.size ();
}
Ptr<NetDevice> 
WifiChannel::GetDevice (uint32_t i) const
{
  return m_deviceList[i].first;
}

} // namespace ns3