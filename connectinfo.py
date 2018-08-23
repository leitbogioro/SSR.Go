#! /usr/bin/env python
# -*- coding: utf-8 -*-

import readjson
import urllib2
import base64
import os
import json
import socket
import qrcode

# 获取本机IP地址
# 此方法的原理是利用 UDP 协议来实现的，生成一个 UDP 包，将发送包的 IP 记录在 UDP 协议头中，然后从 UDP 包中获取本机 IP

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 53))
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

SSR_Url = str(GetSsrUrl())

def GreenText(string):
    print("\033[32m")
    print("%s") % string
    print("\033[0m")

print("\n")
print("==================== SSR 配置链接 ====================")
print("    你可以复制以下链接分享给你的设备和朋友们使用了！  ")
GreenText(SSR_Url)

# 获得客户端二维码

def genQR_Code(ssr_url):
    qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=1)
    qr.add_data(ssr_url)
    qr.make(fit=True)
    img = qr.make_image()
    img.save("/root/ssr_qrcode.png")

genQR_Code(SSR_Url)
print("======== SSR 二维码已生成并存储在系统根目录！========")
