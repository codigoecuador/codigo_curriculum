# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 08:21:50 2019

@author: rayde

url: https://selenium-python.readthedocs.io/
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class Bot:
    '''
    simple usage
    '''
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def search(self, url='https://www.google.com'):
        '''
        go to a specific webpage. Must include https://
        It’s worth noting that if your page uses a lot of AJAX on load then WebDriver may not know when it has completely loaded.
        '''
        self.driver.get(url)

    def get_title(self):
        ''' get the title of the webpage'''
        return self.driver.title
    
    def find_element(self, x):
        ''' find an element by name'''
        return self.driver.find_element_by_name(x)

    def send_keys(self, key='How to use Python Selenium'):
        '''
        Next, we are sending keys, this is similar to entering keys using your keyboard. Special keys can be sent using Keys class imported from selenium.webdriver.common.keys. To be safe, we’ll first clear any pre-populated text in the input field (e.g. “Search”) so it doesn’t affect our search results:
        '''
        elem = self.find_element()
        elem.clear()
        elem.send_keys(key)
        elem.send_keys(Keys.RETURN)
        
    def get_source(self):
        ''' return html code of website'''
        return self.driver.page_source
        
    def close_tab(self):
        ''' close just one tab of browser'''
        self.driver.close()
    
    def close_browser(self):
        ''' close all tabs '''
        self.driver.quit()
        
    
class test(unittest.TestCase, Bot):
    '''
    Selenium is mostly used for writing test cases. The selenium package itself doesn't provide a testing tool/framework.
    You can write test cases using Python's unittest module. The other 
    options for a tool/framework are py.test and nose. 
    
    In this chapter, we use unittest as the framework of choice. Here is the modified example
    which uses unittest module. This is a test for google.com. 
    '''
        
    def setUp(self):
        ''' 
        setUp is part of initialization and will get called before 
        every test function which you are going to write in this test case class. 
        Here you are creating an instance of Chrome WebDriver.
        '''
        self.driver = Bot().driver
        
    def test_search_in_google(self):
        '''
        This is the test case method. The test case method shoul always start with characters test. 
        The first line inside this method create a local reference to the driver object created in setUp method.
        '''
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google", driver.title)
        #assert command confirms information. returns assertion error if false. nothing if true.
        elem = driver.find_element_by_name("q")
        elem.send_keys("How to use Selenium Python")
        elem.send_keys(Keys.RETURN) #automate input of text into the searchbar.
        assert "No results found." not in driver.page_source
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()

'''
Can also run in python shell with command "python Selenium_Exercise.py"
'''


        
    