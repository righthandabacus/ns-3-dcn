#!/bin/bash

DATAPATH="../_CBR"

for pc in 50 60 70 80 90 95; do
	if [ ! -e $DATAPATH/adm-tcp-$pc.bz2 ]; then
		./waf --run="Admissible --pc=0.$pc --tcp=1 --rr=1" 2>$DATAPATH/adm-tcp-$pc.log
	fi
	if [ ! -e $DATAPATH/adm-udp-$pc.bz2 ]; then
		./waf --run="Admissible --pc=0.$pc --tcp=0 --rr=1" 2>$DATAPATH/adm-udp-$pc.log
	fi
	if [ ! -e $DATAPATH/adm-tcp-norr-$pc.bz2 ]; then
		./waf --run="Admissible --pc=0.$pc --tcp=1 --rr=0" 2>$DATAPATH/adm-tcp-norr-$pc.log
	fi
	if [ ! -e $DATAPATH/adm-udp-norr-$pc.bz2 ]; then
		./waf --run="Admissible --pc=0.$pc --tcp=0 --rr=0" 2>$DATAPATH/adm-udp-norr-$pc.log
	fi
	if [ ! -e $DATAPATH/ran-tcp-$pc.bz2 ]; then
		./waf --run="Simulation --pc=0.$pc --tcp=1 --rr=1" 2>$DATAPATH/ran-tcp-$pc.log
	fi
	if [ ! -e $DATAPATH/ran-udp-$pc.bz2 ]; then
		./waf --run="Simulation --pc=0.$pc --tcp=0 --rr=1" 2>$DATAPATH/ran-udp-$pc.log
	fi
	if [ ! -e $DATAPATH/ran-tcp-norr-$pc.bz2 ]; then
		./waf --run="Simulation --pc=0.$pc --tcp=1 --rr=0" 2>$DATAPATH/ran-tcp-norr-$pc.log
	fi
	if [ ! -e $DATAPATH/ran-udp-norr-$pc.bz2 ]; then
		./waf --run="Simulation --pc=0.$pc --tcp=0 --rr=0" 2>$DATAPATH/ran-udp-norr-$pc.log
	fi
done
