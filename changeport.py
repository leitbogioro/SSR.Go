#! /usr/bin/env python
# -*- coding: utf-8 -*-
import ssrextra
import readjson
import writejson
from ssrextra import is_number

# 主程序

print ("Current port is: %s") % str(readjson.ConfPort)
print ("Would you like to generate a new random port (r) or custom it by yourself (m)? ")
ifgenport = raw_input()

if ifgenport == "r" or ifgenport == '':
    newport=ssrextra.Port(10000, 65535)
    writejson.WritePort(newport)
    print("New port is: %s") % newport
elif ifgenport == "m":
    print ("Please pick a new port: ")
    newport = raw_input()
    if (is_number(newport)) and int(newport) >= 0 and int(newport) <= 65535:
	writejson.WritePort(newport)
        print("New port is: %s") % newport
    else:
	print("Input error, please pick a number between 1 and 65535 ! ")
else:
    print("Incorrect input, please press 'r' or 'm'! ")
