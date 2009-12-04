#!/bin/bash

DATAPATH="../_DATA"

for cbr in 1 0; do
for sim in adm sim; do
for pc in 50 95 60 90 70 80; do
for tcp in 1 0; do
for rr in 1 0; do
	if [ "$cbr" -eq 1 ]; then
		cbrtag="cbr"
	else
		cbrtag="mmp"
	fi
	if [ "$sim" == "sim" ]; then
		cmd="Simulation"
	else
		cmd="Admissible"
	fi
	if [ "$tcp" -eq 1 ]; then
		tcptag="tcp"
	else
		tcptag="udp"
	fi
	if [ "$rr" -eq 1 ]; then
		rrtag="+rr"
	else
		rrtag="-rr"
	fi
	FILE=$DATAPATH/$sim-$cbrtag-$tcptag$rrtag-$pc
	if [ ! -e $FILE.gz ]; then
		./waf --run="$cmd --cbr=$cbr --pc=0.$pc --tcp=$tcp --rr=$rr" 2>$FILE.log |
		tee >(grep 'CnHead\|Pause' | gzip -9 > $FILE.cn.gz) |
		tee >(tail -1000 > $FILE.tail1k) |
		tee >(perl -e '$n=0;while(<>){print if ++$n<1001;};' > $FILE.head1k) |
		tee >($DATAPATH/trRoutes.pl > $FILE.flows) |
		gzip -9 > $FILE.gz
	fi
done
done
done
done
done
