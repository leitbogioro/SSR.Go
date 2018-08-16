#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
import string

# 生成随机密码

# python3中为string.ascii_letters,而python2下则可以使用string.letters和string.ascii_letters

def Pwd(length):
    salt = '!@#$%^&*()><?'
    chars=string.ascii_letters+string.digits+salt
    return ''.join([random.choice(chars) for i in range(length)]) # 得出的结果中字符会有重复的
    # return ''.join(random.sample(chars, 16))#得出的结果中字符不会有重复的
if __name__=="__main__":
    # 密码的长度为16
    print GenPassword(length)

# 生成随机区间数（端口）

def Port(port1, port2):
        return(random.randint(port1, port2))

# 判断是否为数字的函数（ulits）

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

# 协议、加密方式、混淆模式函数

def Whether(ask, c1, c2, config, describe ,item, cancel):
    print(ask)
    pick = raw_input()
    if pick == c1 or pick == '':
        config(item)
	print("新的"+ describe + "为：%s") % item
    elif pick == c2:
        print("已取消" + cancel + ",未执行任何操作")
    else:
        print("输入不正确，请输入 " + c1 + " 或 " + c2)

