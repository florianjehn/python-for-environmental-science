# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 14:42:42 2018

@author: Florian Ulrich Jehn
"""
import random


# Exercise 1
def middle(a):
    """Returns a (list) without the first and last element"""
    return a[1:-1]

print(middle([1,2,3]))


# Exercise 2
def is_sorted(a):
    """Evaluates if a is sorted or not."""
    a_sorted = sorted(a)
    if a_sorted == a:
        return True
    else:
        return False

print(is_sorted([1,2,2]))


# Exercise 3
def has_duplicates(a):
    """Evaluates if a list has duplicates"""
    if sorted(a) == sorted(list(set(a))):
        return False
    else:
        return True
    
print(has_duplicates([1,2,2]))
print(has_duplicates([1,3,4]))


# Exercise 4
def count_till_tuple(a):
    """Counts the elements until a tuple is in the list and returns the number"""
    counter = 0
    for item in a:
        if type(item) == tuple:
            break
        else: 
            counter += 1
    return counter

print(count_till_tuple([1, 3, "bla", (1,2)]))


# Exercise 5
def generate_bdays(num_bdays):
    """Generates n birthdays and returns them as a list"""
    bdays = []
    for bday in range(num_bdays):
        bdays.append(random.randint(1, 365))
    return bdays

def calculate_probability(rep, num_bdays):
    """
    Calculates the probability of that in a certain number of birthdays
    several people have birthday on the same day.
    """
    matches = 0
    for i in range(rep):
        bdays = generate_bdays(num_bdays)
        if has_duplicates(bdays):
            matches += 1
    return (matches / rep) * 100

print(calculate_probability(10000, 23))


# Exercise 6
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inv):
    """Displays the contents of the inventory."""
    print("Inventory:")
    for item, amount in inv.items():
        print(amount, item)
        
display_inventory(inv)


# Exercise 7
def add_to_inventory(inventory, added_items):
    """Updates inventory by added_items."""
    for item in added_items:
        # Check if the item is already in the inventory
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory
    
inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)

# Exercise 8

test = { x : x**2 for x in range(10)}

print(test)


# Exercise 9

import math

a = [0.6014,0.6031,0.6143,0.6247,0.6239,0.6251,0.6289,0.6344,0.6378,0.6383,0.6372,0.6361,0.6316,
     0.6271,0.6247,0.6272,0.6296,0.6278,0.6256,0.6263,0.6297,0.6344,0.6381,0.6432,0.6452,0.6375,
     0.6281,0.6204,0.6216,0.6149,0.6147,0.6134,0.6255,0.6311,0.6333,0.6298,0.6295,0.6377,0.6409,
     0.6427,0.6369,0.6366,0.6340,0.6345,0.6358,0.6392,0.6373,0.6327,0.6214,0.6161,0.6123,0.6202,
     0.6269,0.6317,0.6298,0.6280,0.6323,0.6303,0.6275,0.6203,0.6198,0.6202,0.6206,0.6224,0.6247,
     0.6265,0.6246,0.6223,0.6205,0.6173,0.6129,0.6086,0.6074,0.6108,0.6084,0.6073,0.6022,0.6041,
     0.6004,0.5958,0.5891,0.5862,0.5911,0.6011,0.6082,0.6052,0.5976,0.5946,0.5964,0.6000,0.5984,
     0.5950,0.5913,0.5910,0.5908,0.5883,0.5885,0.5887,0.5914,0.5891,0.5865,0.5839,0.5847,0.5859,
     0.5850,0.5829,0.5815,0.5877,0.5945,0.5996,0.5993,0.5983,0.6002,0.5992,0.5985,0.5959,0.5962,
     0.5969,0.5976,0.5982,0.6020,0.6002,0.5984,0.5893,0.5858,0.5905,0.5990,0.6075,0.6034,0.5990,
     0.5932,0.5912,0.5880,0.5826,0.5768,0.5737,0.5782,0.5853,0.5918,0.6014,0.6093,0.6164,0.6175,
     0.6140,0.5911,0.6011,0.6082,0.6052,0.5976,0.5946,0.5964,0.6298,0.6280,0.6323]

b = [0.4562,0.4518,0.4532,0.4473,0.4478,0.4360,0.4389,0.4346,0.4395,0.4325,0.4293,0.4307,0.4363,
     0.4431,0.4455,0.4380,0.4292,0.4230,0.4255,0.4280,0.4269,0.4226,0.4184,0.4169,0.4261,0.4277,0.4273,
     0.4193,0.4189,0.4184,0.4169,0.4153,0.4192,0.4240,0.4269,0.4218,0.4147,0.4116,0.4136,0.4176,0.4190,
     0.4167,0.4096,0.4079,0.4036,0.4072,0.4059,0.4101,0.4119,0.4135,0.4140,0.4106,0.4068,0.4023,0.3993,
     0.3967,0.3963,0.4024,0.4086,0.4180,0.4228,0.4228,0.4096,0.3933,0.3817,0.3894,0.4002,0.4110,0.4058,
     0.4057,0.4155,0.4304,0.4329,0.4226,0.4123,0.4093,0.4070,0.4048,0.4062,0.4099,0.4135,0.4134,0.4133,
     0.4116,0.4096,0.4077,0.4075,0.4071,0.4062,0.4056,0.4053,0.4053,0.4097,0.4141,0.4186,0.4129,0.4141,
     0.3996,0.4021,0.3949,0.4033,0.4003,0.4003,0.4005,0.4007,0.4003,0.3996,0.4041,0.4094,0.4042,0.3919,
     0.3815,0.3768,0.3755,0.3709,0.3725,0.3714,0.3720,0.3709,0.3720,0.3731,0.3743,0.3732,0.3702,0.3672,
     0.3661,0.3691,0.3734,0.3769,0.3783,0.3741,0.3688,0.3601,0.3591,0.3556,0.3577,0.3549,0.3557,0.3543,
     0.3583,0.3623,0.3663,0.3637,0.3617,0.3590,0.3582,0.3564,0.3534]


def calc_mean(data):
    """This function calculates the mean of a given numerous list and returns it."""
    
    summ = 0
    for i in data:
        summ += i
    mean = summ/len(data)
    return mean

def calc_var(data):
    """This function calculates the variance of a given numerous list and returns it."""
    
    mean = calc_mean(data)
    saq = 0
    for i in data:
        saq += (i - mean)**2
    var = 1 /(len(data)-1) * saq
    return var

def calc_psd(data1,data2):
    """This function calculates the pooled standard deviation of two given numerous lists and returns it."""
    
    n1 = len(data1)
    n2 = len(data2)
    psd = math.sqrt(((n1-1) * calc_var(data1) +  (n2-1) * calc_var(data2)) / (n1 + n2 - 2))
    return psd

def calc_t(data1, data2):
    """This is the main function of this program and it calculates the absolute t-value of
       two given numerous lists and returns it.
    """
    t = abs((calc_mean(data1) - calc_mean(data2)) / (calc_psd(data1,data2) * math.sqrt(1 / len(data1) + 1 / len(data2))))
    return t


    
print("The calculated t-value is " + str(calc_t(a,b)))
print("The degree of freedom is " + str(len(a)+len(b)-2))

































        
        
    

        
        
