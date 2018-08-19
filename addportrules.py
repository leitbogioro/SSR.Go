#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import readjson
import subprocess

CurPort=str(readjson.ConfPort)
TcpPort = "iptables -I INPUT -m state --state NEW -m tcp -p tcp --dport " + CurPort +" -j ACCEPT"
UdpPort = "iptables -I INPUT -m state --state NEW -m udp -p udp --dport " + CurPort +" -j ACCEPT"

# 决定是否增加端口
def JudgeAddPort():
    # 设置查询 iptables 规则
    SetRules='iptables -L INPUT -n --line-numbers | grep ' + CurPort
    # 调用 shell
    runShell=subprocess.Popen(SetRules, shell=True, stdout=subprocess.PIPE)
    # 输出包含 SSR 端口的防火墙规则
    shellOutput=runShell.communicate()[0]
    if int(shellOutput.find(CurPort)) == -1:
        os.system(TcpPort)
        os.system(UdpPort)

JudgeAddPort()
