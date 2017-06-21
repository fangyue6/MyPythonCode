#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月9日

@author: fangyue
'''

import os
def dirList(path):
    filelist= os.listdir(path)
    #if filelist:
    print path
   # fpath=os.getcwd()
    for filename in filelist:
        filepath=os.path.join(path,filename)
        if os.path.isdir(filepath):
            dirList(filepath)
        else :
           print filepath


dirList(os.path.join(os.getcwd(),'testdir'))

print "**"*25

g=os.walk(os.path.join(os.getcwd(),'testdir'))
for path,d,filelist in g:
    for filename in filelist:
        print os.path.join(path,filename)




