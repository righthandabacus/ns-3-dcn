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
#include "ns3/nstime.h"

using namespace ns3;

class FTable : public Object
{
public:
	static TypeId GetTypeId (void);

	FTable () ;
	virtual ~FTable (); 

	Time GetThreshold() { return m_threshold; };

protected:
	Time m_threshold;
};

NS_LOG_COMPONENT_DEFINE ("FTable");
NS_OBJECT_ENSURE_REGISTERED (FTable);

TypeId
FTable::GetTypeId (void)
{
	static TypeId tid = TypeId ("ns3::FTable")
	.SetParent<Object> ()
	.AddConstructor<FTable> ()
	.AddAttribute ( "Threshold", 
			"Expiry threshold of a flow",
			TimeValue (Seconds(5)),
			MakeTimeAccessor (&FTable::m_threshold),
			MakeTimeChecker())
	;
	return tid;
}

FTable::FTable ()
{
	NS_LOG_FUNCTION (this);
	//m_threshold = Seconds(5);
	NS_LOG_LOGIC("Threshold = " << m_threshold);
}

FTable::~FTable ()
{
}

int 
main (int argc, char *argv[])
{
  LogComponentEnable("FTable", LOG_LEVEL_ALL);
  LogComponentEnable("FTable", LOG_PREFIX_TIME);
  Ptr<FTable> n = CreateObject<FTable>();
  std::cout << n->GetThreshold() << std::endl;
  return 0;
}
