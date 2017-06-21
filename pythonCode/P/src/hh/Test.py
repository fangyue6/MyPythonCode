# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 12:12:08 2016

@author: admin
"""
import os
from selenium import webdriver  
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类  
from selenium.webdriver.common.keys import Keys #引入keys类操作  
import time  

import urllib.request
from bs4 import BeautifulSoup
   
def s(int):  
    time.sleep(int)  

def getVedioUrl(url):
    browser1 = webdriver.Firefox()
    browser1.get(a1)
    href = browser1.find_element_by_class_name('ndownlist').find_element_by_xpath("//ul/li[1]/p/a").get_attribute("href") 
    browser1.quit()
    return href
    

#chromedriver = "C:\Program Files (x86)\Mozilla Firefox\firefox.exe"    
browser = webdriver.Firefox()  #"C:/path/Chromedriver.exe"
  
#print('现在将浏览器最大化') 
#browser.maximize_window()  
#text = browser.find_element_by_name('f').text 
#imgsrc = browser.find_element_by_id('lg').find_element_by_tag_name('img').get_attribute("src") 
#print(text) #打印备案信息  

#browser.get('https://www.ccc557.com/htm/movie1/6502.htm')
#href = browser.find_element_by_class_name('ndownlist').find_element_by_xpath("//ul/li[1]/p/a").get_attribute("href") 
#print(href)
#
#browser.get('https://www.ccc557.com/htm/movie1/6502.htm')
#href = browser.find_element_by_class_name('ndownlist').find_element_by_xpath("//ul/li[1]/p/a").get_attribute("href") 
#print(href)
#
#browser.quit()

browser.get('https://www.ccc557.com/htm/index.htm')
a = browser.find_element_by_xpath("//div[3]/ul[2]/li[2]/a")
a1 = a.get_attribute("href") 
a2 = a.text
print(a1,a2)

s(2)
#其中一页

browser.get(a1)
ul = browser.find_element_by_xpath("//div[5]/div[1]/ul[1]")
lis = ul.find_elements_by_css_selector('li')

for i in range(len(lis)):
    print(str(i+1))
    a = browser.find_element_by_xpath("//div[5]/div[1]/ul[1]/li["+str(i+1)+"]/a")
    #a = ul.find_element_by_xpath("//li["+str(i+1)+"]/a")
    apic = a.find_element_by_tag_name("img").get_attribute('src')
    a1 = a.get_attribute('href')
    a2 = a.find_element_by_tag_name('h3').text
    print(apic,a1,a2)
    ##爬一个电影
    url = getVedioUrl(a1)
    print(url)

    
#apic = a.find_element_by_tag_name("img").get_attribute('src')
#a1 = a.get_attribute('href')
#a2 = a.find_element_by_xpath('//h3').text
#print(apic,a1,a2)




##爬一个电影
#url = getVedioUrl(browser,a1)
#print(url)
#
#browser.quit()
#www.869bb.com
#https://www.ccc557.com/htm/index.htm




# 通过id定位元素：find_element_by_id("id_vaule")
# 通过name定位元素：find_element_by_name("name_vaule")
# 通过tag_name定位元素：find_element_by_tag_name("tag_name_vaule")
# 通过class_name定位元素：find_element_by_class_name("class_name")
# 通过css定位元素：find_element_by_css_selector();用css定位是比较灵活的
# 通过xpath定位元素：find_element_by_xpath("xpath")
# 通过link定位：find_element_by_link_text("text_vaule")或者find_element_by_partial_link_text()