===========
python-nmap
===========

|PyPI latest| |PyPI Version| |PyPI License|

python-nmap is a python library which helps in using nmap port scanner. It allows to easilly manipulate nmap scan results and will be a perfect tool for systems administrators who want to automatize scanning task and reports. It also supports nmap script outputs.

It can even be used asynchronously. Results are returned one host at a time to a callback function defined by the user.

Download latest
===============

    python-nmap-0.4.1.tar.gz - 2015-08-21
    md5sum is b466e4b2ef30a0b9c0cb80aac215fb79

Warning : this version is intended to work with Python 3.x. For Python 2.x, please use python-nmap-0.1.4.tar.gz

Download development version
============================


.. code-block:: bash

    $ hg clone https://bitbucket.org/xael/python-nmap

Installation
============

From the shell, uncompress python-nmap-0.4.1.tar.gz and then run make :

.. code-block:: bash

    $ tar xvzf python-nmap-0.4.1.tar.gz
    $ cd python-nmap-0.4.1
    $ python setup.py install

or using Pip

.. code-block:: bash

    $ pip install python-nmap

Now you may invoke nmap from python


.. code-block:: bash

    $ python
    Python 2.6.4 (r264:75706, Dec  7 2009, 18:45:15)
    [GCC 4.4.1] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >> import nmap


Usage
=====

From python/ipython:
--------------------

.. code-block:: python

    >>> import nmap
    >>> nm = nmap.PortScanner()
    >>> nm.scan('127.0.0.1', '22-443')
    >>> nm.command_line()
    'nmap -oX - -p 22-443 -sV 127.0.0.1'
    >>> nm.scaninfo()
    {'tcp': {'services': '22-443', 'method': 'connect'}}
    >>> nm.all_hosts()
    ['127.0.0.1']
    >>> nm['127.0.0.1'].hostname()
    'localhost'
    >>> nm['127.0.0.1'].state()
    'up'
    >>> nm['127.0.0.1'].all_protocols()
    ['tcp']
    >>> nm['127.0.0.1']['tcp'].keys()
    [80, 25, 443, 22, 111]
    >>> nm['127.0.0.1'].has_tcp(22)
    True
    >>> nm['127.0.0.1'].has_tcp(23)
    False
    >>> nm['127.0.0.1']['tcp'][22]
    {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh'}
    >>> nm['127.0.0.1'].tcp(22)
    {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh'}
    >>> nm['127.0.0.1']['tcp'][22]['state']
    'open'

    >>> for host in nm.all_hosts():
    >>>     print('----------------------------------------------------')
    >>>     print('Host : %s (%s)' % (host, nm[host].hostname()))
    >>>     print('State : %s' % nm[host].state())
    >>>     for proto in nm[host].all_protocols():
    >>>         print('----------')
    >>>         print('Protocol : %s' % proto)
    >>>
    >>>         lport = nm[host][proto].keys()
    >>>         lport.sort()
    >>>         for port in lport:
    >>>             print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
    ----------------------------------------------------
    Host : 127.0.0.1 (localhost)
    State : up
    ----------
    Protocol : tcp
    port : 22	state : open
    port : 25	state : open
    port : 80	state : open
    port : 111	state : open
    port : 443	state : open


To export to a file
-------------------

.. code-block:: python

    >>> print(nm.csv())
    host;protocol;port;name;state;product;extrainfo;reason;version;conf
    127.0.0.1;tcp;22;ssh;open;OpenSSH;protocol 2.0;syn-ack;5.9p1 Debian 5ubuntu1;10
    127.0.0.1;tcp;25;smtp;open;Exim smtpd;;syn-ack;4.76;10
    127.0.0.1;tcp;53;domain;open;dnsmasq;;syn-ack;2.59;10
    127.0.0.1;tcp;80;http;open;Apache httpd;(Ubuntu);syn-ack;2.2.22;10
    127.0.0.1;tcp;111;rpcbind;open;;;syn-ack;;10
    127.0.0.1;tcp;139;netbios-ssn;open;Samba smbd;workgroup: WORKGROUP;syn-ack;3.X;10
    127.0.0.1;tcp;443;;open;;;syn-ack;;


To check the network status
---------------------------

.. code-block:: python

    >>> nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
    >>> hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    >>> for host, status in hosts_list:
    >>>     print('{0}:{1}'.host)
    192.168.1.0:down
    192.168.1.1:up
    192.168.1.10:down
    192.168.1.100:down
    192.168.1.101:down
    192.168.1.102:down
    192.168.1.103:down
    192.168.1.104:down
    192.168.1.105:down
    [...]


Using a Scanner Async
---------------------

.. code-block:: python

    >>> nma = nmap.PortScannerAsync()
    >>> def callback_result(host, scan_result):
    >>>     print '------------------'
    >>>     print host, scan_result
    >>>
    >>> nma.scan(hosts='192.168.1.0/30', arguments='-sP', callback=callback_result)
    >>> while nma.still_scanning():
    >>>     print("Waiting >>>")
    >>>     nma.wait(2)   # you can do whatever you want but I choose to wait after the end of the scan
    >>>
    192.168.1.1 {'nmap': {'scanstats': {'uphosts': '1', 'timestr': 'Mon Jun  7 11:31:11 2010', 'downhosts': '0', 'totalhosts': '1', 'elapsed': '0.43'}, 'scaninfo': {}, 'command_line': 'nmap -oX - -sP 192.168.1.1'}, 'scan': {'192.168.1.1': {'status': {'state': 'up', 'reason': 'arp-response'}, 'hostname': 'neufbox'}}}
    ------------------
    192.168.1.2 {'nmap': {'scanstats': {'uphosts': '0', 'timestr': 'Mon Jun  7 11:31:11 2010', 'downhosts': '1', 'totalhosts': '1', 'elapsed': '0.29'}, 'scaninfo': {}, 'command_line': 'nmap -oX - -sP 192.168.1.2'}, 'scan': {'192.168.1.2': {'status': {'state': 'down', 'reason': 'no-response'}, 'hostname': ''}}}
    ------------------
    192.168.1.3 {'nmap': {'scanstats': {'uphosts': '0', 'timestr': 'Mon Jun  7 11:31:11 2010', 'downhosts': '1', 'totalhosts': '1', 'elapsed': '0.29'}, 'scaninfo': {}, 'command_line': 'nmap -oX - -sP 192.168.1.3'}, 'scan': {'192.168.1.3': {'status': {'state': 'down', 'reason': 'no-response'}, 'hostname': ''}}}
    >>> nm = nmap.PortScannerYield() >>> for progressive_result in nm.scan('127.0.0.1/24', '22-25'): >>> print(progressive_result)


See also example.py in archive file.


Using a Scanner Async
---------------------

.. code-block:: python

    >>> nm = nmap.PortScanner()                                                                                                                                                                                                              
    >>> nm.scan('127.0.0.1', '22-40043', timeout=10)
    PortScannerTimeout: 'Timeout from nmap process'

Contributors
============

.. code-block:: text

    Steve 'Ashcrow' Milner
    Brian Bustin
    old.schepperhand
    Johan Lundberg
    Thomas D. maaaaz
    Robert Bost
    David Peltier
    Ed Jones


Homepage
========

http://xael.org/norman/python/python-nmap/


.. |PyPI Version| image:: https://img.shields.io/pypi/pyversions/python-nmap.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/python-nmap
.. |PyPI License| image:: https://img.shields.io/pypi/l/python-nmap.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/python-nmap
.. |PyPI latest| image:: https://img.shields.io/pypi/v/python-nmap.svg?maxAge=360
   :target: https://pypi.python.org/pypi/python-nmap
