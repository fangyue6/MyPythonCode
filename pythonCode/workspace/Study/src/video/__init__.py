#!/usr/bin/python
# -*- coding: GBK -*-
'''
Created on 

@author: fangyue
'''
import re
import string
import urllib
#��ȡ��ҳ����
def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getRE(val,reg):
    pattern=re.compile(reg) # ��������ʽ�����Pattern����
    # ʹ��search()����ƥ����Ӵ�����������ƥ����Ӵ�ʱ������None 
    match = pattern.search(val)
    if match:
        return match.group() # ʹ��Match��÷�����Ϣ
    
def getVedio(val,reg):
    xs= re.findall(reg,val)
    for x in xs:
        return x
print "����ץȡ....."
html=getHtml('http://www.dytt8.net')

#�õ����µ�Ӱ
newVedio=getRE(html,r"<!--{start:����-->[\s\S]{0,}<!--}end:����-->")

newVedioList=re.findall("href='(.*?)'",newVedio)
for index,val in enumerate(newVedioList):
    newVedioList[index]='http://www.dytt8.net'+str(val)
for val in newVedioList:
    print getVedio(getHtml(val),'<a href="(ftp://.*?)"')
'''xs= re.findall('<a href="(ftp://.*?)"',getHtml("http://www.dytt8.net/html/gndy/jddy/20150701/48431.html"))
for x in xs:
     print  x'''
#print getVedio("http://www.dytt8.net/html/gndy/jddy/20150701/48431.html", '<a href="(ftp://.*?)"')

