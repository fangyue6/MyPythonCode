#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月9日

@author: fangyue
'''
import re
import urllib
def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getImg(html):
    reg=r'src="(.*?\.jpg)"'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    i=0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, str(i)+".jpg")
        print "第"+str(i+1)+"张图片已下载完成"
        i=i+1
    
html=getHtml('http://image.baidu.com/i?tn=baiduimage&ct=201326592&lm=-1&cl=2&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0')
print getImg(html)
