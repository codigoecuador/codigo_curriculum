# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:53:24 2020

@author: rayde
"""

import pandas, json, requests, datetime, calendar

class dividend_calendar:
     calendars = []
     errors = []
     def __init__(self, year, month):
          '''
        Parameters
        ----------
        year : year int
        month : month int
        
        Returns
        -------
        Sets instance attributes for year, month, and day of object.
        Class attributes are calendars and methods.
          '''
          self.year = int(year)
          self.month = int(month)  
     
     
     def url(self, date):
         '''

         Parameters
         ----------
         date : date str

         Returns
         -------
         URL = base + subdomain
             technically when we use requests we can simply pass these three parameters in as a 
             dictionary with params = {'year':year, 'month':month, 'day':day}
             For this example we will pass the paramaters manually into the URL.

         '''
         base = 'https://api.nasdaq.com/api/'
         subdomain = "calendar/dividends?date={0}"
         subdomain = subdomain.format(date)
         return base + subdomain
      
     def header(self, date):
         '''
         Parameters
         ----------
         year : year int
         month : month int
         day : day int

         Returns
         -------
         hdrs : dictionary object containing values to header parameters.

         '''
         base = 'https://www.nasdaq.com/'
         referer = "market-activity/dividends?date={0}"
         hdrs = {'Accept': 'application/json, text/plain, */*',
                 'DNT': "1",
                 'Origin': base,
                 'Referer': base + referer.format(date),
                 'Sec-Fetch-Mode': 'cors',
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0)'}
         return hdrs
      
     def scraper(self, url, hdrs):
         '''
           Parameters
           - - - - - 
           url : URL string
           hdrs : Header information
           Returns
           - - - -
           dictionary : Returns a JSON dictionary at a given URL.
         '''
         page = requests.get(url, params = hdrs)
         page = page.content
         dictionary = json.loads(page)
         return dictionary
     
      
     def dict_to_df(self, dicti):
          '''
          Parameters
          ----------
          dicti : Output from the scraper method as input.
          Returns
          -------
          calendar : Dataframe of stocks with that exdividend date
          Appends the dataframe to one of the class attributes
          If the date is a trading day, it will append a dataframe 
          to the calendars list (class attribute).
          If the date provided is a nontrading day, then the method 
          will append an error message with 'bad or no parameter 
          [date]' to the errors list (class attribute).
         '''
          try:
               rows = dicti.get('data').get('calendar').get('rows')
               calendar = pandas.DataFrame(rows)
               self.calendars.append(calendar)
          except:
               rows = dicti.get('status').get('bCodeMessage')
               calendar = pandas.DataFrame(rows)
               self.errors.append(calendar)
          finally:
               return calendar
           
            
     def calendar(self, day):
          '''
          Combines the above methods into one method.
          
          Parameters
          ----------
          day : day of the month as string or number.
          
          Returns
          -------
          dictionary : Returns a JSON dictionary with keys 
          dictionary.keys() => data, message, status
          
          Next Levels: 
          dictionary['data'].keys() => calendar, timeframe
          dictionary['data']['calendar'].keys() => headers, rows
          dictionary['data']['calendar']['headers'] => column names
          dictionary['data']['calendar']['rows'] => dictionary list
    
          '''
          self.day = day
          
          date = datetime.date(year, month, day)
          date = date.strftime(format='%Y-%m-%d')
          
          hdrs = self.header(date)
          url = self.url(date)
          
          dictionary = self.scraper(url, hdrs)
          self.dict_to_df(dictionary)
          
          return dictionary
           
if __name__ == '__main__':
    year = 2020
    month = 2
    
    #get number of days in month
    days_in_month = calendar.monthrange(year, month)[1]

    #create calendar object    
    february = dividend_calendar(year, month)

    #define lambda function to iterate over list of days     
    function = lambda days: february.calendar(days)
    
    #define iterator as a list of integers between 1 and the number of days in the month
    iterator = list(range(1,days_in_month+1))

     #Scrape calendar for each day of the month                    
    objects = list(map(function, iterator))

     #concatenate all the calendars in the class attribute
    df = pandas.concat(february.calendars)
    
    #Drop any rows with missing data
    df = df.dropna(how='any')
    
    #set the dataframe's row index to the company name
    df = df.set_index('companyName')
    
    date = datetime.date(year, month, day=28)
    date = date.strftime(format='%Y-%m-%d')
    
    urls = february.url(date)
    urls
    
    hdrs = february.header(date)
    hdrs
    
    page = requests.get(urls, params = hdrs)
    page
    
    page = page.content
    page 
    
    dictionary = json.loads(page)
    dictionary
    
    rows = dictionary.get('data').get('calendar').get('rows')
    rows 
    
    cal = pandas.DataFrame(rows)
    cal