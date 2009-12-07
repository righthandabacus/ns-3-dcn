/* vim: set cin sw=4 syn=cpp ru nu ts=4 cul cuc lbr: */
/*
 * Copyright (c) 2009 Adrian Sai-wah Tam
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
 * Author: Adrian Sai-wah Tam <adrian.sw.tam@gmail.com>
 */

#include "tcp-rfc793.h"
#include "ns3/log.h"

NS_LOG_COMPONENT_DEFINE ("TcpRfc793");

using namespace std;

namespace ns3 {

NS_OBJECT_ENSURE_REGISTERED (TcpRfc793);

TypeId
TcpRfc793::GetTypeId ()
{
	static TypeId tid = TypeId("ns3::TcpRfc793")
		.SetParent<TcpSocketImpl> ()
		.AddConstructor<TcpRfc793> ()
		;
	return tid;
}

TcpRfc793::TcpRfc793 ()
{
	NS_LOG_FUNCTION (this);
}

TcpRfc793::TcpRfc793(const TcpRfc793& sock) : TcpSocketImpl(sock)
{ }

TcpRfc793::~TcpRfc793 ()
{ }

Ptr<TcpSocketImpl> TcpRfc793::Fork ()
{
	return CopyObject<TcpRfc793> (this);
}

void
TcpRfc793::DupAck (const TcpHeader& t, uint32_t count)
{ };

void
TcpRfc793::SetSSThresh (uint32_t threshold)
{ }

uint32_t
TcpRfc793::GetSSThresh (void) const
{
	return 0;
}

void
TcpRfc793::SetInitialCwnd (uint32_t cwnd)
{ }

uint32_t
TcpRfc793::GetInitialCwnd (void) const
{
	return 0;
}

}//namespace ns3
