#!/usr/bin/python
#coding:gbk
from __future__ import division
print 5/2
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

operator1={"+":add,"-":jian,"*":cheng,"/":chu}

def f(x,o,y):
	return operator1.get(o)(x,y)
print operator1["+"](3,2)
print operator1.get("*")(4,5)
print f(12,'*',34)	

print operator(2,'/',4)
