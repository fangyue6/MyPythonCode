#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月9日

@author: fangyue
'''
try:
    f= open('2.py')
    print 1/0
except  IOError,msg:
    print '打开文件出错啦'
except ZeroDivisionError,msg:
    print 'ZeroDivisionError'
finally:
    f.close

if 1>0:
    raise TypeError("nothing !!!!!!")
    