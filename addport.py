#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import readjson

CurPort=str(readjson.ConfPort)

AddTcpPort = "iptables -I INPUT -m state --state NEW -m tcp -p tcp --dport " + CurPort +" -j ACCEPT"
AddUdpPort = "iptables -I INPUT -m state --state NEW -m tcp -p tcp --dport " + CurPort +" -j ACCEPT"
os.system(AddTcpPort)
os.system(AddUdpPort)
