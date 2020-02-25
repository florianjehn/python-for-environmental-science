# -*- coding: utf-8 -*-
"""
Created on Jun 08 10:11 2018
@author(s): Florian U. Jehn
"""
# Exercise 1
for i in range(1,11):
    print(i)
    
# Exercise 2
import time
seconds = time.time()
minutes = seconds / 60
print(str(minutes) +" minutes have passed since epoch")

# Exercise 3
s1 = 10
s2 = 5 
s3 = 100

if s1 > s2 + s3:
    print("Does not work")
elif s2 > s1 + s3:
    print("Does not work")
elif s3 > s1 + s2:
    print("Does not work")
else:
    print("Perfectly good triangle")
    
# Exercise 4
for i in range(1,8):
    print(str(i) * i)    
    
# Exercise 5
month = "jan"
if month == "jan":
    print(31)
elif month == "feb":
    print(28)
elif month == "mar":
    print (31)
elif month == "apr":
    print(30)
elif month == "may":
    print(31)
elif month == "jun":
    print(30)
elif month == "jul":
    print(31)
elif month == "aug":
    print(31)
elif month == "sep":
    print(30)
elif month == "oct":
    print(31)
elif month == "nov":
    print(30)
elif month == "dec":
    print(31)
else:
    print("you gave me no month")
    

# Exercise 6
my_miles = 10
marathon = 42
training_days = 0
while my_miles < marathon:
    my_miles *= 1.1
    training_days += 1
print("I need to train " + str(training_days) + " days")
    

# Exercise 7
vacation_price = float(input("How expensive should the holiday be? "))
save_frac = float(input("How much of your monthly salary do you want to save? "))
annual_salary = float(input("How large is your annual salary? "))
monthly_salary = annual_salary / 12
current_savings = 0
month = 0
# r is the interest rate (here 4 %)
r = 0.04
while current_savings < vacation_price:
    # Add a month
    month += 1
    # calculate the monthly saving
    returns = current_savings * (r/12)
    print(returns)
    monthly_savings = monthly_salary * save_frac
    current_savings = current_savings + monthly_savings + returns
print("You need to save for " + str(month) + " months to afford your holiday.")
    
# Exercise 8
import random

number = 20
guesses = 0

random_number = random.randint(1, number+1)

while True:
    guesses += 1
    guess = int(input("Take a guess!\n"))
    if guess == random_number:
        print("YOU WIN!!!")
        print("It took you " + str(guesses) + " guesses.")
        break
    elif guess < random_number:
        print("Your guess was too low.")
    else:
        print("Your guess was too high.")
        
# Exercise 9
import os
print(os.name)
import platform
print(platform.system())
print(platform.release())

# Exercise 10
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

# Exercise 11
for i in range(0,7):
    if i == 3 or i == 6:
        continue
    print(i)
    
# Exercise 12
a = float(input("Side a? "))
b = float(input("Side b? "))
c = float(input("Side c? "))

if a == b == c:
    print("Equilateral")
elif a != b and a != c and b != c:
    print("Scalene")
else:
    print("Isosceles")

# Exercise 13
import string
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
while True:
    pw = input("Give me a good password! ")
    # Check the length
    if len(pw) < 5 or len(pw) > 17:
        print("Not a good password!")
        continue
    
    # Check for upper case and lowercase and specials
    lower_in = False
    upper_in = False
    digits_in = False
    for char in pw:
        if char in lower:
            lower_in = True
            continue
        if char in upper:
            upper_in = True
            continue
        if char in digits:
            digits_in = True
            
    if not lower_in or not upper_in or not digits:
        print("Not a good password!")
        continue 
    
    # The program only gets here when everything above was correct
    print("Good Job. You created a nice password!")
    break



    
    



    
