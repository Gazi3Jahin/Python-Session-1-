#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Python Basics: Variables and Data Types

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script is designed to teach you the basics of variables and data types in Python.
We will cover:
1. What variables are and how to use them.
2. The basic data types in Python.
3. Variable naming conventions and industry standards.
4. Python's dynamic typing feature.

Each section includes explanations, examples, and assignments to reinforce your learning.
"""

# Section 1: Variables
# ---------------------
# Variables are containers for storing data values. In Python, a variable is created the moment you first assign a value to it.

# Example 1: Creating Variables
x = 5
y = "Hello, Python learners!"

# You can print the variables to see their values.
# print(x)
# print(y)

# Assignment 1: Create two variables, one holding a number and the other holding your name. Then print both.
# Write your code below:
age = 23
name = "Gazi Jahin"

print("Age: ", age, end="; ")
print("Name: ", name)

# Section 2: Data Types
# ---------------------
# Python has various data types including integers, float (decimal numbers), strings, booleans, and more.

# Example 2: Data Types
a = 5               # int
b = 3.14            # float
c = "Python"        # str
d = True            # bool

# You can check the type of any variable by using the type() function.
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Assignment 2: Create variables of different types and use the type() function to check their types.
# Write your code below:

my_integer = 33

my_float = 3.14

my_string = "Hello, world!"

my_boolean = True

my_list = [1, 2, 3, 4, 5]

my_tuple = (1, 2, 3)

my_dict = {"name": "Jahin", "age": 20}

print("Type of my_integer:", type(my_integer))
print("Type of my_float:", type(my_float))
print("Type of my_string:", type(my_string))
print("Type of my_boolean:", type(my_boolean))
print("Type of my_list:", type(my_list))
print("Type of my_tuple:", type(my_tuple))
print("Type of my_dict:", type(my_dict))


# Section 3: Variable Naming Conventions and Industry Standards
# -------------------------------------------------------------
"""
Variable names should be:
- Clear and descriptive.
- Start with a letter or an underscore.
- Only contain alpha-numeric characters and underscores (A-z, 0-9, and _).
- Case-sensitive (age, Age, and AGE are different variables).

Industry standards often follow the 'snake_case' naming style for variables in Python.
"""

# Example 3: Good and Bad Variable Names
good_name = "John"
_bad_name = 23
# 2bad = 42  # This will raise a SyntaxError because variable names cannot begin with a number.

# Assignment 3: Fix the bad variable name above and create three more variables with good naming practices.
# Write your code below:
good_name = "John"
age = 42
pi_value = 3.14
message = "Hello, world!"

# Section 4: Python's Dynamic Typing
# ----------------------------------
# Python is dynamically typed, which means you don’t have to declare the type of variable while declaring it.

# Example 4: Dynamic Typing
var = "I am a string"
print(var)

var = 42
print(var)

# The variable 'var' changes type from str to int, demonstrating Python's dynamic typing.

# Assignment 4: Create a variable, assign it a value of one type, then reassign it to a different type and print both.
# Write your code below:
# Assigning a value of one type

my_variable = 2024
print("Original value:", my_variable)

my_variable = "Happy New Year!"
print("New value:", my_variable)


# Congratulations on completing this part of the Python workshop!
# Review the assignments, try to solve them, and check your understanding of variables and data types.


# In[ ]:




