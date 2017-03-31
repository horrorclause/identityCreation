# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:40:12 2017

@author: horrorclause
"""

from selenium import webdriver
import time
#import IMPORT FILE WITH STORED ACCOUNTS


    
def makeTA():
    
    
    
    for k,v in json_data.items():
        
        actualized = open('''List of accounts that are actualized''', 'a')
        browser = webdriver.Chrome()
        browser.get('https://www.tripadvisor.com/')
            
        #Locate and fill in appropriate fields
        time.sleep(2)                                               
        browser.find_element_by_css_selector('.link.no_cpu').click()
        time.sleep(5)
        browser.switch_to.frame('overlayRegFrame')
        browser.find_element_by_css_selector('.ui_button.primary.w100p.regTaEmail').click()
        time.sleep(.5)
        insertEmail = browser.find_element_by_id('regSignUp.email')          
        insertEmail.send_keys(v[0])
        insertPass = browser.find_element_by_id('regSignUp.password')          
        insertPass.send_keys(v[1])                                                                       
        time.sleep(.5)
        browser.find_element_by_css_selector('.ui_button.primary.regSubmitBtn').click()
        time.sleep(15)                           
        
                    
        actualized.write('\n'+k)    #Adds full name of actualized accounts
        actualized.close()
        browser.quit()
        
        time.sleep(600)
        
    
        
        
makeTA()
