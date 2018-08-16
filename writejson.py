#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import readjson

# 打开配置文件
jsonfile = file("/etc/shadowsocks.json")
config = json.load(jsonfile)

# 写入配置文件
def Write():
    myjsondump=json.dumps(config,indent=4) # json.dumps方法用于将对象格式化成json，indent定义了缩进
    openjsonfile=file("/etc/shadowsocks.json","w+") # file方法用于打开文件，w+参数表示可读写
    openjsonfile.writelines(myjsondump) # writelines方法用于向文件写入一个序列字符串列表
    openjsonfile.close() # close方法表示关闭文件。关闭后文件不能再进行读写操作。

# 更改密码
def WritePwd(mypwd):
    config[u"password"]=str(mypwd)
    Write()

# 更改端口
def WritePort(myport):
    config[u"server_port"]=int(myport)
    Write()

# 更改加密方式
def WriteMethod(mymethod):
    config[u"method"]=str(mymethod)
    Write()

# 更改传输协议
def WriteProtocol(myprotocol):
    config[u"protocol"]=str(myprotocol)
    Write()

# 更改混淆模式
def WriteObfs(myobfs):
    config[u"obfs"]=str(myobfs)
    Write()

