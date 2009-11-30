/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2009 Polytechnic Institute of NYU
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
 * Programmer: Adrian Sai-wah Tam <adrian.sw.tam@gmail.com>
 */

#ifndef RP_NET_DEVICE_H
#define RP_NET_DEVICE_H

#include "ns3/qbb-net-device.h"

namespace ns3 {

class FlowTable;

/**
 * \class RpNetDevice
 * \brief Reaction Point Device for a Point to Point Network Link.
 *
 * This RpNetDevice class extends PointToPointNetDevice to
 * support handling of congestion notification packet upon
 * congestion. That is, imposing rate throttling to flows
 * as identified by the congestion notification signal, and
 * releasing the throttle when the signal is not present.
 */
class RpNetDevice : public QbbNetDevice
{
public:
  static const TypeId& GetTypeId (void);

  RpNetDevice ();
  virtual ~RpNetDevice ();
  virtual void Receive (Ptr<Packet> p);

protected:
  virtual void DequeueAndTransmit();
  void RateIncrease(unsigned qIndex);

  /* RP parameters */
  double   m_gd;		//< Control gain param for rate decrease
  double   m_minDec;		//< Min decrease ratio
  DataRate m_minRate;		//< Min sending rate
  uint32_t m_bc;		//< Tx byte counter timeout threshold
  DataRate m_rai;		//< Rate of additive increase
  DataRate m_rhai;		//< Rate of hyper-additive increase
  EventId  m_nextSend;		//< The next send event
  /* State variable for rate-limited queues */
  DataRate m_targetRate[qCnt];	//< Target rate
  DataRate m_rate[qCnt];	//< Current rate
  int32_t  m_txBytes[qCnt];	//< Tx byte counter
  uint32_t m_incCount[qCnt];	//< Count of Tx-based rate increments
  uint32_t m_timeCount[qCnt];	//< Count of timer-based rate increments
  Time     m_timer[qCnt];	//< Time to next self-increment
  Time     m_nextAvail[qCnt];	//< Soonest time of next send
  double   m_credits[qCnt];	//< Credits accumulated
};

} // namespace ns3

#endif // RP_NET_DEVICE_H
