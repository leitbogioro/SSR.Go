#! /usr/bin/env python
# -*- coding: utf-8 -*-
from readjson import ConfObfs
import writejson
from ssrextra import (is_number, Whether, runpy, runshell, Show_conf)

co="changeobfs"

Show_conf("当前混淆模式", ConfObfs)
print ("按数字键选择混淆模式")
print ("")
print ("0.返回上一级")
print ("1.plain")
print ("2.http_simple")
print ("3.http_simple_compatible")
print ("4.http_post")
print ("5.http_post_compatible")
print ("6.tls1.2_ticket_auth")
print ("7.tls1.2_ticket_auth_compatible")
print ("8.tls1.2_ticket_fastauth")
print ("9.tls1.2_ticket_fastauth_compatible")
print ("10.random_head")
newobfs = raw_input()

if ( not is_number(newobfs) ):
    print ("输入错误，请确保你的输入内容正确！")
    runpy(co)
else:
    if (newobfs=="0"):
        runshell("/usr/local/bin/ssr", "change_config")
    elif (newobfs=="1"):
        Whether("该模式表示不做任何混淆，无论配合何种协议，在内卷国大部分地区都会被运营商直接阻断，是否要选择？(y/n)", "y", "n", writejson.WriteObfs, "混淆", "plain", "混淆选择", co)
    elif (newobfs=="2"):
        Whether("该模式仅制造一次 GET 请求和回应包，中途依旧不采用混淆模式通信，建议配合最新协议使用，是否要选择？(y/n)", "y", "n", writejson.WriteObfs, "混淆", "http_simple", "混淆选择", co)
    elif (newobfs=="3"):
        Whether("该模式的作用和 http_simple 一致，可兼容原版 shadowsocks 协议，是否要选择？(y/n)", "y", "n", writejson.WriteObfs, "混淆", "http_simple_compatible", "混淆选择", co)
    elif (newobfs=="4"):
        Whether("该模式的作用和 http_simple 类似，区别在于制造的是 POST 请求头，建议配合最新协议使用，是否要选择？(y/n)", "y", "n", writejson.WriteObfs, "混淆", "http_post", "混淆选择", co)
    elif (newobfs=="5"):
        Whether("该模式的作用和 http_simple 一致，可兼容原版 shadowsocks 协议，是否要选择？(y/n)", "y", "n", writejson.WriteObfs, "混淆", "http_post_compatible", "混淆选择", co)
    elif (newobfs=="6"):
        Whether("此项默认推荐，但在 ssr 被 GFW 大规模针对的今天，过度伪装反而可能会把自己更精准地暴露给敌人，是否要选择？(y/n)", "y", "n", writejson.WriteObfs, "混淆", "tls1.2_ticket_auth", "混淆选择", co)
    elif (newobfs=="7"):
        Whether("该模式的作用和 tls1.2_ticket_auth 一致，可兼容原版 shadowsocks 协议，是否要选择？(y/n)", "y", "n", writejson.WriteObfs, "混淆", "tls1.2_ticket_auth_compatible", "混淆选择", co)
    elif (newobfs=="8"):
        Whether("该模式和 tls1.2_ticket_auth 区别是，它不会等待服务端的响应，可有效降低延迟，是否要选择？(y/n)", "y", "n", writejson.WriteObfs, "混淆", "tls1.2_ticket_fastauth", "混淆选择", co)
    elif (newobfs=="9"):
        Whether("该模式的作用和 tls1.2_ticket_fastauth 一致，可兼容原版 shadowsocks 协议，是否要选择？(y/n)", "y", "n", writejson.WriteObfs, "混淆", "tls1.2_ticket_fastauth_compatible", "混淆选择", co)
    elif (newobfs=="10"):
        Whether("该模式通讯前会发送随机数据包，但包的末尾特征明显，容易被防火长城干扰，之后是协议数据流，是否要选择？(y/n)", "y", "n", writejson.WriteObfs, "混淆", "random_head", "混淆选择", co)
    else:
	print("请按 1 到 10 之间的数字！")
        runpy(co)
