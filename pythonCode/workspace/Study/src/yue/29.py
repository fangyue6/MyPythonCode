#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月9日

@author: fangyue
'''

import re
r1=r'csvt.net'
print re.findall(r1, 'csvt.net')
print re.findall(r1, 'csvtonet')
print re.findall(r1, 'csvtxnet')
print re.findall(r1, 'csvt\nnet',re.S)#使.匹配包括换行在内的所有字符
s="""
    hello csvt
    hello python
    hello fang
    csvt hello
    """
r1=r'^csvt'

print re.findall(r1,s,re.M)#

tel=r"""
    /d{3,4}
    -?
    \d{8}
"""
print re.findall(tel,'010-01234567',re.X)


#分组
print "*"*15+'分组()'
email =r"\w{3}@\w+(\.com|\.cn)" 
print re.match(email,'zz@ssd.com')
print re.findall(email, 'zz@ssd.com')

s="""
    sss src=www ssdc dsfd  dsaa hello src=baidu yes
    src=xinlang
    sdkl   yes
    df
    g hello src=sss yes
  """
r1=r"hello src=(.+) yes"#分组
print re.findall(r1, s)

