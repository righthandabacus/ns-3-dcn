#!/bin/bash

if [ "$1" == "optimized" ]; then
	CXXDEFINES=NS3_LOG_ENABLE CXXFLAGS_EXTRA="-DNS3_LOG_ENABLE -ggdb -march=core2 -msse4 -mcx16 -msahf -pipe" ./waf configure -d optimized
	./waf
elif [ "$1" == "profile" ]; then
	CXXFLAGS_EXTRA="-march=core2 -msse4 -mcx16 -msahf -pipe" ./waf configure -d profile
	./waf
elif [ "$1" == "release" ]; then
	CXXFLAGS_EXTRA="-march=core2 -msse4 -mcx16 -msahf -pipe" ./waf configure -d release 
	./waf
elif [ "$1" == "debug" ]; then
	CXXFLAGS_EXTRA="-march=core2 -msse4 -mcx16 -msahf -pipe" ./waf configure -d debug 
	./waf
fi
