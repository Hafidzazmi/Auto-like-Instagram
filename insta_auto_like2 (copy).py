#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:12:28 2019

@author: ocan
"""

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
import openpyxl as excel
from bs4 import BeautifulSoup as BSoup
import time
import os
import random


driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

#link to open a site
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(1)
searchBoxPath = '//input[contains(@name,"username")]'
driver.find_element_by_xpath(searchBoxPath).send_keys("USERNAME")
searchBoxPath1 = '//input[contains(@name,"password")]'
driver.find_element_by_xpath(searchBoxPath1).send_keys("PASSWORD")
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(1)
driver.get("RANDOM INSTA URL")

time.sleep(5)

directory = 'FILE_NAME'


def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory )
        os.makedirs(directory)
        
def create_file(directory,file_name):
    spider1 = directory + '/'+ file_name
    if not os.path.isfile(spider1):
        write_file(spider1, '')
        
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
    
    
# add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
        
#delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass
    
#read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

#iterate thorugh a set, each item will be a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file,link)
        
queue_file = directory + '/queue.txt'
crawled_file = directory + '/crawled.txt'
i=1
crawled=0
while (i==1) :
    
    set_queue = file_to_set(queue_file)
    set_Crawl = file_to_set(crawled_file)
    crawling_set = set()
	
    print(len(set_queue))
    #print("+++")
    #print(len(set_Crawl))
    #print("---")
    #print(len(crawling_set))
    #print("ooo")
    set_queue  =  [item for item in set_queue if item not in set_Crawl]
    grab_content = random.randint(53,197)
    crawled += grab_content
    print('crawled : ' + str(crawled))
    number_of_page = len(set_queue)
    if number_of_page ==0:
        break
    if number_of_page > grab_content:
        
        for nums  in range (grab_content):
            crawling_set.add(list(set_queue)[nums])
            set_Crawl.add(list(set_queue)[nums])
    
    else:
        for nums  in range (number_of_page):
            crawling_set.add(list(set_queue)[nums])
            set_Crawl.add(list(set_queue)[nums])
    #print(len(set_queue))
    #print("+++")
    #print(len(set_Crawl))
    #print("---")
    #print(len(crawling_set))
    #print("/n")
    set_to_file(set_Crawl,crawled_file)
    set_queue  =  [item for item in set_queue if item not in crawling_set]
    set_to_file(set_queue,queue_file)

    for page in range (len(crawling_set)):
        driver.get("https://www.instagram.com"+list(crawling_set)[page])
        time.sleep(10)
        try: 
            driver.find_element_by_class_name('coreSpriteHeartOpen').click()
        except:
            pass
    time.sleep(random.randint(21, 35))


driver.close()
