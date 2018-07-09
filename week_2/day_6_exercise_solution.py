# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:44:20 2018

@author: Florian Ulrich Jehn
"""
import numpy as np
from sklearn import datasets
import pandas as pd
# Do not worry if those lines confuse you. 
# They are only needed to get some data to work with and you do not need to understand them.
# If you are curious take a look here:
# https://stackoverflow.com/questions/38105539/how-to-convert-a-scikit-learn-dataset-to-a-pandas-dataset
def load_iris():
    """Loads the iris dataset and returns it as a dataframe"""
    iris = datasets.load_iris()
    iris_df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                         columns= iris['feature_names'] + ['target'])
    return iris_df

iris_df = load_iris()


# Exercise 1
# Get the sepal length
print("The minimal sepal length is {} cm".format(iris_df["petal length (cm)"].min()))
# Describe the target 0 group
print(iris_df[iris_df["target"] == 0].describe())
# Create a slice of the last two rows
print(iris_df[-2:])


# Exercise 2
def load_energy():
    """Loads the energy file, skipping all useluss information and returns it as a dataframe"""
    energy = pd.read_excel("Energy Indicators.xls", skiprows=17, header=0,
                           skip_footer=53-15, na_values="...", usecols=[2,3,4,5])
    # Rename columns
    energy.columns = ["Country", "Energy Supply", "Energy Supply per Capita", "% Renewable"]
    
    # Exclude numbers from country names
    energy["Country"] = energy["Country"].str.replace("\d+", "")
    
    # Delete the parentheses
    energy["Country"] = energy["Country"].str.replace("\(.*\)", "")
    
    return energy
    
energy = load_energy()
print(energy.describe())


# Exercise 3
def write_energy(energy):
    """Writes the energy file in a nicer format"""
    energy.to_csv("energy_formatted.csv", index=False, sep=";")
    
write_energy(energy)
    















































