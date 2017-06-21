#!/usr/bin/python
# -*- coding: GBK -*-
'''
Created on 

@author: fangyue
'''
import re
import string
import urllib
#获取网页内容
def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getRE(val,reg):
    pattern=re.compile(reg) # 将正则表达式编译成Pattern对象
    # 使用search()查找匹配的子串，不存在能匹配的子串时将返回None 
    match = pattern.search(val)
    if match:
        return match.group() # 使用Match获得分组信息
    
def getVedio(val,reg):
    xs= re.findall(reg,val)
    for x in xs:
        return x
print "正在抓取....."
html=getHtml('http://www.dytt8.net')

#得到最新电影
newVedio=getRE(html,r"<!--{start:最新-->[\s\S]{0,}<!--}end:最新-->")

newVedioList=re.findall("href='(.*?)'",newVedio)
for index,val in enumerate(newVedioList):
    newVedioList[index]='http://www.dytt8.net'+str(val)
for val in newVedioList:
    print getVedio(getHtml(val),'<a href="(ftp://.*?)"')
'''xs= re.findall('<a href="(ftp://.*?)"',getHtml("http://www.dytt8.net/html/gndy/jddy/20150701/48431.html"))
for x in xs:
     print  x'''
#print getVedio("http://www.dytt8.net/html/gndy/jddy/20150701/48431.html", '<a href="(ftp://.*?)"')

