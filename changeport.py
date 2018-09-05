#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
from readjson import ConfPort
import writejson
from ssrextra import (is_number, Port, Show_conf)

# 主程序
Show_conf("当前端口", ConfPort)
print ("生成随机端口 (r) 还是自定义端口 (m)：")
ifgenport = raw_input()
functype = re.search('[RrMm]', ifgenport)

while not functype:
    print ("输入不正确，请输入 r 或 m")
    print ("生成随机端口 (r) 还是自定义端口 (m)：")
    ifgenport = raw_input()
    functype = re.search('[RrMm]', ifgenport)
if ifgenport == "r" or ifgenport == "R":
    newport=Port(10000, 65535)
    writejson.WritePort(newport)
    Show_conf("新的端口", newport)
else:
    print ("请输入新端口：")
    newport = raw_input()
    while not (is_number(newport)) or int(newport) < 0 or int(newport) > 65535:
        print ("输入错误，请输入 1 至 65535 之间的数字！")
        print ("")
        print ("请输入新端口：")
        newport = raw_input()
    writejson.WritePort(newport)
    Show_conf("新的端口", newport)
