# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 16:00:24 2019

@author: rayde
https://medium.com/c%C3%B3digo-ecuador/tagged/web-scraping
"""

from datetime import datetime, timedelta
import time
import requests, pandas, lxml
from lxml import html

def scrape_page(url, hdrs):
     page = requests.get(url, params=hdrs)
     element_html = html.fromstring(page.content)
     table = element_html.xpath('//table')
     table_tree = lxml.etree.tostring(table[0], method='xml')
     panda = pandas.read_html(table_tree)
     return panda

def format_date(date_datetime):
    date_timetuple = date_datetime.timetuple()
    date_mktime = time.mktime(date_timetuple)
    date_int = int(date_mktime)
    date_str = str(date_int)
    return date_str
 
def subdomain(symbol, start, end, filter='history'):
    '''

    Parameters
    ----------
    symbol : stock symbol - canada should end with '.to'
    start : start date in epoch time
    end : end date in epoch time
    filter : history or div
        DESCRIPTION. The default is 'History'.

    Returns
    -------
    subdomain : url 

    '''
    subdoma="/quote/{0}/history?period1={1}&period2={2}&interval=1d&filter={3}&frequency=1d"
    subdomain = subdoma.format(symbol, start, end, filter)
    return subdomain
 
def header_function(subdomain):
    hdrs =  {"authority": "finance.yahoo.com",
                 "method": "GET",
                 "path": subdomain,
                 "scheme": "https",
                 "accept": "text/html",
                 "accept-encoding": "gzip, deflate, br",
                 "accept-language": "en-US,en;q=0.9",
                 "cache-control": "no-cache",
                 "cookie": "Cookie:identifier",
                 "dnt": "1",
                 "pragma": "no-cache",
                 "sec-fetch-mode": "navigate",
                 "sec-fetch-site": "same-origin",
                 "sec-fetch-user": "?1",
                 "upgrade-insecure-requests": "1",
                 "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64)"}
    return hdrs
 
if __name__ == '__main__':
    base_url = 'https://finance.yahoo.com'
    symbol = 'BTC-USD'
     
    dt_start = datetime.today() - timedelta(days=1000)
    dt_start
    
    dt_end = datetime.today()
    dt_end
    
    start = format_date(dt_start)
    start
    
    end = format_date(dt_end)
    end
    
    sub = subdomain(symbol, start, end)
    sub
    
    hdrs = header_function(sub)
    hdrs
    
    url = base_url + sub
    url
    
    page = requests.get(url, headers=hdrs)
    page
    page.content
    
    element_html = html.fromstring(page.content)
    element_html
    
    table = element_html.xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table')
    table
    
    table_tree = lxml.etree.tostring(table[0], method='HTML', pretty_print=True)
    table_tree
    
    panda = pandas.read_html(table_tree)
    panda
    