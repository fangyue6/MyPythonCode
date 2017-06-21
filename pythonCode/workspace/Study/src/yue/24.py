#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月9日

@author: fangyue
'''
def f(x):
    if x%2==0:
        return True
def muli(x,y):
    return x*y    
l=range(10)

print filter(f, l)

name=['fang','zou','zhang']
age=[10,20,30]
tel=['15071098070','12345678901','56897564563']
tel1=['15071098070','12345678901','56897564563','55555']

print zip(name,age,tel1) #zip并行遍历时，个数不相同时，取个数最小的

print map(None,name,age,tel1) #map并行遍历时，个数不相同时，个数少的用Nano代替

a=[1,3,5]
b=[2,4,6]
print map(muli,a,b)

#*******************************

l=range(1,101,1)
#n=0
#for i in l:
#    n+=i
#print n    
print reduce(lambda x,y:x+y, l)#逐个取l列表中的数据

l=range(1,11,1)
print reduce(muli, l)#逐个取l列表中的数据

print filter(lambda x:x%2==0, l)










