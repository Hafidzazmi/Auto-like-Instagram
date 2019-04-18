#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:12:47 2019

@author: ocan
"""


# Import required packages
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

create_file(directory,"spider1.txt")
create_file(directory,"crawl_spider1.txt")
create_file(directory,"crawled_spider1.txt")
queue_file = directory + '/queue.txt'

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

#link to open a site
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(1)
searchBoxPath = '//input[contains(@name,"username")]'
driver.find_element_by_xpath(searchBoxPath).send_keys("USERNAME")
searchBoxPath1 = '//input[contains(@name,"password")]'
driver.find_element_by_xpath(searchBoxPath1).send_keys("PASSWORD")
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)
driver.get("SPECIFIC CATEGORY URL")

time.sleep(5)


def collect(driver, file) :
    i=0
    
    set1 =  file_to_set(file)
    while (i<500000):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0,"+str(i)+")")

        driver.execute_script("window.scrollTo(0,"+str(i-500)+")")
        driver.execute_script("window.scrollTo(0,"+str(i+500)+")")


        time.sleep(5)
        soup = BSoup(driver.page_source, 'html.parser')
        for link in soup.find_all("a"):
	    
    #link = all_link.get('href')
            soup = BSoup(driver.page_source, 'html.parser')
            set1.add(link.get('href'))
            #print(len(set1))
        #print(i)
        print(len(set1))
        set_to_file(set1,file)#print(len(set1))
        set1 =  file_to_set(file)
		
		
        i+=1000
        time.sleep(1)
        
    set_to_file(set1,file)#print(len(set1))
    
collect(driver,queue_file)
driver.close()
