"""
Created on Thu Apr 27 16:28:36 2017
@author: barnabysandeford
"""
# Currently works for Safari, but just change to whichever
# browser you're using.

import time
#Changed the method of opening the browser.
#Selenium allows for the page to be refreshed.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
driver.get("file:///C:/Users/96653/Desktop/1.html") #register page

while True:
    try:
        inputElement = driver.find_element_by_id("crn__id1")
        inputElement.send_keys('hhhhhhh')
        inputElement.submit()
        time.sleep(1)
    except:
            pass
    driver.refresh()

