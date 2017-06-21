#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年5月9日

@author: fangyue
'''
import functools
import json  
from web import ctx
from Error import APIError
def api(func):
    @functools.wraps(func)
    def _wrapper(*args, **kw):
        try:
            r = json.dumps(func(*args, **kw))
        except APIError, e:
            r = json.dumps(dict(error=e.error, data=e.data, message=e.message))
        except Exception, e:
            r = json.dumps(dict(error='internalerror', data=e.__class__.__name__, message=e.message))
        ctx.response.content_type = 'application/json'
        return r
    return _wrapper



