#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月13日

@author: fangyue
'''

class MyDataWithMethod(object): # 定义类
    def printFoo(self): # 定义方法
        print 'You invoked printFoo()!'
        
myObj = MyDataWithMethod() # 创建实例

myObj.printFoo()


class AddrBookEntry(object): # 类定义
    'address book entry class'
    def __init__(self, nm, ph): # 定义构造器
        self.name = nm # 设置 name
        self.phone = ph # 设置 phone
        print 'Created instance for:', self.name
    def updatePhone(self, newph): # 定义方法
        self.phone = newph
        print 'Updated phone# for:', self.name
    def show(self):
        print 'name=',self.name
        print 'phone=',self.phone
        
john = AddrBookEntry('John Doe', '408-555-1212') #为John Doe 创建实例
john.show() 
john.updatePhone('15071098074')
john.show()

"""继承AddrBookEntry类"""
class EmplAddrBookEntry(AddrBookEntry):
    'Employee Address Book Entry class'#员工地址本类
    def __init__(self, nm, ph, id, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em
    def updateEmail(self, newem):
        self.email = newem
        print 'Updated e-mail address for:', self.name
johnimpl=EmplAddrBookEntry('John Doe', '408-555-1212',42, 'john@spam.doe')
johnimpl.show()










