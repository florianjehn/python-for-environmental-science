# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 09:39:55 2018

@author: Florian Ulrich Jehn
"""
import datetime
import time
import dateutil
import random
import os


# Exercise 1
def count_char(char, word):
    """Counts the characters in word"""
    return word.count(char)
    # If you want to do it manually try a for loop

print(count_char("a", "banana"))


# Exercise 2
def is_anagram(w1, w2):
    """
    Determines if w1 and w2 are anagrams
    """
    return (sorted(first.upper()) == sorted(second.upper()))

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
    """Prints hello for 10 seconds and makes pauses in between"""
    start = datetime.datetime.now()
    while (datetime.datetime.now() - start).seconds < 10:
        print("Hello")
        time.sleep(0.7)
        
print_n_pause()


# Exercise 5
import datetime
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
    """Calculates the day when one person is twice as old as the other one"""
    if bday1 > bday2:
        delta = bday1 - bday2
        double_day = bday1 + delta
    else:
        delta = bday2 - bday1
        double_day = bday2 + delta
    return double_day

bday1 = datetime.date(1990, 1, 9)
bday2 = datetime.date(1989, 12, 23)
double_day = double_day(bday1, bday2)
print("The double day of {} and {} is {}".format(bday1, bday2, double_day))
    

# Exercise 7
def create_files():
    """Creates the specified files"""
    for i in range(10):
        num = random.random()
        # Pause to allow the timestamp to change. 
        time.sleep(0.01)
        now = time.time()
        # Use 'with' to make reading and writing easier.  
        with open(str(now) +  ".txt", "w", encoding='utf-8') as outfile:
            outfile.write(str(num))
            
create_files()
        
        
# Exercise 8
def rewrite_files():
    for file in os.listdir():
        # Only consider txts
        if file[-3:] == "txt":
            with open(file, "r") as infile:
                # Determine the new value               
                num = float(infile.readline())
                out_num = 1 if num > 0.5 else 0
                # Get the date
                timestamp = file[:-4]
                date = datetime.datetime.fromtimestamp(float(timestamp))
                # Write the files
                with open(str(num) + ".txt", "w", encoding='utf-8') as outfile:
                    outfile.write(str(date) + "\n\n\n" + str(out_num))
                    
rewrite_files()































        
