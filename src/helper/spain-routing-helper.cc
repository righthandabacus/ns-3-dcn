/* -*-  Mode: C++; c-file-style: "gnu"; indent-tabs-mode:nil; -*- */
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

#include "spain-routing-helper.h"
#include "ns3/log.h"
#include "ns3/ipv4-list-routing.h"
#include "ns3/hash-function-impl.h"

NS_LOG_COMPONENT_DEFINE("SpainRoutingHelper");

namespace ns3 {

SpainRoutingHelper::SpainRoutingHelper() : m_hashfunc(0)
{
  m_hashfunc = CreateObject<HashHsieh> ();
}

SpainRoutingHelper::SpainRoutingHelper (const SpainRoutingHelper &o)
{
  if (m_hashfunc == 0) {
    m_hashfunc = CreateObject<HashHsieh> ();
  };
}

SpainRoutingHelper* 
SpainRoutingHelper::Copy (void) const 
{
  return new SpainRoutingHelper (*this); 
}

Ptr<Ipv4RoutingProtocol> 
SpainRoutingHelper::Create (Ptr<Node> node) const
{
  Ptr<SpainRouting> r = CreateObject<SpainRouting> ();
  r->SetHashFunction(m_hashfunc);
  return r;
}

Ptr<SpainRouting>
SpainRoutingHelper::GetSpainRouting (Ptr<Ipv4> ipv4) const
{
  NS_LOG_FUNCTION (this);
  Ptr<Ipv4RoutingProtocol> ipv4rp = ipv4->GetRoutingProtocol ();
  NS_ASSERT_MSG (ipv4rp, "No routing protocol associated with Ipv4");
  if (DynamicCast<SpainRouting> (ipv4rp))
    {
      NS_LOG_LOGIC ("Spain routing found as the main IPv4 routing protocol.");
      return DynamicCast<SpainRouting> (ipv4rp); 
    } 
  if (DynamicCast<Ipv4ListRouting> (ipv4rp))
    {
      Ptr<Ipv4ListRouting> lrp = DynamicCast<Ipv4ListRouting> (ipv4rp);
      int16_t priority;
      for (uint32_t i = 0; i < lrp->GetNRoutingProtocols ();  i++)
        {
          NS_LOG_LOGIC ("Searching for Spain routing in list");
          Ptr<Ipv4RoutingProtocol> temp = lrp->GetRoutingProtocol (i, priority);
          if (DynamicCast<SpainRouting> (temp))
            {
              NS_LOG_LOGIC ("Found Spain routing in list");
              return DynamicCast<SpainRouting> (temp);
            }
        }
    }
  NS_LOG_LOGIC ("Spain routing not found");
  return 0;
}

}; // namespace ns3
