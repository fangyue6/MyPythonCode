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

def machine(x=3,y="ţ��"):
	print "����һ��",x,"Ԫ",y,"��ζ��***"
def machine1(y,x=3):
	print "1111����һ��",x,"Ԫ",y,"��ζ��***"
machine(y="��ݮ")
machine1("��ݮ")