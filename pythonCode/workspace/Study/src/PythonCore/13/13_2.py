#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月13日

@author: fangyue
'''
class MyClass(object):
    'MyClass class definition' #MyClass 类定义
    myVersion = '1.1' # static data 静态数据
    def showMyVersion(self): # method 方法
        print MyClass.myVersion    
        
print dir(MyClass)
print MyClass.__dict__


'''13.5.4 __del__() "解构器"方法'''
class InstCt(object):
    count = 0 # count is class attr count 是一个类属性
    def __init__(self): # increment count 增加count
        InstCt.count += 1
    def __del__(self): # decrement count 减少count
        InstCt.count -= 1
    def howMany(self): # return count 返回count
        return InstCt.count
a = InstCt()
b = InstCt()
print b.howMany()
print a.howMany()
del b
print a.howMany()
del a
print InstCt.count



'''13.6.5 实例属性 vs 类属性'''
class C(object): # define class 定义类
    version = 1.2 # static member 静态成员
c = C() # instantiation 实例化
print C.version # access via class 通过类来访问
print c.version # access via instance 通过实例来访问

C.version += 0.1 # update (only) via class 通过类（只能这样）来更新
print C.version # access via class 通过类来访问
print c.version # access via instance 通过实例来访问

c.version+=0.2
print C.version # access via class 通过类来访问   1.3
print c.version # access via instance 通过实例来访问  1.5



