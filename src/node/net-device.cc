/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2005,2006 INRIA
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
 * Author: Mathieu Lacage <mathieu.lacage@sophia.inria.fr>
 */

#include "ns3/object.h"
#include "ns3/log.h"
#include "ns3/uinteger.h"
#include "net-device.h"

NS_LOG_COMPONENT_DEFINE ("NetDevice");

namespace ns3 {

NS_OBJECT_ENSURE_REGISTERED (NetDevice);

const Address NetDevice::Mac48Bcast = Mac48Address("ff:ff:ff:ff:ff:ff");

TypeId NetDevice::GetTypeId (void)
{
  static TypeId tid = TypeId ("ns3::NetDevice")
    .SetParent<Object> ()
    .AddAttribute ("Mtu", "The MAC-level Maximum Transmission Unit",
                   TypeId::ATTR_SET | TypeId::ATTR_GET,
                   UintegerValue (0xffff),
                   MakeUintegerAccessor (&NetDevice::SetMtu,
                                         &NetDevice::GetMtu),
                   MakeUintegerChecker<uint16_t> ())
                   
    ;
  return tid;
}

NetDevice::~NetDevice ()
{
  NS_LOG_FUNCTION_NOARGS ();
}

} // namespace ns3
