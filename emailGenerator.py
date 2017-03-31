# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 11:49:52 2017

@author: mjerez
"""
from selenium import webdriver
import time
from identityCreation import json_data
#makeEmail function connects to protonmail and creates an email account

    
def makeEmail():
    for k, v in json_data.items():
        username = v[0].split('@')[0]
        pword = v[1]
        
        browser = webdriver.Chrome()
        browser.get('https://mail.protonmail.com/create/new')
            
        #Locate and fill in appropriate fields
        time.sleep(5)                                               #Wait 5 sec to allow webpage to load
        nameElem = browser.find_element_by_id('username')           #Identify username input
        nameElem.send_keys(username)                                #Insert created username
        pElem = browser.find_element_by_id('password')              #Identify password box
        pElem.send_keys(pword)                                      #Insert created password
        time.sleep(.5)
        pCheckElem = browser.find_element_by_id('passwordc')        #Identify password check
        pCheckElem.send_keys(pword)                                 #Verify password
        time.sleep(.5)
        browser.find_element_by_css_selector('.pm_button.primary.large.signUpProcess-btn-create').click()        #Need to be able identify button
        time.sleep(2)
        browser.find_element_by_css_selector('.pm_button.primary').click()
        time.sleep(45)
        browser.quit()
        actualized = open('actualizedAccounts.txt', 'a')            #Adds full name of actualized accounts to actualizedAccounts.txt
        actualized.write(k+'\n')
        actualized.close()
        
makeEmail()
