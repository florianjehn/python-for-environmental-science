# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:44:20 2018

@author: Florian Ulrich Jehn
"""
import numpy as np
from sklearn import datasets
import pandas as pd
import random

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
import pandas as pd
def load_energy():
    """Loads the energy file, skipping all useluss information and returns it as a dataframe"""
    energy = pd.read_excel("Energy Indicators.xls", skiprows=17, header=0,
                           skip_footer=53-15, na_values="...", usecols=[2,3,4,5])
    # Rename columns
    #energy.columns = ["Country", "Energy Supply [Petajoules]", "Energy Supply per Capita [Gigajoules]", "% Renewable"]
    
    # Exclude numbers from country names
   # energy["Country"] = energy["Country"].str.replace("\d+", "")
    
    # Delete the parentheses
   # energy["Country"] = energy["Country"].str.replace("\(.*\)", "")
    
    return energy
    
energy = load_energy()
print(energy)


# Exercise 3
def write_energy(energy):
    """Writes the energy file in a nicer format"""
    energy.to_csv("energy_formatted.csv", index=False, sep=";")
    
write_energy(energy)
    

# Exercise 4
energy = pd.read_csv("energy_formatted.csv", sep=";")

# Print the last 5 countries
print(energy.iloc[-5:, :])

# Display the mean values for all columns that begin with 'A'
a_countries = energy.loc[energy["Country"].str.startswith("A"), :]
print(a_countries.mean())

# Display the renewable energy production of the countries 50 to 100 in ascending order.
countries_50_to_100 = energy.iloc[50:100, :]
renewables = countries_50_to_100["% Renewable"]
sorted_countries = sorted(renewables)
print(sorted_countries)


# Exercise 5
pokemon = pd.read_csv("pokemon.csv")
# Print all the names
grouped_pokemon = pokemon.groupby("Type 1")
for group_name, group_df in grouped_pokemon:
    print("Type 1: {}".format(group_name))
    print(group_df.iloc[:10,:]["Name"])
    
# Create the dictionary
poke_dict = {}
for group_name, group_df in grouped_pokemon:
    poke_dict[group_name] = group_df
    
# Print the pokemon amounts in each group
for group_name, group_df in grouped_pokemon:
    print("Type: {}; Amount: {}".format(
            group_name, group_df.count()[0]))
    
    
# Exercise 6
def create_dfs():
    """Creates several small dataframes and returns them in a list"""
    df_list = []
    for i in range(3):
        df = pd.DataFrame({
            "probe": [1, 2, 3],
            "humidity": [random.random(), random.random(), random.random()],
            "temperature": [random.randint(-100,100), random.randint(-100,100), random.randint(-100,100)]
        })
        df_list.append(df)
    return df_list

df_list = create_dfs()

# Concat
print("\nBy Row")
print(pd.concat(df_list, axis=0))

print("\nBy Column")
print(pd.concat(df_list, axis=1))


# Exercise 7
df1 = pd.DataFrame({
            "probe": [1, 2, 3],
            "humidity": [random.random(), random.random(), random.random()],
        })
df2 = pd.DataFrame({
            "probe": [1, 2, 3, 4],
            "temperature": [random.randint(-100,100), random.randint(-100,100), 
                            random.randint(-100,100), random.randint(-100,100)]
        })
merged = pd.merge(df1, df2, on="probe", how="outer")
print(merged)













































