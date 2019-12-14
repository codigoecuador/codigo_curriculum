# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:35:14 2019

@author: rayde
https://www.kdnuggets.com/2019/12/python-dictionary-methods.html
"""

# Define a dictionary code: A key value pair is connected in a dictionary. 
# for example: here, 'person' is a key and 'a human being' is a value. 
webstersDict = {'person': 'a human being',
                'marathon': 'a running race that is about 26 miles',
                'resist': 'to remain strong against the force',
                'run': 'to move with haste; act quickly'}

'''
The dictionary webstersDict used strings as keys in the dictionary, but dictionary keys can be any immutable data type (numbers, strings, tuples etc). Dictionary values can be just about anything (int, lists, functions, strings, etc).

For example, the dictionary below, genderDict has ints as keys and strings as values.
'''

# Define a dictionary
genderDict = {0: 'male',
              1: 'female'}

'''
An important point to emphasize is that if you try to make a key a mutable datatype (like a list), you will get an error.
'''
# Failure to define a dictionary
webstersDict = {(1, 2.0): 'tuples can be keys',
                1: 'ints can be keys',
                'run': 'strings can be keys', 
                ['sock', 1, 2.0]: 'lists can NOT be keys'}

'''

Access Values in a Dictionary
 
To access a dictionary value, you can use square brackets [].

For example, the code below uses the key ‘marathon’ to access the value ‘a running race that is about 26 miles’.

'''
# Get value of the 'marathon' key
webstersDict['marathon']

'''
Keep in mind that you will get a KeyError if you try to access a value for a key that does not exist.

# Try to get value for key that does not exist
'''
webstersDict['nonexistentKey']

'''
In the Dictionary Methods section, you will see the utility of using the dictionary method get to avoid KeyErrors.
'''

'''
Add, Update, and Delete Keys from a Dictionary
 

Add or Update Key
 
You can add a new key-value pair.
'''
# add one new key value pair to a dictionary
webstersDict['shoe'] = 'an external covering for the human foot'

'''
In the Dictionary Methods section, you will see that you can also add or update multiple key value pairs at a time using the dictionary update method.
'''

'''

Delete Keys from Dictionary
 
It is possible to remove a key and its corresponding value from a dictionary using del.

'''
# Remove the key 'resist' from the dictionary
del webstersDict['resist']

'''
In the Dictionary Methods section, you will see that you can also delete keys using the dictionary pop method.

 
'''

'''
Dictionary Methods
 
Python dictionaries have different methods that help you modify a dictionary. 
This section of the tutorial just goes over various python dictionary methods.

update method
 
The update method is very useful for updating multiple key values pairs at a time. 
It takes a dictionary as an argument.
'''
# Using update method to add two key value pairs at once
webstersDict.update({'ran': 'past tense of run',
                     'shoes': 'plural of shoe'})
'''
get method
 
'''
# Define a dictionary
storyCount = {'is': 100,
              'the': 90,
              'Michael': 12,
              'runs': 5}

'''
The get method returns a value for a given key. If a key doesn’t exist, the dictionary will by default return None.

# Since the key 'Michael' exists, it will return the value 12
'''
storyCount.get('Michael')

'''

Since the key ‘Michael’ exists, it returns the value 12. If ‘Michael’ didn’t exist, it would return None.

The method is very useful to look up keys you don’t know are in the dictionary to avoid KeyErrors.


'''


# Make default value for key that doesn't exist 0.
storyCount.get('chicken', 0)

'''
pop Method
 
The pop method removes a key and returns the value.
'''
storyCount.pop('the')

'''

keys Method
 
The keys method returns the keys of the dictionary.
'''
storyCount.keys()

'''
values Method
 
The values method returns the values in the dictionary.
'''
storyCount.values()

'''

items Method
 
The items method returns a list like object of tuples where each tuple is of the form (key, value).
'''
webstersDict.items()
'''
Iterate through a Dictionary
 
You can iterate through the keys of a dictionary by using a for loop.
'''
for key in storyCount:
   print(key)
   
'''
You also iterate through the keys of a dictionary by using the keys method.
'''
for key in storyCount.keys():
   print(key)

'''
The for loop below uses the items method to access one (key, value) pair on each iteration of the loop.
'''
for key, value in webstersDict.items():
    print(key, value)
    
'''
 If you have difficulty understanding this section, I recommend watching the following video.
'''