#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月9日

@author: fangyue
'''

fo=open('../file/test.txt','a+')
fo.write("嘻嘻嘻\n")
#print fo.read()#读取
fo.close#关闭

f1=file('../file/test.txt','a+')
f1.write("呵呵\n")
f1.close()
f1=file('../file/test.txt','a+')
print f1.read()









