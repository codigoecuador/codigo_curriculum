# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 10:30:40 2019

#How to reverse a string in Python
https://medium.com/better-programming/how-to-reverse-a-string-in-python-43780399d670

@author: rayde
"""

#String: A sequence of character data. Text Data. 
    #Properties: Iterable, enumerable

#Iterable: Can be looped over

#Enumerable: A data type that can be counted over. Structured order.
    

# What is reversing a string?
    #Taking the last character and making it the first, the second to last becomes second, etc. 

name = 'Jonathan' 

# name in reverse => 'nahtanoJ'

#Two methods to reverse a string

''' Metodo Uno
Programmatically using reverse/join. This is a generic technique that involves creating 
a reversed iterable and reconstituting it as a string. The exact implementation is 
Python-specific; however, the technique is broadly implemented across many languages. 
'''    

'''
This method involves treating a string as an array of characters, reversing it, and reconstituting it as a string. 
In other languages, this technique might involve a for loop to iterate over each index and create
a reverse data set. The next step is to take the array and recombine it as a string. 

1) Begin at the highest index and manually count down, populating an array with each character.
2) Join the array with an empty string as a delimiter, meaning the characters are sequential with nothing between them. 
3) Use the reverse function to reverse an iterator that will be similarly joined by empty strings.
'''
name = 'Jonathan' 
r = "".join(reversed(name))

''' Metodo Dos
The Pythonic way using slice notation. This is a condensed technique that is more specific to Python
as a slice notation is not found in all languages.
'''

'''
Slice notation is a technique unique to Python that allows a shorthand notation within an iterable's 
square brackets, which then executes a traditional slice. 

Slice notation involves two colons and up to three values within the square brackets. 
The first, middle, and end values - separated by colons - are as follows: [start:stop:step]

By omitting the start and stop positions while passing -1 as the step value, we instruct Python to slice 
counting backwards and not to stop before the end of the string. 
'''
name = 'Jonathan' 
print(name[::-1])

#Performance Comparison: According to Dan Bader, slice notation is up to seven times faster than the reverse/join technique.

import timeit

def reverse_join(s):
    return "".join(reversed(s))

def slice_notation(s):
    return s[::-1]

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

reverse_join_times = timeit.repeat(lambda: reverse_join(s))

slice_notation_times = timeit.repeat(lambda: slice_notation(s))

avg_reverse = sum(reverse_join_times)
avg_slice = sum(slice_notation_times)/len(slice_notation_times)

print(avg_reverse)
print(avg_slice)
print(avg_reverse / avg_slice) 