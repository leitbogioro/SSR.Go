#! /usr/bin/env python
# -*- coding: utf-8 -*-

import readjson
import urllib2
import base64
import os
import json

# 获取本机IP地址

thisip = urllib2.urlopen('http://api.ipify.org').read()
thisip = thisip.strip()

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

print("服务器IP：%s") % IP
print("端口：%s") % Port
print("密码：%s") % Pwd
print("加密方式: %s") % Method
print("传输协议：%s") % Protocol
print("混淆模式：%s") % Obfs

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
print("==================== SSR 配置链接 ====================")
print("    你可以复制以下链接分享给你的设备和朋友们使用了！  ")
GreenText(GetSsrUrl())


