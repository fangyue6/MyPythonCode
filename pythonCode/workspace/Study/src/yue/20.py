#!/usr/bin/python
#coding:gbk
def f(x,y):
	return x*y
def f1(n):
	if n>0:
		return n*f1(n-1)
print f(2,3)
g=lambda x,y:x*y  #��������
print g(2,3)


print "******************************************* "
def f2(x,y):
	return x*y
L=range(1,6)
print reduce(f2,L)#�����б�����ݽ��в���
print reduce(lambda x,y:x*y,L)