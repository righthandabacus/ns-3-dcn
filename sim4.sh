#!/bin/bash
# Process the simulation result

for time in 250; do
for pc in 50 95 60 90 70 80; do
	if [ ! -e ../_CBR/adm-tcp-norr$time-$pc.gz ]; then
		./waf --run="CBRAdm --pc=0.$pc --tcp=1 --rr=0 --pt=$time" 2>../_CBR/adm-tcp-norr$time-$pc.log | gzip -9 > ../_CBR/adm-tcp-norr$time-$pc.gz
		cd ../_CBR
		zcat adm-tcp-norr$time-$pc.gz |
		tee >(grep 'CnHead\|Pause' | gzip -9 > adm-tcp-norr$time-$pc.cn.gz) |
		tee >(tail -1000 > adm-tcp-norr$time-$pc.tail1k) |
		tee >(perl -e '$n=0;while(<>){print if ++$n<1001;};' > adm-tcp-norr$time-$pc.head1k) |
		./trRoutes.pl > adm-tcp-norr$time-$pc.flows
		cd ../ns3-f
	fi
	if [ ! -e ../_CBR/ran-tcp-norr$time-$pc.gz ]; then
		./waf --run="CBRSim --pc=0.$pc --tcp=1 --rr=0 --pt=$time" 2>../_CBR/ran-tcp-norr$time-$pc.log | gzip -9 > ../_CBR/ran-tcp-norr$time-$pc.gz
		cd ../_CBR
		zcat ran-tcp-norr$time-$pc.gz |
		tee >(grep 'CnHead\|Pause' | gzip -9 > ran-tcp-norr$time-$pc.cn.gz) |
		tee >(tail -1000 > ran-tcp-norr$time-$pc.tail1k) |
		tee >(perl -e '$n=0;while(<>){print if ++$n<1001;};' > ran-tcp-norr$time-$pc.head1k) |
		./trRoutes.pl > ran-tcp-norr$time-$pc.flows
		cd ../ns3-f
	fi
	if [ ! -e ../_CBR/adm-udp-norr$time-$pc.gz ]; then
		./waf --run="CBRAdm --pc=0.$pc --tcp=0 --rr=0 --pt=$time" 2>../_CBR/adm-udp-norr$time-$pc.log | gzip -9 > ../_CBR/adm-udp-norr$time-$pc.gz
		cd ../_CBR
		zcat adm-udp-norr$time-$pc.gz |
		tee >(grep 'CnHead\|Pause' | gzip -9 > adm-udp-norr$time-$pc.cn.gz) |
		tee >(tail -1000 > adm-udp-norr$time-$pc.tail1k) |
		tee >(perl -e '$n=0;while(<>){print if ++$n<1001;};' > adm-udp-norr$time-$pc.head1k) |
		./trRoutes.pl > adm-udp-norr$time-$pc.flows
		cd ../ns3-f
	fi
	if [ ! -e ../_CBR/ran-udp-norr$time-$pc.gz ]; then
		./waf --run="CBRSim --pc=0.$pc --tcp=0 --rr=0 --pt=$time" 2>../_CBR/ran-udp-norr$time-$pc.log | gzip -9 > ../_CBR/ran-udp-norr$time-$pc.gz
		cd ../_CBR
		zcat ran-udp-norr$time-$pc.gz |
		tee >(grep 'CnHead\|Pause' | gzip -9 > ran-udp-norr$time-$pc.cn.gz) |
		tee >(tail -1000 > ran-udp-norr$time-$pc.tail1k) |
		tee >(perl -e '$n=0;while(<>){print if ++$n<1001;};' > ran-udp-norr$time-$pc.head1k) |
		./trRoutes.pl > ran-udp-norr$time-$pc.flows
		cd ../ns3-f
	fi
done
done

for time in 250; do
for pc in 50 95 60 90 70 80; do
	if [ ! -e ../_MMPP/adm-udp-norr$time-$pc.gz ]; then
		./waf --run="Admissible --pc=0.$pc --tcp=0 --rr=0 --pt=$time" 2>../_MMPP/adm-udp-norr$time-$pc.log | gzip -9 > ../_MMPP/adm-udp-norr$time-$pc.gz
		cd ../_MMPP
		zcat adm-udp-norr$time-$pc.gz |
		tee >(grep 'CnHead\|Pause' | gzip -9 > adm-udp-norr$time-$pc.cn.gz) |
		tee >(tail -1000 > adm-udp-norr$time-$pc.tail1k) |
		tee >(perl -e '$n=0;while(<>){print if ++$n<1001;};' > adm-udp-norr$time-$pc.head1k) |
		./trRoutes.pl > adm-udp-norr$time-$pc.flows
		cd ../ns3-f
	fi
	if [ ! -e ../_MMPP/ran-udp-norr$time-$pc.gz ]; then
		./waf --run="Simulation --pc=0.$pc --tcp=0 --rr=0 --pt=$time" 2>../_MMPP/ran-udp-norr$time-$pc.log | gzip -9 > ../_MMPP/ran-udp-norr$time-$pc.gz
		cd ../_MMPP
		zcat ran-udp-norr$time-$pc.gz |
		tee >(grep 'CnHead\|Pause' | gzip -9 > ran-udp-norr$time-$pc.cn.gz) |
		tee >(tail -1000 > ran-udp-norr$time-$pc.tail1k) |
		tee >(perl -e '$n=0;while(<>){print if ++$n<1001;};' > ran-udp-norr$time-$pc.head1k) |
		./trRoutes.pl > ran-udp-norr$time-$pc.flows
		cd ../ns3-f
	fi
	if [ ! -e ../_MMPP/adm-tcp-norr$time-$pc.gz ]; then
		./waf --run="Admissible --pc=0.$pc --tcp=1 --rr=0 --pt=$time" 2>../_MMPP/adm-tcp-norr$time-$pc.log | gzip -9 > ../_MMPP/adm-tcp-norr$time-$pc.gz
		cd ../_MMPP
		zcat adm-tcp-norr$time-$pc.gz |
		tee >(grep 'CnHead\|Pause' | gzip -9 > adm-tcp-norr$time-$pc.cn.gz) |
		tee >(tail -1000 > adm-tcp-norr$time-$pc.tail1k) |
		tee >(perl -e '$n=0;while(<>){print if ++$n<1001;};' > adm-tcp-norr$time-$pc.head1k) |
		./trRoutes.pl > adm-tcp-norr$time-$pc.flows
		cd ../ns3-f
	fi
	if [ ! -e ../_MMPP/ran-tcp-norr$time-$pc.gz ]; then
		./waf --run="Simulation --pc=0.$pc --tcp=1 --rr=0 --pt=$time" 2>../_MMPP/ran-tcp-norr$time-$pc.log | gzip -9 > ../_MMPP/ran-tcp-norr$time-$pc.gz
		cd ../_MMPP
		zcat ran-tcp-norr$time-$pc.gz |
		tee >(grep 'CnHead\|Pause' | gzip -9 > ran-tcp-norr$time-$pc.cn.gz) |
		tee >(tail -1000 > ran-tcp-norr$time-$pc.tail1k) |
		tee >(perl -e '$n=0;while(<>){print if ++$n<1001;};' > ran-tcp-norr$time-$pc.head1k) |
		./trRoutes.pl > ran-tcp-norr$time-$pc.flows
		cd ../ns3-f
	fi
done
done
