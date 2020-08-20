#! /usr/bin/env bash

#tcpdump -i <interface> -s 65535 -w <file>
tcpdump -i eth0 -s 65535 -w ../log/tcpdump.pcap
