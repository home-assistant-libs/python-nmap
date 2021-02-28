#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Install : python setup.py install
    Register : python setup.py register

    platform = 'Unix',
    download_url = 'http://xael.org/norman/python/python-nmap/',
"""

import codecs
import os
from distutils.core import setup, Command, Extension

nmap = Extension(
    'nmap',
    sources=['nmap/nmap.py', 'nmap/__init__.py', 'nmap/example.py']
)

from nmap import *


here = os.path.dirname(os.path.abspath(__file__))
version = nmap.__version__


class VersionCommand(Command):
    description = 'Show library version'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(version)


# Get the short description
description = 'This is a python class to use nmap and access scan results from python3'

# Get the long description
with codecs.open(os.path.join(here, 'README.rst')) as f:
    long_description = '\n{}'.format(f.read())

# Get change log
with codecs.open(os.path.join(here, 'CHANGELOG')) as f:
    changelog = f.read()
    long_description += '\n\n{}'.format(changelog)

setup(
    author='Alexandre Norman',
    author_email='norman@xael.org',
    # bugtrack_url='https://bitbucket.org/xael/python-nmap',
    cmdclass={'version': VersionCommand},
    description=description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking",
        "Topic :: System :: Networking :: Firewalls",
        "Topic :: System :: Networking :: Monitoring",
    ],
    keywords="nmap, portscanner, network, sysadmin",
    # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    license='gpl-3.0.txt',
    long_description=long_description,
    name='python-nmap',
    packages=['nmap'],
    platforms=[
        "Operating System :: OS Independent",
    ],
    url='http://xael.org/pages/python-nmap-en.html',
    version=version,
)
