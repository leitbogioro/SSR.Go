#! /usr/bin/env python
# -*- coding: utf-8 -*-
from readjson import ConfPwd
import writejson
from ssrextra import (Pwd, Show_conf)

def genradompwd(length):
    newpwd=Pwd(length)
    writejson.WritePwd(newpwd)
    Show_conf("新的密码", newpwd)

Show_conf("当前密码", ConfPwd)
print ("是否要随机生成一个新的密码 (y/n)：")
ifgenpwd = raw_input()

if ifgenpwd == "y" or ifgenpwd == '':
    genradompwd(16)
elif ifgenpwd=="n":
    print("请输入新密码")
    newpwd = raw_input()
    if newpwd == "":
	print ("密码不可为空")
        print ("")
	genradompwd(16)
    else:
	writejson.WritePwd(newpwd)
	Show_conf("新的密码", newpwd)
else:
    print("输入不正确，请输入 y 或 n")
