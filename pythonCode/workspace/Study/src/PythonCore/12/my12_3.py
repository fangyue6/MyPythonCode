#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月13日

@author: fangyue
'''
'''12.3.3 无限制的名称空间'''
def foo():
    pass
foo.__doc__='Oops, forgot to add doc str above!'
foo.version = 0.2

class MyUltimatePythonStorageDevice(object):
    pass

bag=MyUltimatePythonStorageDevice()
bag.x=100
bag.y=200
bag.version=01
bag.completed=False

print bag.x





