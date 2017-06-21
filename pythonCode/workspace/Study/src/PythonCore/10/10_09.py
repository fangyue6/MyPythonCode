#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月10日

@author: fangyue
'''
import os, socket, errno, types, tempfile

class NetworkError(IOError):
    pass
class FileError(IOError):
    pass
def updArgs(args, newarg=None):
    if isinstance(args, IOError):
        myargs = []
        myargs.extend([arg for arg in args])
    else:
        myargs = list(args)
    if newarg:
        myargs.append(newarg)
        return tuple(myargs)
def fileArgs(file, mode, args):
    if args[0] == errno.EACCES and \
        'access' in dir(os):
        perms = ''
        permd = { 'r': os.R_OK, 'w': os.W_OK,'x': os.X_OK}
        pkeys = permd.keys()
        pkeys.sort()
        pkeys.reverse()


