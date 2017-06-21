#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月9日

@author: fangyue
'''



#模块
import model_21
print "#"*15+"下面是model_21模块代码"

print model_21.operator1.get('*')(4,5)

import string 
s="hello"
print s.capitalize()#如果自定义模块没有当前函数，则到系统模块下找函数

import test.cal
print test.cal.add_cal(45,56)#调用包

import test.cal as c  #取别名
print c.add_cal(568, 89)

from  test.cal import add_cal#从test包里面导入cal模块中的add_cal方法，可以直接使用
print add_cal(56, 56) 








