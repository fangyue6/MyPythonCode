#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月9日

@author: fangyue
'''

#浅拷贝 深拷贝


a=[1,2,3,'a','b','c']
b=a

a.append('d')
print a
print b

b.append('e')
print a
print b

import copy
c=[1,2,3,['a','b','c']]
d=copy.copy(c)#浅拷贝
print c
print d
print id(c)
print id(d)



c.append('d')
print "c.append('d')"
print c
print d
print id(c)
print id(d)

e=copy.deepcopy(c)#深拷贝
print id(c[3])
print id(e[3])
c[3].append('sss')
print c
print e
