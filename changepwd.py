#! /usr/bin/env python
# -*- coding: utf-8 -*-
import ssrextra
import readjson
import writejson

print ("Current password is : %s") % str(readjson.ConfPwd)
print ("Need to generate a new password? (y/n)：")
ifgenpwd = raw_input()
def genradompwd(length):
    newpwd=ssrextra.Pwd(length)
    writejson.WritePwd(newpwd)
    print("New password is: %s") % newpwd

if ifgenpwd == "y" or ifgenpwd == '':
    genradompwd(16)
elif ifgenpwd=="n":
    print("Please input a new password: ")
    newpwd = raw_input()
    if newpwd == "":
	print ("An empty password is not allowed! ")
	genradompwd(16)
    else:
	writejson.WritePwd(newpwd)
	print("New password is: %s") % newpwd
else:
    print("Incorrect input! Please press 'y' or 'n'! ")
