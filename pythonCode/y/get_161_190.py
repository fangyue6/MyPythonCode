# coding:utf-8
'''
#author: SomeOne
#date: 2015-04-02
#copyright: default
'''
import urllib2
from bs4 import BeautifulSoup
import re
import os.path
import csv
import sys, codecs
reload(sys)
sys.setdefaultencoding( "utf-8" )


def repalce(s,re_exp,repl_string):
    return re_exp.sub(repl_string,s)
def get_href(url):
    page = urllib2.urlopen(url)
    html_doc = page.read()
    #html_doc=open('html.html')
    soup = BeautifulSoup(html_doc.decode('gb2312','ignore'),"lxml")
    #soup=BeautifulSoup(html_doc,"lxml")#,"lxml"
    soup_pret=soup.prettify()
    #.find('table')
    href=soup.find('div',class_='fullHNS').find('table').find_all('table')[1].find('td').find('input').get('value').strip()
    return href
#得到总页数
def get_total_page(url):
    page = urllib2.urlopen(url)
    html_doc = page.read()
    #html_doc=open('html.html')
    soup = BeautifulSoup(html_doc.decode('gb2312','ignore'),"lxml")
    #soup=BeautifulSoup(html_doc,"lxml")#,"lxml"
    soup_pret=soup.prettify()
   
    bb=soup.find('div',class_='fullLS').find('div',class_='area').find('div',class_='center').find_all('table')[1].find('tr').find('td').find('span').string.strip()
    b=bb.split(' ')[0].split('/')[1]
    print(b)
    return int(b)

def jd_01(index,url, filename):
    page = urllib2.urlopen(url)
    html_doc = page.read()
    #html_doc=open('html.html')
    soup = BeautifulSoup(html_doc.decode('gb2312','ignore'),"lxml")
    #soup=BeautifulSoup(html_doc,"lxml")#,"lxml"
    soup_pret=soup.prettify()
   
    bb=soup.find('div',class_='fullLS').find('div',class_='area').find('div',class_='center').find('table').find_all('tr',class_='row')
    #print(bb)
    for i in bb:
        #名称
        name=i.find_all('td')[0].find('a').string.strip()
        #链接
        href=get_href('http://8xfzy.com'+i.find_all('td')[0].find('a').get('href').strip())
        #国家
        country=i.find_all('td')[1].find('font').string.strip()
        #类型
        clsss_=i.find_all('td')[2].find('font').string.strip()
        #时间
        time=i.find_all('td')[3].string.strip()
        print(time)#name+'--'+href+'---'+country+'---'+clsss_+'---'+
        tarr=[index,name,country,clsss_,time,href]
        #print(tarr)
        filename.writerow(tarr)

if __name__ == "__main__": 
    output = open("y_162_190.csv", "ab+")
    output.write(codecs.BOM_UTF8)
    ww = csv.writer(output, dialect='excel')   
    tarr = ["序号","名字", "国家", "类型", \
            "时间" ,"地址"]
    #ss = ",".join(tarr)
    ww.writerow(tarr)
    #total_page=get_total_page('http://8xfzy.com/5qlis/index29.html')
    for i in range(186,191):
        print(str(i)+'-------------------------------------------')
        if i==1:
            url = "http://8xfzy.com/5qlis/index29.html"
        else :
            url = "http://8xfzy.com/5qlis/index29_"+str(i)+".html"
        #http://tianchi.shuju.aliyun.com/competition/rankingList.htm?season=1&raceId=231530&pageIndex=1
        try:
            jd_01(i,url, ww)
        except:
            print("^^^^^error:"+str(i)+"  ^^^^^^^^")
            f=open("y_error_161_190.txt", "ab+")
            f.write(str(i)+'\n')
            f.close()
    output.close()





    
'''
http://8xfzy.com/5qlis/index29.html
http://8xfzy.com/5qlis/index29_2.html
http://8xfzy.com/5qlis/index29_222.html

'''