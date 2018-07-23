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

# Exercise 6
a = int(input("Enter a number:\n"))
b = int(input("Enter another number:\n"))

remainder_1 = a % b 
decimal_1 = remainder_1 * 10 // b
remainder_2 = remainder_1 * 10 % b
decimal_2 = remainder_2 * 10 // b
remainder_3 = remainder_2 * 10 % b
decimal_3 = remainder_3 * 10 // b

print("The remainder of {} / {} is:".format(a, b)) # Or print("The remainder of " +str(a) + "/" + str(b) + " is:")
result = str(decimal_1) + str(decimal_2) + str(decimal_3)
print(result)

# Exercise 7
n= int(input("Enter the number you want to check: "))
print("The remainder is: " + str(n % 7))
print("If the remainder is 0 your number is divisible completely")
