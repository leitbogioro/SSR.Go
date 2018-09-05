#! /usr/bin/env python
# -*- coding: utf-8 -*-
import readjson, base64, os, json 
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
print("服务器IP：%s") % IP
print("端口：%s") % Port
print("密码：%s") % Pwd
print("加密方式: %s") % Method
print("传输协议：%s") % Protocol
print("混淆模式：%s") % Obfs

# ssr客户端链接
ssr_url=str(GetSsrUrl(IP, Port, Protocol, Method, Obfs, base64Pwd, SecondPart))

# 绿色字体
def GreenText(string):
    print("\033[32m")
    print("%s") % string
    print("\033[0m")

# 输出信息
print ("")
print ("==================== SSR 配置链接 ====================")
print ("    你可以复制以下链接分享给你的设备和朋友们使用了！  ")
GreenText(ssr_url)

# 生成客户端二维码
genQR_Code(ssr_url, "/root/ssr_qrcode.png")
print ("======== SSR 二维码已生成并存储在系统根目录！=========")
