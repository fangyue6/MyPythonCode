#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月9日

@author: fangyue
'''
import re
r=r'^abc'
print re.findall(r, "^abc", 0)

r=r'\^abc'
print re.findall(r, "^abc", 0)

r=r'[0-9]+'
print re.findall(r, "123", 0)

r=r'[\d]+'
print re.findall(r, "123", 0)

r=r'^010-\d{8}$'#010-12345678  以010-开头  \d重复8次
print '\n010-12345678  以010-开头  \d重复8次'
print re.findall(r, "010-123456780", 0)


r=r'ab*'#*将ab重复0次或n次
print '\n*将ab重复0次或n次'
print re.findall(r, "abbaba", 0)

r=r'ab+'#+将ab重复1次或n次
print '\n+将ab重复1次或n次'
print re.findall(r, "abbbbbbba", 0)

r=r'^010-?\d{8}$'#+将ab重复1次或n次
print '\n?表示将前面的符号可有可无'
print re.findall(r, "010-12345678", 0)

r=r'ab+?'#+?将ab进行最小匹配
print '\n+?表示非贪婪模式，匹配最短'
print re.findall(r, "abbbbbbbbb", 0)

r=r'a{1,3}'#{1,3}a重复1到3次
print '\na{1,3}a重复1到3次'
print re.findall(r, "aaa", 0)








