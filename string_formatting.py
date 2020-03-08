"""
Created on Sat Mar 7 11:55:40 2019

#How to format strings in Python 

@author: tomwsullivan, with some parts adapted from @rayde
"""

#String: A sequence of character data. Text Data. 
    #Properties: Iterable, enumerable

#Iterable: Can be looped over

#Enumerable: A data type that can be counted over. Structured order.

#There are many ways of formatting and displaying strings in Python. It is straightforward when we have 
#the entire string hard-coded into the program

forest = 'forest'
car = 'red car'
#in these strings we know the entire text before the program starts
#but what if we want to include some variable in the string? Or some value when we don't know it in advance?
#Let's say we want to get the user's name and then print it out

#There are numerous ways we can do this. All these look the same to the user, so we must think from the 
#perspective of the programmer.

def say_hello(name):
    print('hello', name)

say_hello(name='Thomas')

def say_hello2(name):
    print('hello' + ' ' + name) #string concatenation, note the blank space we need to add

say_hello2(name='Thomas')

#We can also format strings using the format method
def say_hello3(name):
    print('hello {0}'.format(name))

#The {0} tells the program that this is the first space it needs to fill, and the .format() method
#specifies self.name as the variable in its place
    
say_hello3(name='Thomas')

#This works well, but what if we have two variables

def describe_student(name, class_, grade): #notice how we use class_ because class is a reserved word
    print('{0} is currently taking {1} with a grade of {2}'.format(name, class_, grade))

describe_student(name='Joanna', class_='Python', grade='A')

#This works just fine, but it produces an awefully long line of code. 
#We can address this by placing an "f" before the string

def describe_student2(name, class_, grade):
    print(f'{name} is currently taking {class_} with a grade of {grade}')

#The result is exactly the same, but the line of code is much shorter. Take a look for yourself:

describe_student2(name='Joanna', class_='Python', grade='A')

#This approach is both simpler for the user, and recommended by most large tech companies as easier to read
#Any of these approaches will work in your code. Still, we should try to learn the best ways of coding
#if it is easier for us and is approved by the community!
