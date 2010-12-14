# -*- coding: latin-1 -*-

"""
nmap.py - v0.1.4 - 2010.06.20

Author : Alexandre Norman - norman@xael.org
Contributor: Steve 'Ashcrow' Milner - steve@gnulinux.net
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


Test strings :
^^^^^^^^^^^^
>>> import nmap
>>> nm = nmap.PortScanner()
>>> nm.scan('127.0.0.1', '22-443')
>>> nm.command_line()
u'nmap -oX - -p 22-443 -sV 127.0.0.1'
>>> nm.scaninfo()
{u'tcp': {'services': u'22-443', 'method': u'connect'}}
>>> nm.all_hosts()
[u'127.0.0.1']
>>> nm['127.0.0.1'].hostname()
u'localhost'
>>> nm['127.0.0.1'].state()
u'up'
>>> nm['127.0.0.1'].all_protocols()
[u'tcp']
>>> nm['127.0.0.1']['tcp'].keys()
[80, 25, 443, 22, 111]
>>> nm['127.0.0.1'].has_tcp(22)
True
>>> nm['127.0.0.1'].has_tcp(23)
False
>>> nm['127.0.0.1']['tcp'][22]
{'state': u'open', 'reason': u'syn-ack', 'name': u'ssh'}
>>> nm['127.0.0.1'].tcp(22)
{'state': u'open', 'reason': u'syn-ack', 'name': u'ssh'}
>>> nm['127.0.0.1']['tcp'][22]['state']
u'open'
"""


__author__ = 'Alexandre Norman (norman@xael.org)'
__version__ = '0.1.4'

from nmap import *
