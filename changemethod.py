#! /usr/bin/env python
# -*- coding: utf-8 -*-
import readjson
import writejson
import ssrextra
from ssrextra import is_number
from ssrextra import Whether

print ("Current encryption method is: %s") % str(readjson.ConfMethod)
print ("Please choose a new method: ")
print ("1.none")
print ("2.aes-256-cfb")
print ("3.aes-256-cfb8")
print ("4.aes-256-ctr")
print ("5.bf-cfb")
print ("6.camellia-256-cfb")
print ("7.cast5-cfb")
print ("8.chacha20-ietf")
print ("9.chacha20")
print ("10.xchacha20")
print ("11.salsa20")
print ("12.xsalsa20")
print ("13.idea-cfb")
print ("14.seed-cfb")
print ("15.rc4-md5")
print ("16.rc4-md5-6")
print ("17.table")
newmethod = raw_input()

if ( not is_number(newmethod) ):
    print ("Input error, please try it again! ")
    exit
else:
    if (newmethod=="1"):
	writejson.WriteMethod("none")
	Whether("This model is suitable with auth_chain / auth_akarin, 	surely it? (y/n)", "y", "n", writejson.WriteMethod, "encryption method", "none", "choose encryption method")
    elif (newmethod=="2"):
	Whether("This model may cause bad performance of low-power device(smartphone, wireless-router etc), surely it? (y/n)", "y", "n", writejson.WriteMethod, "encryption method", "aes-256-cfb", "choose encryption method")
    elif (newmethod=="3"):
        Whether("This model may cause bad performance of low-power device(smartphone, wireless-router etc), surely it? (y/n)", "y", "n", writejson.WriteMethod, "encryption method", "aes-256-cfb8", "choose encryption method")
    elif (newmethod=="4"):
        Whether("This model may cause bad performance of low-power device(smartphone, wireless-router etc), surely it? (y/n)", "y", "n", writejson.WriteMethod, "encryption method", "aes-256-ctr", "choose encryption method")
    elif (newmethod=="5"):
        writejson.WriteMethod("bf-cfb")
    elif (newmethod=="6"):
	Whether("This model may not support low-power device(smartphone, wireless-router etc), surely it? (y/n)", "y", "n", writejson.WriteMethod, "encryption method", "camellia-256-cfb", "choose encryption method")
    elif (newmethod=="7"):
	Whether("This model may not support low-power device(smartphone, wireless-router etc), surely it? (y/n)", "y", "n", writejson.WriteMethod, "encryption method", "cast5-cfb", "choose encryption method")
    elif (newmethod=="8"):
        writejson.WriteMethod("chacha20-ietf")
    elif (newmethod=="9"):
        writejson.WriteMethod("chacha20")
    elif (newmethod=="10"):
	Whether("This model may not support low-power device(smartphone, wireless-router etc), surely it? ", "y", "n", writejson.WriteMethod, "encryption method", "xchacha20", "choose encryption method")
    elif (newmethod=="11"):
        writejson.WriteMethod("salsa20")
    elif (newmethod=="12"):
	Whether("This model may not support low-power device(smartphone, wireless-router etc), surely it? ", "y", "n", writejson.WriteMethod, "encryption method", "xsalsa20", "choose encryption method")
    elif (newmethod=="13"):
        writejson.WriteMethod("idea-cfb")
    elif (newmethod=="14"):
        writejson.WriteMethod("seed-cfb")
    elif (newmethod=="15"):
	Whether("This model's is so weak that may be cracked easily, surely it? (y/n)", "y", "n", writejson.WriteMethod, "encryption method", "rc4-md5", "choose encryption method")
    elif (newmethod=="16"):
        writejson.WriteMethod("rc4-md5-6")
    elif (newmethod=="17"):
        writejson.WriteMethod("table")
    else:
	print("Please input number on keyboard from 1 to 17! ")
