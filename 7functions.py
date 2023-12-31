# -*- coding: utf-8 -*-
"""7functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zbldTZuB06UKq1AnvQCKSXfneyXGd1pN
"""

# 7functions.py

# 7.1 Functions

# 7.1.1 Create a function named function1 that prints this string "Hello World"
# TODO: Write your code below
def function1():
    print("Hello World")

# 7.1.2 Execute the functon function1
# TODO: Write your code below
function1()

# 7.1.3 Create a function named function2 that takes in one integer parameter number1. The function adds 5 to the input number1, and prints the result
# TODO: Write your code below
def function2(number):
    print(number+5)

function2(234)
# 7.1.4 Create a function named compare_numbers() with two arguments. If the first argument is greater than the second, print "first number is greater".
# If the second number is greater than the first, print "first number is smaller". Is the numbers are equal, print "equal numbers"
# TODO: Write your code below
def compara_numbers():
    x, y = int(input())
    a, b = 0
    if x == y:
        print("equal numbers")
    if x > y:
        a, b = x, y
    elif y > x:
        a,b = y, x

    print(f"{a} is greater than {b}")

# 7.2 Create a lambda function that takes one parameter (a) and returns it.
# TODO: Write your code below
function3 = lambda a:a
print(function3("Eric"))

### 7.3 Python built-in functions : https://www.w3schools.com/python/python_ref_functions.asp
nums = [11,33,14,2,58,65,34]
# 7.3.1 Using Python's built in sum() function, print the sum of the numbers in the list nums
# TODO: Write your code below
print(sum(nums))

# 7.3.2 Using Python's built in min() function, print the minimum of the numbers in the list nums
# TODO: Write your code below
print(min(nums))

# 7.3.3 Using Python's built in abs() function, print the absolute value of -6.
# TODO: Write your code below
print(abs(-6))

# 7.3.4 Using Python's built in round() function, round the number 4.67888 to two decomal places.
# TODO: Write your code below
print(round(4.67888,2))

# 7.4 Python Modules
# HINT: https://www.w3schools.com/python/python_modules.asp
# HINT: https://realpython.com/python-modules-packages/
# HINT: https://docs.python.org/3/tutorial/modules.html


# 7.4.1 Create a python module mod.
# In mod.py, create a function psum(number1, number2) that takes two arguments and prints the sum of them. Assume the input arguments to be numbers.
# In mod.py, create a function pmultiply(number1, number2) that takes two arguments and prints the product of them. Assume the input arguments to be numbers.
def psum(number1, number2):
    print(number1 + number2)
def pmultiply(number1, number2):
    print(number1 * number2)

# 7.4.2 Create python file main.py and import the module mod.
# In main.py run the psum() and pmultiply() functions from the module mod using any two numbers.
#import mod as mod
psum(123,5)
pmultiply(23,4)

# 7.4.3 In main.py, also import Python's built in modul