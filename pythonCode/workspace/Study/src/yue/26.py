#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月9日

@author: fangyue
'''

'''正则表达式'''

import re
s=r'abc'
print re.findall(s, "abcaaaabca",0)
st='top tip tap twp tep'
s=r'top'
print re.findall(s, st, 0)  
  
s=r't[oi]p' #包含有tip和top
print re.findall(s, st, 0)

s=r't[^oi]p' #除了有tip和top之外的
print re.findall(s, st, 0)

print '*'*15
st="hello world,hello boy"

r=r'^hello'#匹配以hello开头的
print re.findall(r, st, 0)

r=r'boy$'#匹配以boy结尾的
print re.findall(r, st, 0)

r=r't[abc$]'
print re.findall(r, 'tax$', 0)

r=r'x[0-9]x'
print re.findall(r, 'x6x', 0)

r=r'x[0-9A-Za-z]+x'
print re.findall(r, 'xzzzzx', 0)

