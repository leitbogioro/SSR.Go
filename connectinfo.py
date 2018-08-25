#! /usr/bin/env python
# -*- coding: utf-8 -*-

import readjson
import base64
import os
import json
from ssrextra import (is_internal_ip, get_host_ip, look_ip_from, GetSsrUrl, genQR_Code)

# 获取本机IP地址

# 默认采用发送 UDP 数据包的方式获取 IP 地址
thisip = get_host_ip()

# 如果检测到的是内网 IP，进一步的操作
if int(is_internal_ip(thisip)) == 1:
    thisip = look_ip_from()

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

# ssr客户端链接
ssr_url=str(GetSsrUrl(IP, Port, Protocol, Method, Obfs, base64Pwd, SecondPart))

# 绿色字体
def GreenText(string):
    print("\033[32m")
    print("%s") % string
    print("\033[0m")

# 输出信息
print("\n")
print("======================================== SSR Configuration url ========================================")
print("    Now you can copy the following url to share to your devices and friends to access a wide world!    ")
GreenText(ssr_url)

# 生成客户端二维码
genQR_Code(ssr_url, "/root/ssr_qrcode.png")
print("============= SSR Configuration QRCode has been storaged into root folder of the system! ==============")
