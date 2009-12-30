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

#ifndef CP_NET_DEVICE_H
#define CP_NET_DEVICE_H

#include "ns3/qbb-net-device.h"

namespace ns3 {

/**
 * \class CpNetDevice
 * \brief Congestion Point Device for a Point to Point Network Link
 *
 * This CpNetDevice class extends PointToPointNetDevice
 * to support generating congestion notification packet
 * upon congestion.
 */
class CpNetDevice : public QbbNetDevice
{
public:
	static TypeId GetTypeId (void);

	CpNetDevice ();
	virtual ~CpNetDevice ();

	/**
	 * Queue up a packet to send out of this device
	 *
	 * This is a specialization of the pure virtual function inherited from
	 * NetDevice class. We extended the verison from PointToPointNetDevice
	 * to send congestion notifications.
	 */
	virtual bool Send(Ptr<Packet> packet, const Address &dest, uint16_t protocolNumber);
protected:
	uint8_t ShouldSendCN(flowid& fid, uint32_t pktSize);
	uint32_t m_qeq;
	uint32_t m_speedup;
	double m_w;
	int32_t m_qOld[qCnt];
	int32_t m_timeToMark[qCnt];
};

} // namespace ns3

#endif // CP_NET_DEVICE_H
