#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月9日

@author: fangyue
'''
import os
os.removedirs('test/1/2')
os.mkdir('test')
os.makedirs('test/1/2')

print os.listdir(".")#当前目录
print os.listdir("/")#根目录

print os.getcwd()#获取当前路径

os.chdir('/')#切换根目录
print os.getcwd()#获取当前路径





