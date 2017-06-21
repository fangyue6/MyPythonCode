# -*- coding:utf-8 -*-
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
n = 3
for i in range(n):
    r.append(L[i])
print r

print L[0:3] #Slice
print L[1:5]
print L[-2:]
print L[-2:-1]

L = range(100)
print L[:10]
print L[-10:]
print L[:10:2] #前10个数，每两个取一个：'''
print L[::5]   #所有数，每5个取一个：
print 'ABCDEFG'[::2]