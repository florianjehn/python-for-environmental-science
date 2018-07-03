# -*- coding: utf-8 -*-
"""
Created on Jun 07 16:11 2018
@author(s): Florian U. Jehn
"""
import math

# Exercise 1
print("Hello there")
name = input("What is your name? ")
print("Hello " + name)
print("Your name has " + str(len(name)) + " letters")
height = float(input("What is your height? "))
height *= 25
print("Your height times 25 is " + str(height))

# Exercise 2
side = "*       *"
print(side)
print(side)
print(side)
print(side)
print(side)
print(side)
bottom = "* * * * *"
print(bottom)

# Exercise 3
word = input("Give me a word! ")
print(word[0])

# Exercise 4
celsius = 40
fahrenheit = 1.8 * celsius + 32
print(fahrenheit)

# Exercise 5
x = float(input("What is the value of x? "))
y = float(input("What is the value of y? "))
print("x raised to the power of y is " + str(x**y))
print("log (base 2) of x is " + str(math.log2(x)))