#! /usr/bin/env python
# -*- coding: utf-8 -*-

import readjson
import writejson
import ssrextra
from ssrextra import is_number
from ssrextra import Whether

print ("当前加密方式为：%s") % str(readjson.ConfProtocol)
print ("请选择新的加密方式：")
print ("1.origin")
print ("2.verify_deflate")
print ("3.auth_sha1_v4")
print ("4.auth_sha1_v4_compatible")
print ("5.auth_aes128_md5")
print ("6.auth_aes128_sha1")
print ("7.auth_chain_a")
print ("8.auth_chain_b")
print ("9.auth_chain_c")
print ("10.auth_chain_d")
print ("11.auth_chain_e")
print ("12.auth_chain_f")
print ("13.auth_akarin_rand")
print ("14.auth_akarin_spec_a")
newprotocol = raw_input()

if ( not is_number(newprotocol) ):
    print ("输入错误，请检查你输入的内容！")
    exit
else:
    if (newprotocol=="1"):
	Whether("该协议来自原生shadowsocks协议，已无法适用于审查严密的环境，是否要选择？(y/n)", "y", "n", writejson.WriteProtocol, "协议", "origin", "协议选择")
    elif (newprotocol=="2"):
	Whether("该协议压缩解压缩效率低，大量用户连接可能会导致 CPU 占用率高，是否要选择？(y/n)", "y", "n", writejson.WriteProtocol, "协议", "verify_deflate", "协议选择")
    elif (newprotocol=="3"):
	Whether("该协议已不可抵御防火长城的重放攻击，不建议使用，是否要选择？(y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_sha1_v4", "协议选择")
    elif (newprotocol=="4"):
	Whether("该协议已不可抵御防火长城的重放攻击，不建议使用，是否要选择？(y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_sha1_v4_compatible", "协议选择")
    elif (newprotocol=="5"):
	Whether("防火长城可迅速探测该协议的特征，不建议使用，是否要选择？(y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_aes128_md5", "协议选择")
    elif (newprotocol=="6"):
	Whether("防火长城可迅速探测该协议的特征，不建议使用，是否要选择？(y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_aes128_sha1", "协议选择")
    elif (newprotocol=="7"):
        Whether("防火长城可迅速探测该协议的特征，不建议使用，是否要选择？(y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_chain_a", "协议选择")
    elif (newprotocol=="8"):
        writejson.WriteProtocol("auth_chain_b")
	print("新的协议为：auth_chain_b")
    elif (newprotocol=="9"):
	Whether("使用该协议偶尔可能会导致与服务端通信失败，是否要选择？(y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_chain_c", "协议选择")
    elif (newprotocol=="10"):
	Whether("该协议仅 Windows 和 Android 客户端支持，是否要选择？(y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_chain_d", "协议选择")
    elif (newprotocol=="11"):
        Whether("该协议仅支持 Windows 客户端，是否要选择？(y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_chain_e", "协议选择")
    elif (newprotocol=="12"):
	Whether("该协议仅支持 Windows 客户端，是否要选择？(y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_chain_f", "协议选择")
    elif (newprotocol=="13"):
	Whether("该协议尚处试验阶段，仅支持 Windows 客户端，暂不支持移动客户端，是否要选择？(y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_akarin_rand", "协议选择")
    elif (newprotocol=="14"):
        Whether("该协议尚处试验阶段，仅支持 Windows 客户端，暂不支持移动客户端，是否要选择？(y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_akarin_spec_a", "协议选择")
    else:
	print("输入错误，请按 1 到 14 之间的数字！")

