# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 15:49:56 2018

@author: Florian Ulrich Jehn
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Exercise 2
pokemon = pd.read_csv("pokemon.csv")
plot_attributes = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]
pokemon_plot = pokemon.loc[:, plot_attributes]
plt.boxplot(pokemon_plot.transpose(), labels=plot_attributes)
ax = plt.gca()
ax.set_facecolor("white")
plt.savefig("pokemon_boxplots.png", dpi=200, bbox_inches="tight")
plt.close()


# Exercise 3

# 3.1 
fao = pd.read_csv("FAO.csv", encoding="'latin-1'")
# The code are understood as numeric, but are categorical
fao["Area Code"] = fao["Area Code"].astype('category')
fao["Item Code"] = fao["Item Code"].astype('category')
fao["Element Code"] = fao["Element Code"].astype('category')
# print(fao.describe(include="all"))

# 3.2
# print(list(fao["Item"].unique()))

# 3.3
# Get the data
food = fao.loc[fao["Element"]=="Food",:].sum()[10:]
feed = fao.loc[fao["Element"]=="Feed",:].sum()[10:]
# Plot
plt.plot(food, label="Food")
plt.plot(feed, label="Feed")
plt.xticks(rotation=90)
plt.legend(frameon=True)
plt.ylabel("Worldwide Production [tons]")
ax = plt.gca()
ax.set_facecolor("white")
ax.grid(color="grey", alpha=0.3)
plt.savefig("worldwide_production.png", dpi=300, bbox_inches="tight")
plt.close()

# 3.4
# Get the food value
barley_food_A = fao.loc[fao["Element"]=="Food",:]
barley_food_A = barley_food_A.loc[barley_food_A["Item"]=="Barley and products",:]
barley_food_A = barley_food_A.loc[barley_food_A["Area"]=="Afghanistan",:]
barley_food_A = barley_food_A["Y1961"]
barley_food_A = float(barley_food_A)
# Get the feed value
barley_feed_A = fao.loc[fao["Element"]=="Feed",:]
barley_feed_A = barley_feed_A.loc[barley_feed_A["Item"]=="Barley and products",:]
barley_feed_A = barley_feed_A.loc[barley_feed_A["Area"]=="Afghanistan",:]
barley_feed_A = barley_feed_A["Y1961"]
barley_feed_A = float(barley_feed_A)

# Plot
plt.bar(["Food", "Feed"], [barley_food_A, barley_feed_A])
ax = plt.gca()
plt.title("Barley Production in Afghanistan (1961)")
plt.xlabel("Production [tons]")
ax.set_facecolor("white")
ax.yaxis.grid(color="grey", alpha=0.3)
plt.savefig("barley.png", dpi=200, bbox_inches="tight")
plt.close()







