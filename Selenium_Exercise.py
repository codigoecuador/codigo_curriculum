# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 08:21:50 2019

@author: rayde

url: https://selenium-python.readthedocs.io/
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.by import By

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

class Element_Search(Bot):
    ''' find single elements. Use elements to search for multiple.'''
    def by_id(self):
        ''' 
        this method will search by id. https://www.w3schools.com/tags/att_id.asp
        The id attribute specifies a unique id for an HTML element (the value must be unique within the HTML document).
        The id attribute is most used to point to a style in a style sheet (CSS), an by JavaScript (via the HTML DOM) to 
        manipulate the element with the specific id.
        
        The id attribute is part of the Global Attributes, and can be used on any HTML element. 
        HTML attributes give elements meaning and context. The global attributes below can be used on any HTML element. 
        examples of HTML global attributes: 
            1. class (Specifies one or more classnames for an element (refers to a class in a style sheet))
            2. title (Specifies extra information about an element)
            3. style (Specifies an inline CSS style for an element)
        '''
        self.driver.find_element_by_id
        
    def by_name(self):
        ''' 
        The name attribute specifies the name of an <input> element. 
        The name attribute is used to reference elements in a JavaScript, or to 
        reference form data after a form is submitted. 
        
        Only form elements with a name attribute will have their values passed when submitting a form.
        
        https://www.w3schools.com/tags/att_input_name.asp
        '''
        self.driver.find_element_by_name
    
    def by_xpath(self):
        '''
        XPath is defined as XML Path. It is syntax or language for finding any element on the webpage using XML path expression.
        XPath is used to find the location of any element on a webpage using HTML DOM structure. 
        DOM or Document Object Model is a cross-platform and language-independent interface that treats an XML or HTML document as a tree
        structure wherin each node is an object representing part of the document. The DOM represents a ocument with a logical tree. 
        The HTML DOM defines:
            1) HTML elements as objects
            2) Properties
            3) Methods
            4) Events
        
        HTML DOM is an API (Programming Interface) for JavaScript: 
            JavaScript can: add/change/remove HTML elements, attributes, CSS styles, and events. 
            Javascript can also react to HTML events.
        
        https://www.w3schools.com/whatis/whatis_htmldom.asp
        '''
        self.driver.find_element_by_xpath
        
    def by_link_text(self):
        '''
        HTML links are hyperlinks. You can click on a link to go to another webpage or document.
        When you move the mouse over a link, the mouse arrow will turn into a little hand.
        A link does not have to be text. It can be an image or any other HTML element. 
        
        Hyperlinks are defined with the HTML <a> tag. 
        
        example:<a href="https://www.w3schools.com/html/">Visit our HTML tutorial</a>
        the "href" attribute specifies the destination address of the link. 
        The link text is the visible part. "Visit our HTML tutorial"
        
        https://www.w3schools.com/html/html_links.asp
        '''
        self.driver.find_element_by_link_text
    
    def by_partial_link(self):
        '''
        url = https://www.guru99.com/locate-by-link-text-partial-link-text.html
        
        Links can be accessed using an exact or partial match of their link text. 
        
        Accessing links using a portion of their link text is done using the By.partialLinkText() method. If you specify a partial link text that has multiple matches, only the first match will be accessed.
        
        If you want to access multiple links with similar text, use xpath()
        '''
        self.driver.find_element_by_partial_link_text
        
    def by_tag(self):
        ''' https://www.w3schools.com/tags/
        There are many different HTML tags. Common HTML tags you will encounter include:
            <a> : Defines a hyperlink
            <address>: Defines contact information for the author/owner of a document.
            <b>: Defines bold text
            <base>: Specifies the base URL/target for all the relative URLs in a document.
            <body>: defines the document body
            <button>: defines a clickable button
            <div>: defines a section in a document.
            <form>: defines a HTML form for user input
            <head>: defines information about the document.
            <hr>: defines a thematic change in the content.
            <img>: defines an image
            <p>: defines a paragraph
            <span>: defines a section in a document
            <table>: defines a table
            <tbody>: defines the body content in a table
            <td> defines a cell in a table
            <th> defines a header cell in a table
            <thead> groups the header content in a table
            <title> defines the title for the document
            
        '''
        self.driver.find_element_by_tag_name
    
    def by_class(self):
        '''
        https://www.w3schools.com/html/html_classes.asp        
        The HTML class attribute is used to define equal styles for elements with the same
        class name.         
        So, all HTML elements with the same class attribute will get the same style.         
        An HTML element can contain many different classes pointing to different objects or text with different styles.         
        Tags can share the same class. 
        
        '''
        self.driver.find_element_by_class_name
    
    def by_css(self):
        '''
        https://www.w3schools.com/cssref/css_selectors.asp
        In CSS, selectors are patterns used to select the element(s) you want to style. 
        common css selectors you will encounter include:
            1) .class = selects all the elements of a particular class
            2) .class1.class2 = selects all the elements of both those classes. 
            3) #id = selects the element of a particular id
        
        Most of the time, you will want to use an xpath selector, but it is still useful to understand
        how css selectors work. 
        '''
        self.driver.find_element_by_css_selector
        
if __name__ == "__main__":
    unittest.main()

'''
Can also run in python shell with command "python Selenium_Exercise.py"
'''


        
    