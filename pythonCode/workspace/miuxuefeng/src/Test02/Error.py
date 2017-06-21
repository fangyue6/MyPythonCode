#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年5月11日

@author: fangyue
'''
class APIError(StandardError):
    '''
    raise APIError if got failed json message
    '''
    def __init__(self,error_code,error,request):
        self.error_code-error_code
        self.error=error
        self.request=request
        StandardError.__init__(self,error)
    def __str__(self):
        return 'APIError:%s:%s,request:%s(self.error_code,self.error.self.request)'

class APIValueError(StandardError):
    '''
     raise APIValueError if got failed  message
    '''
    def __init__(self,error_code,error,request):
        self.error_code-error_code
        self.error=error
        self.request=request
        StandardError.__init__(self,error)
    def __str__(self):
        return 'APIError:%s:%s,request:%s(self.error_code,self.error.self.request)'