#! /usr/bin/env python
# -*- coding: utf-8 -*-

import readjson
import writejson
import ssrextra
from ssrextra import is_number
from ssrextra import Whether

print ("Current obfs model is: %s") % str(readjson.ConfObfs)
print ("Please choose a new obfs:")
print ("1.plain")
print ("2.http_simple")
print ("3.http_simple_compatible")
print ("4.http_post")
print ("5.http_post_compatible")
print ("6.tls1.2_ticket_auth")
print ("7.tls1.2_ticket_auth_compatible")
print ("8.tls1.2_ticket_fastauth")
print ("9.tls1.2_ticket_fastauth_compatible")
print ("10.random_head")
newobfs = raw_input()

if ( not is_number(newobfs) ):
    print ("Input error, please try it again!")
    exit
else:
    if (newobfs=="1"):
        Whether("This model mean no obfs, I recommend you to use it with latest protocol, surely it? (y/n)", "y", "n", writejson.WriteObfs, "obfs", "plain", "choose obfs")
    elif (newobfs=="2"):
        Whether("This model only build one request and respond package on the begining of the communication and during translate data has no disguise with obfs, surely it? (y/n)", "y", "n", writejson.WriteObfs, "obfs", "http_simple", "choose obfs")
    elif (newobfs=="3"):
        Whether("This model has same utility to http_simple, and it compatible with original edition of ShadowSocks, surely it? (y/n)", "y", "n", writejson.WriteObfs, "obfs", "http_simple_compatible", "choose obfs")
    elif (newobfs=="4"):
        Whether("This model has same utility to http_simple, the difference from them is the latter build a POST request header, I recommend you to use it with latest protocol, surely it? (y/n)", "y", "n", writejson.WriteObfs, "obfs", "http_post", "choose obfs")
    elif (newobfs=="5"):
        Whether("This model has same utility to http_post, and it compatible with original edition of ShadowSocks, surely it? (y/n)", "y", "n", writejson.WriteObfs, "obfs", "http_post_compatible", "choose obfs")
    elif (newobfs=="6"):
        writejson.WriteObfs("tls1.2_ticket_auth")
        print("New obfs model is: tls1.2_ticket_auth")
    elif (newobfs=="7"):
        Whether("This model has same utility to tls1.2_ticket_auth, and it compatible with original edition of ShadowSocks, surely it? (y/n)", "y", "n", writejson.WriteObfs, "obfs", "tls1.2_ticket_auth_compatible", "choose obfs")
    elif (newobfs=="8"):
        Whether("This model has same utility to tls1.2_ticket_auth, the difference from them is the latter doesn't need to wait for response of the server and it can effectively reduce latency, surely it? (y/n)", "y", "n", writejson.WriteObfs, "obfs", "tls1.2_ticket_fastauth", "choose obfs")
    elif (newobfs=="9"):
        Whether("This model has same utility to tls1.2_ticket_fastauth, and it compatible with original edition of ShadowSocks, surely it? (y/n)", "y", "n", writejson.WriteObfs, "obfs", "tls1.2_ticket_fastauth_compatible", "choose obfs")
    elif (newobfs=="10"):
        Whether("This model will send random data package but features of the end random package will be obvious affected by GFW and then translate data, surely it? (y/n)", "y", "n", writejson.WriteObfs, "obfs", "random_head", "choose obfs")
    else:
	print("Please input number on keyboard from 1 to 10! ")
