#!/usr/bin/python
#coding:gbk
#coding=utf8
#encoding:utf8
#encoding=utf8
#_*_ coding:utf8 _*_
def fun(x,y):
	if x==y:
		print x,'=',y
	else:
		print x,'!=',y
#x=raw_input("please input:")
#y=raw_input("please input:")
#fun(x,y)

def machine(x=3,y="牛奶"):
	print "生成一个",x,"元",y,"口味的***"
def machine1(y,x=3):
	print "1111生成一个",x,"元",y,"口味的***"
machine(y="草莓")
machine1("草莓")