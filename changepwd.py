#! /usr/bin/env python
# -*- coding: utf-8 -*-
import ssrextra
import readjson
import writejson

print ("当前密码为：%s") % str(readjson.ConfPwd)
print ("是否要随机生成一个新的密码 (y/n)：")
ifgenpwd = raw_input()
def genradompwd(length):
    newpwd=ssrextra.Pwd(length)
    writejson.WritePwd(newpwd)
    print("新的密码为：%s") % newpwd

if ifgenpwd == "y" or ifgenpwd == '':
    genradompwd(16)
elif ifgenpwd=="n":
    print("请输入新密码")
    newpwd = raw_input()
    if newpwd == "":
	print ("密码不可为空")
	genradompwd(16)
    else:
	writejson.WritePwd(newpwd)
	print("新的密码为：%s") % newpwd
else:
    print("输入不正确，请输入 y 或 n")
