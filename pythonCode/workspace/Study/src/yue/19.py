#!/usr/bin/python
#coding:gbk
def f(x):
	print x
def f1(x,y):
	print x,y
def f2(x,y):
	print "%s : %s" % (x,y)#格式化
def f3(name="name",age=0):
	print "name:%s" % name
	print "age :%s" %age
def f4(x,*args):#接收多余的参数 保存在args里面
		print x
		print args
def f5(x,*args,**kwargs):#接收多余的参数 保存在args里面
		print x
		print args
		print kwargs
l=(1,2,3)
f(l)
f({1:11,2:22,'3':33})
f1(l,{1:11,2:22,'3':33})
f2('aaa','bb')
t=('name','yue')
f2(*t)

r=['111','222']
f2(*r)

f3("fang")

print "****************************************"
t=(30,'fang')
d={'age':30,'name':'fang'}
f3(*t)
f3(*d)
f3(**d)

print "*************************************"
f4(1,2,3,l)
f5(1,2,l,d)