# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 09:51:33 2018

@author: Florian Ulrich Jehn
"""
import math

# Exercise 1
def calc_base(vol, height):
    """
    Calculates the length of one side of the base of a rectangular pyramid,
    given the volumne and height.
    """
    return math.sqrt((3 * vol) / height)

print(calc_base(1000, 18))


# Exercise 2
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod
def a(x, y):
    x = x + 1
    return x * y
def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square
x = 1
y = x + 1
print(c(x, y+3, x+y))


# Exercise 3
def do_twice(f, val):
    """Calls the funktion f with the argument val two times."""
    f(val)
    f(val)
    
def print_twice(to_print):
    """Prints the given parameter twice."""
    print(to_print)
    print(to_print)
    
do_twice(print_twice, "bla")

def do_four(f, val):
    """Calls the funktion f with the argument val four times."""
    do_twice(f, val)
    do_twice(f, val)
    
do_four(print_twice, "that is a lot of printing")


# Exercise 4
def adder():
    """Adds all the numbers the user gives until "done" is typed."""
    print("Type a number or 'done' when finished")
    result = 0
    while True:
        try:
            val = input("Please give input: ")
            if val == "done":
                break
            else:
                result += float(val)
        except ValueError:
            print("Wrong input type")
    return result
print("The result is: " + str(adder()))


# Exercise 5
def collatz(number):
    """Creates the next number in a collatz sequence"""
    if number % 2 == 0:
        return int(number / 2)
    else:
        return int(3 * number + 1)

def prompt_and_run():
    """
    Prompts the user for a starting number for the collatz sequence and 
    prints the sequence.
    """
    number = int(input("Please provide a starting number (int): "))
    print(number)
    while number > 1:
        number = collatz(number)
        print(number)
        
prompt_and_run()

# Exercise 6

n = int(input("Which element of the Fibonacci Sequence do you want to calculate?\nPut in here (int): "))

def fibonacci(n):
    x = 1
    y = 1
    for i in range(n):
        z = x + y
        x = z
        y = x
    print(z)

fibonacci(n)
   
# Exercise 7

import math

def calculation(o, n):
    """This function checks which operation the user wants to run."""

    if o == "a":
       result = squareroot(n)
    elif o == "b":
        result = power2(n)
    elif o == "c":
        result = power3(n)
    else o == "d":
        result = lognaturalis(n)

    if result != None:
        print("The result is " + str(round(result,2)))
    else:
        pass


def squareroot(n):
    """This function calculates the square root of a given number."""
    
    try:
        result = math.sqrt(n)
        return result
    except:
        print("The number you enterd is a negative number")
        return None
    
def power2(n):
    """This function calculates the power of two of a given number."""
    
    result = n**2
    return result

    
def power3(n):
    """This function calculates the power of three of a given number."""
    
    result = n**3
    return result
    
    
def lognaturalis(n):
    """This function calculates the natural logarithm of a given number."""
    
    try:
        result = math.log(n)
        return result
    except:
        print("The number you enterd is eather equal to zero or a negative number")
        return None


while True:
    print("I can do the following operations, please choose:")
    print("a for squareroot")
    print("b for power of 2")
    print("c for power of 3")
    print("d for logarithmus naturalis")
    
    operation = input("enter a, b, c or d to choose a claculation\n")
    
    if operation not in ["a","b","c","d"]:
        print("I can not do that")
        continue
    try:
        number = float(input("enter a number you want to process with\n"))
    except:
        print("This was not a number")
        continue

    calculation(operation, number)

    done = input("Do you want to continue? press y or n\n")
    if done == "n":
        break
                



    

