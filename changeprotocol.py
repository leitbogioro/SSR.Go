#! /usr/bin/env python
# -*- coding: utf-8 -*-

import readjson
import writejson
import ssrextra
from ssrextra import is_number
from ssrextra import Whether

print ("Current transmission protocol: %s") % str(readjson.ConfProtocol)
print ("Please choose a new protocol: ")
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
    print ("Input error, please try it again!")
    exit
else:
    if (newprotocol=="1"):
	Whether("This protocol cames from original ShadowSocks and it cannot suitable with contemporary internet censorship, surely it? (y/n)", "y", "n", writejson.WriteProtocol, "protocol", "origin", "choose protocol")
    elif (newprotocol=="2"):
	Whether("This protocol's compression and decompression are so ineffective that it will cause a higher CPU occupy, surely it? (y/n)", "y", "n", writejson.WriteProtocol, "protocol", "verify_deflate", "choose protocol")
    elif (newprotocol=="3"):
	Whether("This protocol cannot resistant GFW's replay attack so I don't recommend it, surely it? (y/n)", "y", "n", writejson.WriteProtocol, "protocol", "auth_sha1_v4", "choose protocol")
    elif (newprotocol=="4"):
	Whether("This protocol cannot resistant GFW's replay attack so I don't recommend it, surely it? (y/n)", "y", "n", writejson.WriteProtocol, "protocol", "auth_sha1_v4_compatible", "choose protocol")
    elif (newprotocol=="5"):
	Whether("This protocol can attacked by GFW rapidly so I don't recommend it, surely it? (y/n)", "y", "n", writejson.WriteProtocol, "protocol", "auth_aes128_md5", "choose protocol")
    elif (newprotocol=="6"):
	Whether("This protocol can attacked by GFW rapidly so I don't recommend it, surely it? (y/n)", "y", "n", writejson.WriteProtocol, "protocol", "auth_aes128_sha1", "choose protocol")
    elif (newprotocol=="7"):
        Whether("This protocol can attacked by GFW rapidly so I don't recommend it, surely it? (y/n)", "y", "n", writejson.WriteProtocol, "protocol", "auth_chain_a", "choose protocol")
    elif (newprotocol=="8"):
        writejson.WriteProtocol("auth_chain_b")
	print("New protocol is auth_chain_b")
    elif (newprotocol=="9"):
	Whether("This protocol will cause a failure telecommunication between server and client, surely it? (y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_chain_c", "协议选择")
    elif (newprotocol=="10"):
	Whether("This protocol is only supported by Windows and Android client, surely it? (y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_chain_d", "协议选择")
    elif (newprotocol=="11"):
        Whether("This protocol is only supported by Windows and Android client, surely it? (y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_chain_e", "协议选择")
    elif (newprotocol=="12"):
	Whether("This protocol is only supported by Windows and Android client, surely it? (y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_chain_f", "协议选择")
    elif (newprotocol=="13"):
	Whether("This is an experiment protocol so it can only support Windows client except movement client and also included by Mac OS, surely it? (y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_akarin_rand", "协议选择")
    elif (newprotocol=="14"):
        Whether("This is an experiment protocol so it can only support Windows client except movement client and also included by Mac OS, surely it? (y/n)", "y", "n", writejson.WriteProtocol, "协议", "auth_akarin_spec_a", "协议选择")
    else:
	print("Please input number on keyboard from 1 to 14!")
