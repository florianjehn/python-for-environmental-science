# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 09:39:55 2018

@author: Florian Ulrich Jehn
"""
import datetime
import time
import dateutil


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
    while (datetime.datetime.now() - start).seconds < 10:
        print("Hello")
        time.sleep(0.7)
        
# print_n_pause()


# Exercise 5
def bday_timer(bday):
    """Tells how old you are and how long it is till your next birthday."""
    # Calculate the age
    today = datetime.datetime.today()
    age = dateutil.relativedelta.relativedelta(today, bday)
    age = age.years
    print("Your age is {} years".format(age))
    # Calculate the time till the next birthday
    # Normalize the birthday to get a timedelta
    bday_changed_year = datetime.datetime(today.year, bday.month, bday.day)
    # Calculate the difference to the birthday
    till_bday = today - bday_changed_year
    # Check if the the bday already was this year
    if till_bday.days < 0:
        print("Only {} days until your birthday".format(- till_bday.days))
    else:
        bday_changed_year = datetime.datetime(bday_changed_year.year + 1, 
                                              bday_changed_year.month, 
                                              bday_changed_year.day)
        till_bday = bday_changed_year - today
        print("Only {} days until your next birthday".format(till_bday.days))
    
bday = datetime.datetime(1989, 12, 23)
bday_timer(bday)


# Exercise 6
def double_day(bday1, bday2):
    """Calculates the day when one person is double as old as the other one"""
    if bday1 > bday2:
        delta = bday1 - bday2
        double_day = bday1 + delta
    else:
        delta = bday2 - bday1
        double_day = bday2 + delta
    return double_day

bday1 = datetime.date(1990, 8, 31)
bday2 = datetime.date(1989, 12, 23)
double_day = double_day(bday1, bday2)
print("The double day of {} and {} is {}".format(bday1, bday2, double_day))
    
































        