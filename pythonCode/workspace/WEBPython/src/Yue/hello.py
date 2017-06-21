#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月14日

@author: fangyue
'''
#HTTP请求的所有输入信息都可以通过environ获得
#start_response：一个发送HTTP响应的函数。
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')