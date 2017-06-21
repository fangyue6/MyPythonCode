#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月9日

@author: fangyue
'''
import re
r1=r'^\d{3,4}--?\d{8}$'
p_tel=re.compile(r1)#编译后的正则  速度比较快

print p_tel.findall('010-12345678')

csvt_re=re.compile(r'csvt',re.I)#不区分大小写
print csvt_re.findall('CSvt')

x= csvt_re.match('csvt hello')#match判断有值还是没有值
print x.group()

y=csvt_re.search(' hello csvt hello')

z=csvt_re.finditer('hello csvt hello')
z.next()

s='hello csvt'
print s.replace('csvt', 'python')#不支持正则表达式

rs=r'c..t'
print re.sub(rs,'python','csvt caat cvvt cccc')#使用正则来进行替换
print re.subn(rs,'python','csvt caat cvvt cccc')#使用正则来进行替换  可以返回次数

ip='1.2.3.4'
print ip.split('.')#不支持正则

s='123+456-789*000'
print re.split(r'[\+\-\*]', s)#使用正则切割

