#!/usr/bin/python
# -*- coding: UTF-8 -*-

s="hello world"
print s.capitalize()

print s.replace("hello","good")

x='1231231231323'
print x.replace('1','x',3)

ip="192.168.1.1"
l=ip.split('.',3)
print l[0]

import string    #引入模块
#print string.replace(s,'hello','good')


def f(x):
    if x>5:
        return True


print f(10)
l=range(10)
print filter(f, l) #过滤


