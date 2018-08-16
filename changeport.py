#! /usr/bin/env python
# -*- coding: utf-8 -*-
import ssrextra
import readjson
import writejson
from ssrextra import is_number

# 主程序

print ("当前主端口为：%s") % str(readjson.ConfPort)
print ("生成随机端口 (r) 还是自定义端口 (m)：")
ifgenport = raw_input()

if ifgenport == "r" or ifgenport == '':
    newport=ssrextra.Port(10000, 65535)
    writejson.WritePort(newport)
    print("新的端口为：%s") % newport
elif ifgenport == "m":
    print ("请输入新端口：")
    newport = raw_input()
    if (is_number(newport)) and int(newport) >= 0 and int(newport) <= 65535:
	writejson.WritePort(newport)
        print("新的端口为：%s") % newport
    else:
	print("输入错误，请输入 1 至 65535 之间的数字！")
else:
    print("输入不正确，请输入 r 或 m")
