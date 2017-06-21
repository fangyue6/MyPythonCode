#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月10日

@author: fangyue
'''

'''
生成器表达式:
(expr for iter_var in iterable if cond_expr)
'''

data = open('hhga.txt', 'r')
print sum(len(word) for line in data for word in line.split())

rows = [1, 2, 3, 17]
def cols(): # example of simple generator
    yield 56
    yield '*'*56
    yield 1
    
x_product_pairs = ((i, j) for i in rows for j in cols())
for pair in x_product_pairs:
    print pair

#读取文件最长的一行，返回其长度
def read_longest(file):
    f = open(file, 'r')
    longest = 0
    allLines = f.readlines()
    f.close()
    for line in allLines:
        linelen = len(line.strip())
    if linelen > longest:
        longest = linelen
    return longest
def read_longest1(file):
    f = open(file, 'r')
    longest = 0
    allLines = [x.strip() for x in f.readlines()]
    f.close()
    for line in allLines:
        linelen = len(line)
    if linelen > longest:
        longest = linelen
    return longest
def read_longest2(file):
    f = open(file, 'r')
    longest = max(len(x.strip()) for x in f)
    f.close()
    return longest
def read_longest3(file):
    return max(len(x.strip()) for x in open(file))
print read_longest("hhga.txt")
print read_longest1("hhga.txt")
print read_longest2("hhga.txt")
print read_longest3("hhga.txt")