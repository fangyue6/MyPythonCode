#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月13日

@author: fangyue
'''

#globa 语句
is_this_global = 'xyz'
def foo():
    global is_this_global
    this_is_local = 'abc'
    is_this_global = 'def'
    print this_is_local + is_this_global
foo()
print is_this_global

#11.8.4 闭包
def counter(start_at=0): 
    count = [start_at] 
    def incr():
        count[0] += 1
        return count[0]
    return incr

count= counter(5)
print count()#6
print count()#7

count2 = counter(100)
print count2()#101
print count()#8

'''例子11.8 用闭包将函数调用写入日至。 p436'''

s='''11.8.5 作用域和lambda'''
print s
x= 10
def foos():
    y = 5
    bar = lambda y=y:x+y
    print bar(y)
    y=8
    print bar(y)
foos()







