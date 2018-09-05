#! /usr/bin/env python
# -*- coding: utf-8 -*-
from readjson import ConfMethod
import writejson
from ssrextra import (is_number, Whether, runpy, runshell, Show_conf)

cm="changemethod"

Show_conf("当前加密方式", ConfMethod)
print ("按数字键选择加密方法")
print ("")
print ("0.返回上一级")
print ("1.none")
print ("2.aes-256-cfb")
print ("3.aes-256-cfb8")
print ("4.aes-256-ctr")
print ("5.bf-cfb")
print ("6.camellia-256-cfb")
print ("7.cast5-cfb")
print ("8.chacha20-ietf")
print ("9.chacha20")
print ("10.xchacha20")
print ("11.salsa20")
print ("12.xsalsa20")
print ("13.idea-cfb")
print ("14.seed-cfb")
print ("15.rc4-md5")
print ("16.rc4-md5-6")
print ("17.table")
newmethod = raw_input()

if ( not is_number(newmethod) ):
    print ("输入错误，请检查你输入的内容！")
    runpy(cm)
else:
    if (newmethod=="0"):
        runshell("/usr/local/bin/ssr", "change_config")
    elif (newmethod=="1"):
	writejson.WriteMethod("none")
	Whether("该模式适合搭配 auth_chain 和 auth_akarin 系列协议使用，是否要选择？(y/n)", "y", "n", writejson.WriteMethod, "加密方式", "none", "加密方式选择", cm)
    elif (newmethod=="2"):
	Whether("该模式可能影响低功耗设备（手机、路由器）的性能，是否选择？(y/n)", "y", "n", writejson.WriteMethod, "加密方式", "aes-256-cfb", "加密方式选择", cm)
    elif (newmethod=="3"):
        Whether("该模式可能影响低功耗设备（手机、路由器）的性能，是否选择？(y/n)", "y", "n", writejson.WriteMethod, "加密方式", "aes-256-cfb8", "加密方式选择", cm)
    elif (newmethod=="4"):
        Whether("该模式可能影响低功耗设备（手机、路由器）的性能，是否选择？(y/n)", "y", "n", writejson.WriteMethod, "加密方式", "aes-256-ctr", "加密方式选择", cm)
    elif (newmethod=="5"):
        writejson.WriteMethod("bf-cfb")
        Show_conf("新的加密方式", "bf-cfb")
    elif (newmethod=="6"):
	Whether("该模式可能不支持移动设备，是否选择？(y/n)", "y", "n", writejson.WriteMethod, "加密方式", "camellia-256-cfb", "加密方式选择", cm)
    elif (newmethod=="7"):
	Whether("该模式可能不支持移动设备，是否选择？(y/n)", "y", "n", writejson.WriteMethod, "加密方式", "cast5-cfb", "加密方式选择", cm)
    elif (newmethod=="8"):
        writejson.WriteMethod("chacha20-ietf")
        Show_conf("新的加密方式", "chacha20-ietf")
    elif (newmethod=="9"):
        writejson.WriteMethod("chacha20")
        Show_conf("新的加密方式", "chacha20")
    elif (newmethod=="10"):
	Whether("该模式可能不支持移动设备，是否选择？(y/n)", "y", "n", writejson.WriteMethod, "加密方式", "xchacha20", "加密方式选择", cm)
    elif (newmethod=="11"):
        writejson.WriteMethod("salsa20")
        Show_conf("新的加密方式", "salsa20")
    elif (newmethod=="12"):
	Whether("该模式可能不支持移动设备，是否选择？(y/n)", "y", "n", writejson.WriteMethod, "加密方式", "xsalsa20", "加密方式选择", cm)
    elif (newmethod=="13"):
        writejson.WriteMethod("idea-cfb")
        Show_conf("新的加密方式", "idea-cfb")
    elif (newmethod=="14"):
        writejson.WriteMethod("seed-cfb")
        Show_conf("新的加密方式", "seed-cfb")
    elif (newmethod=="15"):
	Whether("该加密方式强度不够，容易被破解，是否要选择？(y/n)", "y", "n", writejson.WriteMethod, "加密方式", "rc4-md5", "加密方式选择", cm)
    elif (newmethod=="16"):
        writejson.WriteMethod("rc4-md5-6")
        Show_conf("新的加密方式", "rc4-md5-6")
    elif (newmethod=="17"):
        writejson.WriteMethod("table")
        Show_conf("新的加密方式", "table")
    else:
	print("请按 1 到 17 之间的数字！")
        runpy(cm)
