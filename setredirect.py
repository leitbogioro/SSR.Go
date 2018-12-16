#! /usr/bin/env python
# -*- coding: utf-8 -*-
from readjson import ConfRedirect
import writejson
from ssrextra import (Show_conf, is_number, runpy, runshell)

sr="setredirect"
lh="127.0.0.1"

def ShowRedirect():
    if (ConfRedirect==[]):
        print ("未作配置")
    else:
        index=0
        for item in ConfRedirect:
            Redirect=ConfRedirect[index]
            RedirectSplit=Redirect.split('#')
            RedirectIn=RedirectSplit[0]
            RedirectInSplit=RedirectIn.split(':')
            RedirectInIP=RedirectInSplit[0]
            RedirectInPort=RedirectInSplit[1]
            if ( RedirectInIP=='*' ):
                RedirectInIP='任何'
            RedirectOut=RedirectSplit[1]
            RedirectOutSplit=RedirectOut.split(':')
            RedirectOutIP=RedirectOutSplit[0]
            RedirectOutPort=RedirectOutSplit[1]
            if ( RedirectOutIP==lh or 'localhost' ):
                RedirectOutIP='本地 '
            print ("若来自"+RedirectInIP+RedirectInPort+'端口的请求类型与 ShadowSocksR 不符，则自动跳转到'+RedirectOutIP+RedirectOutPort+' 端口')
            index +=1

print ("")
print ("须知：")
print ("* 设置重定向，意味着当来访的请求不符合 ShadowSocksR 数据包类型的时候，ShadowSocksR 会自动将该请求重定向到另一个本机的或其他域的空间")
print ("* 典型的配置，是将外界访问本机 80、443 端口且不符合以上规则的请求，全部重定向到本机的某个端口，然后由 Nginx 或 Caddy 监听该端口，实现 ShadowSocksR 在网站背后的隐藏或反代功能")
print ("* 由于无法完全确定您使用了何种 Web 服务器，何种配置，本功能仅对 ShadowSocksR 配置文件中的重定向参数进行设置，本来有引入一键安装 Caddy 并申请加密证书的计划，")
print ("  但 Web 服务器的用途广泛，配置、需求不一，为了尽量避免对您的生产环境造成干扰，造成配置絮乱，烦请您后续还要手动在 Web 服务器里做好相应的监听设置，敬请谅解")
print ("* 设置好重定向功能后，ShadowSocksR 的端口会被还原为 443")
print ("")
print ("当前重定向参数为：")
ShowRedirect()
print ("")
print ("请选择你想执行的操作：")
print ("")
print ("0.返回上一级")
print ("1.一键将访问本地的 80、443 端口重定向到本机某端口")
print ("2.取消重定向操作")
pick = raw_input()

if ( not is_number(pick) ):
    print ("输入错误，请检查你输入的内容！")
    runpy(sr)
else:
    if (pick=="0"):
        runshell("/usr/local/bin/ssr", "change_config")
    elif (pick=="1"):
        print ("请输入需要重定向到本机的目标端口：")
        newport = raw_input()
        while not (is_number(newport)) or int(newport) < 0 or int(newport) > 65535:
            print ("输入错误，请输入 1 至 65535 之间的数字！")
            print ("")
            print ("请输入新端口：")
            newport = raw_input()
        Redirect1="*:80#"+lh+":"+newport
        Redirect2="*:443#"+lh+":"+newport
        Redirectlist=[Redirect1, Redirect2]
        writejson.WriteRedirect(Redirectlist)
        print ("操作已完成")
        runpy(sr)
    elif (pick=="2"):
        writejson.WriteRedirect("")
        print ("操作已完成")
        runpy(sr)
    else:
        print ("输入错误，请按 0 到 2 之间的数字！")
        runpy(sr)
