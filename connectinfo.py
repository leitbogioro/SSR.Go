#! /usr/bin/env python
# -*- coding: utf-8 -*-

import readjson
import urllib2
import base64
import os
import json
import socket

# 获取本机IP地址
# 此方法的原理是利用 UDP 协议来实现的，生成一个 UDP 包，将发送包的 IP 记录在 UDP 协议头中，然后从 UDP 包中获取本机 IP

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

thisip = get_host_ip()

# 定义配置变量

IP = str(thisip)
Port = str(readjson.ConfPort)
Pwd = str(readjson.ConfPwd)
base64Pwd = str(base64.encodestring(Pwd))[:-1]
Method = str(readjson.ConfMethod)
Protocol = str(readjson.ConfProtocol)
Obfs = str(readjson.ConfObfs)
SecondPart = "/?obfsparam="

# 输出客户端连接配置信息

print("Server IP: %s") % IP
print("Port: %s") % Port
print("Password: %s") % Pwd
print("Encryption method: %s") % Method
print("Transmission protocol: %s") % Protocol
print("Obfs model: %s") % Obfs

# 获取 ssr 链接

def GetSsrUrl():
    parts = [IP, Port, Protocol, Method, Obfs, base64Pwd]
    configs = str(':'.join(parts))
    RealSsrUrl = configs + SecondPart
    base64SsrUrl = str(base64.encodestring(RealSsrUrl))
    base64SsrUrl = base64SsrUrl.replace("\n", "")
    SsrUrl = "ssr://" + base64SsrUrl
    return SsrUrl

def GreenText(string):
    print("\033[32m")
    print("%s") % string
    print("\033[0m")

print("\n")
print("======================================== SSR Configuration url ========================================")
print("    Now you can copy the following url to share to your devices and friends to access a wide world!    ")
GreenText(GetSsrUrl())


