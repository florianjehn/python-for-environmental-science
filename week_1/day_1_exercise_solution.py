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
print("x raised to the power of y is " + str(x ** y))

# Exercise 6
a = int(input("Enter a number:\n"))
b = int(input("Enter another number:\n"))

print("Division " + str(a / b))
print("Integer Division " + str(a // b))
print("Remainder " + str(a % b))

# Exercise 7
n= int(input("Enter the number you want to check: "))
print("The remainder is: " + str(n % 7))
print("If the remainder is 0 your number is divisible completely")

# Exercise 8
first = float(input("Number please: "))
second = float(input("Number please: "))
third = float(input("Number please: "))
print("Multiplying the first number by the second number and dividing by the third")
print("Result: " + str((first * second) / third))

# Exercise 9
import math
radius = float(input("Radius please: "))
circum = math.pi * radius * 2
print("Given a radius of " + str(radius) + ", the circle has a circumference of " + str(circum))