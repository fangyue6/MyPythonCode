#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月10日

@author: fangyue
'''
#列表解析
#[expr for iter_var in iterable]
l= [x**2 for x in range(6)]
for i in l:
    print i
    
    
    
    
print "*"*50
seq = [11, 10, 9, 9, 10, 10, 9, 8, 23, 9, 7, 18, 12, 11, 12]
print filter(lambda x:x%2,seq)
print map(lambda x:x%2,seq)
print [x for x in seq if x%2]

#迭代三维矩阵
print [(x+1,y+1,z+1) for x in range(3) for y in range(5) for z in range(1,101,2)]

#统计hhga.txt中空格的个数
f = open('hhga.txt', 'r')
print len([word for line in f for word in line.split()])

#快速地计算文件大小
import os
print os.stat("hhga.txt").st_size

#把每个单词的长度加起来,
f.seek(0)
print sum([len(word) for line in f for word in line.split()])


