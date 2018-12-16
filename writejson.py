#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os, json, readjson

# 打开配置文件
jsonfile = file("/etc/shadowsocks.json")
config = json.load(jsonfile)

# 写入配置文件
def Write():
    myjsondump=json.dumps(config,indent=4) # json.dumps方法用于将对象格式化成json，indent定义了缩进
    openjsonfile=file("/etc/shadowsocks.json","w+") # file方法用于打开文件，w+参数表示可读写
    openjsonfile.writelines(myjsondump) # writelines方法用于向文件写入一个序列字符串列表
    openjsonfile.close() # close方法表示关闭文件。关闭后文件不能再进行读写操作。

# 写入密码函数
def WritePwd(mypwd):
    config[u"password"]=str(mypwd)
    Write()

# 写入端口函数
def WritePort(myport):
    config[u"server_port"]=int(myport)
    Write()

# 写入加密方式函数
def WriteMethod(mymtd):
    config[u"method"]=str(mymtd)
    Write()

# 写入传输协议函数
def WriteProtocol(myptc):
    config[u"protocol"]=str(myptc)
    Write()

# 写入混淆模式函数
def WriteObfs(myobfs):
    config[u"obfs"]=str(myobfs)
    Write()

# 写入重定向参数函数 
def WriteRedirect(myrdt): 
    config[u"redirect"]=list(myrdt) 
    Write()
