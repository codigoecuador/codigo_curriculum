# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:53:07 2019

@author: rayde

https://towardsdatascience.com/using-magic-methods-in-python-48f31685bc18
http://www.kr41.net/2016/03-23-dont_inherit_python_builtin_dict_type.html

"""

'''
What are magic methods?

They're everything in object-oriented Python. They're special methods
that you can define to add "magic" to your classes. They're always surrounded by double underscores, 
for example __init__. They're also not as well documented as they should be. All of the magic methods for Python
appear in the same section in the Python docs, but they are scattered about and only loosly organized. There's hardly an example to be found in that section.
'''
#Creating a dict object that can only accept integers and floats as values

'''
In this lesson, we will create a class that creates dictionary objects, that only accept either integers or floats as values. 

If any other data types like strings lists or tuples are added as a value to our custom dictionary object, an exception will be raised, 
specifying to the user that this custom dict object can only accept integers and floats as it's values.

In order to implement this, we will make use of the following magic methods: 
    
   1) __int__
   2)__setitem__  
   3) __str__
    
To begin, we will first create a custom class called customintfloat, 
and we will pass dict into the argument inheritance list.
'''
#create a custom class called customintfloat
#pass dict into the argument inheritance list.

class CustomIntFloat(dict):

    '''
    Python Inheritance allows us to define a class that inherits all the methods 
    and properties from another class.
    
        Parent class is the class being inherited from, also called base class.
    
        Child class is the class that inherits from another class, also called derived class.
    
    In this case, dict is the parent class and CustomIntFloat is the child class.
    For more on inheritance, please read: https://www.w3schools.com/python/python_inheritance.asp
    
    Because CustomIntFloat inherits properties from the built-in python dict class, 
    it will act like a dictionary, except in the places where we choose to selectively 
    modify this behavior. 
    
    '''
    #create an empty dictionary to store the objects.
    empty_dict = {}

    '''
    We can then define an __init__ method to construct the CustomIntFloat object. 
    This object takes a key and a value as arguments. 
    The default for each of these arguments is None. 

    '''
    #define an __init__ method taking the default self argument 
    #add two other arguments called key and value.
    #set the default of key and value to None
    
    def __init__(self, key=None, value=None):
        '''
            If a user does not pass any values into the method, 
            it will create an empty dictionary via the 
            if key is none conditional
            
        '''
        # Define a conditional telling the method to create an empty dict object if None is passed as key.

        if key is None:
            CustomIntFloat.empty_dict = {}
        
            # Define an alternative where if there is only one key passed of value integer or float, use the setitem method
            '''
            Following on, if the user specifies a key of length one, and a corresponding value that 
            is an instance of the int or float class, the key and the value will be set in the object.
            '''    
        elif len(key) == 1 and isinstance(value, (int, float)):
            dict.__setitem__(self, key, value)

        # Define a third alternative where if the len(key) is greater than 1, zip the key/value arguments together. 

        else:
            '''
            Finally, in the else statement, if the user specifies multiple keys and values as an 
            iterable, the iterables will be zipped by the zip function and assigned the variable name 
            zipped. 
            '''
            zipped = zip(key, value)
            #create a loop to iterate over zipped. 
            for tup in zipped:
                '''
                Loop over zipped and check that the value is of type int or float. 
                If it is not, a custom CustomIntFloatError exception is raised.
                '''
                #check if values are integers or floats. and set items if they are. 
                if isinstance(tup[1], (int, float)):
                    dict.__setitem__(self, tup[0], tup[1])
                #if the values are not int or floats, raise a value error. We will create our value error in a minute
                else:
                    
                    raise CustomIntFloatError(tup[1])
    
    #Let's overwrite the default setitem method to check if the value is an integer or a float. If Not, raise a value error. If so, then return the dictionary. 
    def __setitem__(self, key, value):
        '''
        __setitem__ is a magic method that is invoked when we set a key and a 
        value in the dictionary. Once the CustomIntFloat object has been constructed, 
        if the user attempts to add a value that is not of type int or float, the same 
        CustomIntFloatError exception will be raised. I have included a code snippet below 
        that shows how to set a key and a value as intended.

        Parameters
        ----------
        key : A dictionary key, located in index 0 of the tuple, tup[0]
        value : A dictionary value, assigned to a key, located in index 1 of a tuple, tup[1]

        Raises
        ------
        CustomIntFloatError
            The CustomIntFloatError Exception class and the __str__ magic method. As you can see the parent 
            class is Exception, which is a built-in python method to tell the program to bypass an error or 
            do something when a particular error occurs.

        Returns
        -------
        A key value pair in a dictionary

        '''
        if not isinstance(value, (int, float)):
            raise CustomIntFloatError(value)
        return dict.__setitem__(self, key, value)

'''
The CustomIntFloatError Exception class and the __str__ magic method. As you can see the parent 
class is Exception, which is a built-in python method to tell the program to bypass an error or 
do something when a particular error occurs. 
'''
class CustomIntFloatError(Exception):
    '''
    Pretty much every class you create will have an __init__ method except in very rare cases which 
    we will not discuss here. 
    
    We will create an __init__ function which takes the default self argument and 
    an argument named value. 
    
    We will also create an attribute called "self.value" equal to the value argument. 
    That way, when we call the CustomIntFloatError class, we can easily refer back to 
    and look up the value we pass into the class. 
    
    The method will input the value of the tuple and return an error letting the user know that the value is invalid
    because it is not a tuple or a float.
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        '''
        This method returns a string, hence the name __str__!
        When invalid input is specified, the CustomIntFloatError exception is raised 
        and the object is not constructed. 
        A useful error message informs the user that only integers and floats are valid values.

        Returns
        -------
        string, str
            return the self.value attribute and a set string to tell the user that only integers and floats are valid values. 
        '''
        return self.value + ' is not valid\nOnly Integers and floats are valid values \nin CustomIntFloat(dict) '


if __name__ == "__main__":
    
    x = CustomIntFloat('a', 1)
    print(type(x))
    
    x['b'] = 2.1
    print(x)
    # x['c'] = 'Three'