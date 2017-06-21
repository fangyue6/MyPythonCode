#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月10日

@author: fangyue
'''
'''
文件模式 操作
r 以读方式打开
rU 或 Ua 以读方式打开, 同时提供通用换行符支持 (PEP 278)
w 以写方式打开 (必要时清空)
a 以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+ 以读写模式打开
w+ 以读写模式打开 (参见 w )
a+ 以读写模式打开 (参见 a )
rb 以二进制读模式打开
wb 以二进制写模式打开 (参见 w )
ab 以二进制追加模式打开 (参见 a )
rb+ 以二进制读写模式打开 (参见 r+ )
wb+ 以二进制读写模式打开 (参见 w+ )
ab+ 以二进制读写模式打开 (参见 a+ )
a. Python 2.3 中新增
'''

def fun1():
    filename = raw_input('Enter file name: ')
    f = open(filename, 'r')
    for eachLine in f:
        print eachLine,#print 语句默认在输出内容末尾后加一个换行符, 而在语句后加一个逗号就可以避免这个行为
    f.close()

import os
def write():
    filename = raw_input('Enter file name: ')
    fobj = open(filename, 'w')
    while True:
        aLine = raw_input("Enter a line ('.' to quit): ")
        if aLine != ".":
            fobj.write('%s%s' % (aLine, os.linesep))
        else:
            print "输出结束"
            break
            
    fobj.close()
#write()

def fun2():
    f=open('aaa.txt','w+')
    print f.tell()
    print f.write('test line 1\n') # 加入一个长为12 的字符串 [0-11]
    print f.tell()
    print f.write('test line 2\n') # 加入一个长为12 的字符串 [12-23]
    print f.tell() # 告诉我们当前的位置
    print f.seek(-12, 1) # 向后移12 个字节
    print f.tell() # 到了第二行的开头
    print f.readline()
    print f.seek(0, 0) # 回到最开始
    print f.seek(0, 0) # 回到最开始
    print f.readline()
    print f.tell() # 又回到了第二行
    print f.readline()
    print f.tell() # 又到了结尾
    print f.close() # 关闭文件
fun2()



