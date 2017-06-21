#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月13日

@author: fangyue
'''


'''11.10.1.简单的生成器特性'''
def ok():
    return 11
def simpleGen():
    yield 1
    yield '2 --> punch!'
    yield ok()
    
myG=simpleGen()
print myG.next()
print myG.next()
print myG.next()
s='''使用一个for 循环而不是手动迭代穿过一个生成器'''
print s
for eachItem in simpleGen():
    print eachItem







