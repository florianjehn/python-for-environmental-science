# -*- coding: utf-8 -*-
"""
Created on Jun 08 10:11 2018
@author(s): Florian U. Jehn
"""
# Exercise 1 
word = input("Word please!")
if len(word) > 4:
    print(word)
    if len(word) == 5:
        print("You choose a fine word, sir!")
print(len(word))

# Exercise 2
for i in range(1,11):
    print(i)
    
# Exercise 3
import time
seconds = time.time()
minutes = seconds / 60
print(str(minutes) +" minutes have passed since epoch")

# Exercise 4
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
    
# Exercise 5
for i in range(1,8):
    print(str(i) * i)    
    
# Exercise 6
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
    monthly_savings = monthly_salary * save_frac
    current_savings = current_savings + monthly_savings + returns
print("You need to save for " + str(month) + " month to afford you holiday.")
    
    
    
    
    



    
