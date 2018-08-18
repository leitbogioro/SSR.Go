#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import readjson

CurPort=str(readjson.ConfPort)

TcpPort = "iptables -I INPUT -m state --state NEW -m tcp -p tcp --dport " + CurPort +" -j ACCEPT"
UdpPort = "iptables -I INPUT -m state --state NEW -m tcp -p tcp --dport " + CurPort +" -j ACCEPT"
os.system(TcpPort)
os.system(UdpPort)
