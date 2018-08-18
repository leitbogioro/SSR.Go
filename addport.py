#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import readjson

TcpPort = "iptables -I INPUT -m state --state NEW -m tcp -p tcp --dport " + str(readjson.ConfPort) +" -j ACCEPT"
UdpPort = "iptables -I INPUT -m state --state NEW -m tcp -p tcp --dport " + str(readjson.ConfPort) +" -j ACCEPT"
os.system(TcpPort)
os.system(UdpPort)
