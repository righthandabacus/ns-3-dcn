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
using namespace std;

class NewObject : public Object
{
  public:
    static TypeId GetTypeId(void) {
      static TypeId tid = TypeId("NewObject")
	.SetParent<ObjectBase> ()
	.AddAttribute ("X", "Just an integer",
	               IntegerValue(99),
		       MakeIntegerAccessor (&NewObject::x),
		       MakeIntegerChecker<int>());
      return tid;
    };
    int GetX() const { return x; };
  private:
    int x;

};

NS_LOG_COMPONENT_DEFINE ("AttributeExample");
NS_OBJECT_ENSURE_REGISTERED(NewObject);

int 
main (int argc, char *argv[])
{
  Ptr<NewObject> n = CreateObject<NewObject>();
  cout << n->GetX() << endl;
  return 0;
}
