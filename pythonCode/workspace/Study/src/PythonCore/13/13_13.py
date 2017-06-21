#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月13日

@author: fangyue
'''
#13.13.1 简单定制（RoundFloat2）
class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), \
        "Value must be a float!"
        self.value = round(val, 2)
rfm = RoundFloatManual(4.202222)
print rfm.value

# p514
