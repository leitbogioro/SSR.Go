#! /usr/bin/env python
# -*- coding: utf-8 -*-
from readjson import ConfRedirect
import writejson
from ssrextra import (Show_conf, is_number, runpy, runshell)

print ("须知：设置重定向，意味着当来访请求不符合 ShadowSocksR 数据包类型的时候，ShadowSocksR 会自动将该请求
重定向到另一个本机的或其他域的空间。")
Show_conf("当前重定向参数", ConfRedirect)
print ("请选择你想执行的操作：")
print ("")
print ("0.返回上一级")
print ("1.指定访问本地的某端口重定向到哪个网站")
print ("2.一键将访问本地的80、443端口重定向到某网站")
print ("3.一键将访问本地的80、443端口重定向到本机某端口")
newredirect = raw_input()
