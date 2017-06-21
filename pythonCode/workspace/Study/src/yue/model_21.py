#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月9日

@author: fangyue
'''
from __future__ import division
def add(x,y):
    return x+y
def jian(x,y):
    return x-y
def cheng(x,y):
    return x*y
def chu(x,y):
    return x/y
def operator(x,o,y):
    if o=="+":
        return add(x,y)
    elif o=="-":
        return jian(x,y)
    elif o=="*":
         return cheng(x,y)
    elif o=="/":
         return chu(x,y)
    else :
        pass
def f(x,o,y):
    return operator1.get(o)(x,y)
operator1={"+":add,"-":jian,"*":cheng,"/":chu}

if __name__ =="__main__":
    print operator1["+"](3,2)
    print operator1["+"](3,2)
    print operator1.get("*")(4,5)
    print f(12,'*',34)    
    print operator(2,'/',4)




