# module_example.py
# This is a simple Python module to demonstrate basic usage

def greet(name):
    return f"Hello, {name}!"

def square(x):
    return x * x


# main_program.py

# Importing the custom module
import module_example

# Using functions from the custom module
print(module_example.greet("Alice"))
print(module_example.square(4))


import math

# Using the math module from the Standard Library
radius = 5
area = math.pi * radius ** 2
print(f"The area of a circle with radius {radius} is {area:.2f}")


