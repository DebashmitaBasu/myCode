#! python3
# -*- coding: utf-8 -*-
#title					:selTry1.py
#author					:Debashmita
#date of creation		:11/07/2022 14:03
#==============================================================================

from datetime import datetime
startTime = datetime.now()

from selenium import webdriver
browser = webdriver.Firefox()
print(type(browser))
browser.get('http://inventwithpython.com')
 
print('Time taken: {}'.format(datetime.now() - startTime))