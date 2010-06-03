#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
example.py - 2010.03.06

Author : Alexandre Norman - norman@xael.org
Licence : GPL v3 or any later version


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import sys


import nmap                         # import nmap.py module
try:
    nm = nmap.PortScanner()         # instantiate nmap.PortScanner object
except nmap.PortScannerError:
    print 'Nmap not found', sys.exc_info()[0]
    sys.exit(0)
except:
    print "Unexpected error:", sys.exc_info()[0]
    sys.exit(0)

nm.scan('127.0.0.1', '22-443')      # scan host 127.0.0.1, ports from 22 to 443
nm.command_line()                   # get command line used for the scan : nmap -oX - -p 22-443 127.0.0.1
nm.scaninfo()                       # get nmap scan informations {'tcp': {'services': '22-443', 'method': 'connect'}}
nm.all_hosts()                      # get all hosts that were scanned
nm['127.0.0.1'].hostname()          # get hostname for host 127.0.0.1
nm['127.0.0.1'].state()             # get state of host 127.0.0.1 (up|down|unknown|skipped) 
nm['127.0.0.1'].all_protocols()     # get all scanned protocols ['tcp', 'udp'] in (ip|tcp|udp|sctp)
nm['127.0.0.1']['tcp'].keys()       # get all ports for tcp protocol
nm['127.0.0.1'].all_tcp()           # get all ports for tcp protocol (sorted version)
nm['127.0.0.1'].all_udp()           # get all ports for udp protocol (sorted version)
nm['127.0.0.1'].all_ip()            # get all ports for ip protocol (sorted version)
nm['127.0.0.1'].all_sctp()          # get all ports for sctp protocol (sorted version)
nm['127.0.0.1'].has_tcp(22)         # is there any information for port 22/tcp on host 127.0.0.1
nm['127.0.0.1']['tcp'][22]          # get infos about port 22 in tcp on host 127.0.0.1
nm['127.0.0.1'].tcp(22)             # get infos about port 22 in tcp on host 127.0.0.1
nm['127.0.0.1']['tcp'][22]['state'] # get state of port 22/tcp on host 127.0.0.1 (open


# a more usefull example :
for host in nm.all_hosts():
    print '----------------------------------------------------'
    print 'Host : %s (%s)' % (host, nm[host].hostname())
    print 'State : %s' % nm[host].state()

    for proto in nm[host].all_protocols():
        print '----------'
        print 'Protocol : %s' % proto

        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print 'port : %s\tstate : %s' % (port, nm[host][proto][port]['state'])


