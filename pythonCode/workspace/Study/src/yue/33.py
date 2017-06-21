#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月9日

@author: fangyue
'''
f1=open('../file/test.txt','a+')
s1=f1.read()
f1.close()
for i in open('../file/test.txt','a+'):
    print i
    
      
f1=open('../file/test.txt','a+')
print f1.readlines()#返回行列表
f1.close()

f1=open('../file/test.txt','a+')
f1.next()
f1.close

l=['one\n','two\n','three\n']
f1=open('../file/test.txt','a+')
f1.writelines(l)
f1.close

print "*"*50
f1=open('../file/test.txt','r+')
print f1.read()
f1.seek(0,0)#从头开始
f1.seek(0,2)#光标移动到末尾
l=['one1\n','two1\n','three1\n']
f1.writelines(l)
f1.flush()#提交更新
f1.seek(0,0)
print f1.read()









