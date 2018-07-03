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




































        
        
    

        
        
