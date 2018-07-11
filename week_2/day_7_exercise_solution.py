# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 15:49:56 2018

@author: Florian Ulrich Jehn
"""
import pandas as pd
import matplotlib.pyplot as plt


# Exercise 1


# Exercise 2


# Exercise 3
fao = pd.read_csv("FAO.csv", encoding="'latin-1'")
# The code are understood as numeric, but are categorical
fao["Area Code"] = fao["Area Code"].astype('category')
fao["Item Code"] = fao["Item Code"].astype('category')
fao["Element Code"] = fao["Element Code"].astype('category')

print(fao.describe(include="all"))
print(list(fao["Item"].unique()))
