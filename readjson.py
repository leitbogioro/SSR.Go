#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os, json
from ssrextra import byteify

# 打开配置文件
jsonfile = file("/etc/shadowsocks.json")
config = json.load(jsonfile)

# 读取传入配置细则
ConfPort=config[u"server_port"]
ConfPwd=config[u"password"]
ConfMethod=config[u"method"]
ConfProtocol=config[u"protocol"]
ConfObfs=config[u"obfs"]
ConfRedirect=config[u"redirect"]
