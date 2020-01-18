# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:53:24 2020

@author: rayde
"""

import pandas, json, requests

class dividend_calendar:
     calendars = []
     errors = []

     def __init__(self, year, month):
          '''
        Parameters
        ----------
        year : year.
        month : month.
        
        Returns
        -------
        Sets instance attributes for year, month, and day of object.
        Class attributes are calendars and methods.
          '''
          self.year = str(year)
          self.month = str(month)
     
     def url(self, year, month, day):
         '''

         Parameters
         ----------
         year : year string
         month : month string
         day : day string

         Returns
         -------
         URL 
             base + subdomain = URL 
             technically when we use requests we can simply pass these three parameters in as a 
             dictionary with params = {'year':year, 'month':month, 'day':day}
             For this example we will pass the paramaters manually into the URL.

         '''
         base = 'https://api.nasdaq.com/api/'
         subdomain = "calendar/dividends?date={0}-{1}-{2}"
         subdomain = subdomain.format(year, month, day)
         return base + subdomain
      
     def header(self, year, month, day):
         '''
         Parameters
         ----------
         year : year as string
         month : month as string
         day : day as string

         Returns
         -------
         hdrs : dictionary object containing values to header parameters.

         '''
         base = 'https://www.nasdaq.com/'
         referer = "market-activity/dividends?date={0}-{1}-{2}"
         hdrs = {'Accept': 'application/json, text/plain, */*',
                 'DNT': "1",
                 'Origin': base,
                 'Referer': base + referer.format(year, month, day),
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
     
     def calendar(self, day):
          '''
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
          self.day = str(day)
          hdrs = self.header(self.year, self.month, self.day)
          url = self.url(self.year, self.month, self.day)
          dictionary = self.scraper(url, hdrs)
          self.dict_to_df(dictionary)
          
          return dictionary
     def dict_to_df(self, dicti):
          '''
          Parameters
          ----------
          dicti : Output from the calendar method as input.
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
           
if __name__ == '__main__':
     february = dividend_calendar('2020', '02')
     
     function = lambda days: february.calendar(days)
     objects = list(map(function, list(range(32))))
     df = pandas.concat(february.calendars)
     df = df.dropna(how='any')
     df = df.set_index('companyName')