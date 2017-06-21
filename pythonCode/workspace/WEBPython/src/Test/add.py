#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月14日

@author: fangyue
'''
import math
def is_prime(n):
    i,j,ret=3,2,0
    sum=2
    while j<=n:
        ret=1
        if (j%2)!=0:
            while i<=math.sqrt(j):
                if (j%i)==0:
                    ret=0
                i=i+1
        else :
            ret=0
        if (ret==1):
            sum=sum+j
            print j
        j=j+1
    return sum
def  IsPrime(x)  :
      if x<3:
          return False
      s=long(math.sqrt(x))

      i=2
      while i<=s:
          if (x%i==0):
              print s
              return False
          i+=1
      return True
def show(n):
    i=2
    sum=0
    while i<=n:
        if IsPrime(i):
            sum+=i
            print i
        i+=1
    print "所有质数和为："
    print sum
        
show(30)