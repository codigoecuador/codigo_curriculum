# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 11:45:58 2019

@author: rayde

https://medium.com/better-programming/how-to-replace-your-python-for-loops-with-map-filter-and-reduce-c1b5fa96f43a
"""

'''
For loops are a Swiss army knife for problem-solving, but, when it comes to scanning code to get a quick read of what you’ve done, they can be overwhelming.

Three techniques — map, filter, and reduce — help remedy the for loop mania by offering functional alternatives that describe why you’re iterating.

Map: Apply the same set of steps to each item, storing the result.

Filter: Apply validation criteria, storing items that evaluate True.

Reduce: Return a value that is passed from element to element.

Map, Filter, and Reduce are functions versus methods. 

Functions are: a piece of code that is called by name. It can be passed data to operate on 
and can optionally return data (the return value). 

functions are written like function(arguments, object)

Methods are: a piece of code that is called by a name that is associated with an object. 

methods are written like: object.method(arguments)

'''
from functools import reduce 

'''
map() and filter() are natively available. 
Natively available means built in with no import necessary.
However, reduce() must be imported from the functools library in Python 3+.
'''

# Basic For Loops

numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = []
squared_odd_numbers = []
total = 0 

for number in numbers:
    ''' check for odd numbers '''
    if number % 2 == 1: 
        ''' append to odd_numbers list '''
        odd_numbers.append(number)

for number in odd_numbers:
    ''' append the square of each odd_number to squared_odd_numbers'''
    squared_odd_numbers.append(number * number)

for number in squared_odd_numbers:
    ''' add each of the squared_odd_numbers to the total '''
    total += number
    
# Filter 

odd_numbers = filter(lambda n: n % 2 == 1, numbers)

# Map Example 

squared_odd_numbers = map(lambda n: n*n, odd_numbers)

# Reduce 
'''
The lambda expression for reduce() requires two arguments: the accumulator (the value that is passed to each element) and the individual element itself.
'''
total = reduce(lambda acc, n: acc + n, squared_odd_numbers)

#Anonymous Functions 

my_list = []

square = lambda number: number * number 

map(square, my_list)

#Full Blown Function

def inefficientSquare(number):
    result = number * number
    return result

map(inefficientSquare, my_list)