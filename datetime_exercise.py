# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 09:08:35 2019

@author: rayde
https://towardsdatascience.com/speeding-through-dates-with-pandas-35472ba028f9
"""
import datetime

datetime.datetime.now()

#datetime objects can be compared through simple computation
dt_a = datetime.datetime(2019, 1, 1)

#declare a date with explicitly definining arguments
dt_b = datetime.datetime(year=2019, month = 11, day = 1, hour=0, minute=0, second=1)

#How many days have passed since date a?
print(f'DateA is {dt_b - dt_a} before Date B')


''' 
The demonstrated computation is possible since all datetime objects contain
date and time instances (even though we didn't specify them in A)

Similarly datetime objects can be computed with instances of just date or time
classes - this is done by instantiating a timedelta object.

Attributes of date: year, month, day
Attributes of time: hour, minute, second, microsecond, tzinfo
'''

#What is the datetime 3 days and 10 seconds from January 1, 2019

#Create a date & a time difference

dt_a = datetime.datetime(2019, 1, 1)
diff = datetime.timedelta(days=3, seconds = 10)

dt_later = dt_a + diff

print(f'({dt_a}) + 3 days and 10 seconds = ({dt_later})')

#Take away is: datetime + timedelta = datetime

'''
Pro tip: timedelta objects contain most (but not all) of the same classes as 
datetime objects. keep in mind to convert between time units when necessary.
'''

'''
Many data objects such as csv store dates in the form of strings. These strings
can be parsed with the strptime method from a datetime.datetime object. 

'''

#Convert from string to date

dt_string = "01/01/2019"
dt_format = '%m/%d/%Y'

dt = datetime.datetime.strptime(dt_string, dt_format)

print(dt)

#get the datetime of every hour since the Chinese New Year (Lunar)

ch_new_yr = datetime.datetime(2019, 2, 5)
today = datetime.datetime.now()

#compute the difference, then access the number of days
days= (today-ch_new_yr).days

all_days = []

for i in range(1, days+1):
    diff = datetime.timedelta(days=i)
    day = ch_new_yr + diff 
    all_days.append(day)

print(f'There are {len(all_days)} days from {all_days[0].date()} (the Chinese New Year) until today ({all_days[-1].date()})')

#Reduce for loop to a single line using list comprehension
all_days = [ch_new_yr + datetime.timedelta(days=i) for i in range(1, days+1)]

''' 
Create a function which will instantiate a big sample of dates data in string format
Note: the non-standard string format is implemented to create a computationsally demanding 
scenario. 
'''

import pandas as pd 
import datetime
import numpy as np

def create_many_dates(start = '1-1-2000', n_repeat = 10**3, sz= 10**6, noise = False):
    ''' This function will return a seriez `s` with a size of `sz` and `n_repeat` unique dates. 
        - Each date will be +1 day from the `start` date
        - Input date format: '%m-%d-%Y'
    '''
    
    some_date = datetime.datetime.strptime(start, '%m-%d-%Y')
    
    if noise==True:
        s = [(some_date + datetime.timedelta(days=i, seconds=np.random.randint(1,10000))).strftime('%b-%d-%Y %H:%M:%S') for i in range(n_repeat)]
        
    else: 
        s= [(some_date + datetime.timedelta(days=i)).strftime('%b-%d-%Y') for i in range(n_repeat)]
    
    s *=int(sz/n_repeat)
    
    s = pd.Series(s)
    
    return s

s = create_many_dates('1-1-2000', n_repeat=10**3, sz=10**7, noise=True)

print(f' {len(s):,}')

''' 
Get the Speed
A function to return the speed of a function. This is getting meta. 
'''

def speed_tester(function, s):
    ''' 
    returns the time required to convert the series `s` using the function `function`
        note: this is a bad function and is not     
    