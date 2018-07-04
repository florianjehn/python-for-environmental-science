# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 09:39:55 2018

@author: Florian Ulrich Jehn
"""
import datetime
import time


# Exercise 1
def count_char(char, word):
    """Counts the characters in word"""
    return word.count(char)
    # If you want to do it manually try a for loop

print(count_char("a", "banana"))


# Exercise 2
def is_anagram(w1, w2):
    """Determines if w1 and w2 are anagrams"""
    if len(w1) != len(w2):
        return False
    else:
        for char in w1:
            if char not in w2:
                return False
        return True

print(is_anagram("beer", "bree"))
print(is_anagram("beer", "banana"))
print(is_anagram("beer", "five"))


# Exercise 3
def transform(string):
    """
    Capitalizes string, deletes all whitespaces and counts the len of the 
    product.
    """
    string = string.upper()
    string = string.replace(" ", "")
    length = len(string)
    return (string, length)

print(transform("This is a sentence!"))


# Exercise 4
def print_n_pause():
    """Prints hello 10 seconds longs and makes pauses in between"""
    start = datetime.datetime.now()
    while (datetime.datetime.now() - start).seconds < 1:
        print("Hello")
        time.sleep(0.7)
        
print_n_pause()


# Exercise 5
def bday_timer(bday):
    """Tells how old you are and how long it is till your next birthday."""
    age = (datetime.datetime.now()- bday).years
    print("Your age is {} years".format(age))
    
bday = datetime.datetime(1989, 12, 23)
bday_timer(bday)
































        