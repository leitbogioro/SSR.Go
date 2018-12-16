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

