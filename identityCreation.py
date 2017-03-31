# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 10:56:18 2017

@author: mjerez
"""

import secrets, random
import string
import json


#Loads file of random names, creates password generator source, creates username
#password, and selects random name. Assigns to dictionary info and exports to 
#json file accounts.json

file = open('C:/Users/Mario/Dropbox/Accounts/names.txt','r')
data = file.read()
names = data.strip('\xa0').split('\n')
names = list(map(lambda s: s.split(), names))
fixName = [ x for x in names if x]                                  #List of names
characters = string.ascii_letters+string.digits+string.printable    #Source for password
info = dict()


for i in range(len(fixName)):
    person = ' '.join([i for i in secrets.choice(fixName) if i not in info])
    ran = ''.join(secrets.choice(string.digits) for i in range(5))
    pword = ''.join(secrets.choice(characters) for i in range(12))
    username = person.split()[random.randint(0,1)]+ran+'@protonmail.com'
    info[person] =[username,pword]
    
    
print(info)

with open('accounts.json', 'w') as f:
    json.dump(info, f)


json_file = open('accounts.json')       #Opens accounts.json
json_str = json_file.read()             
json_data = json.loads(json_str)        #Stored dictionary 
