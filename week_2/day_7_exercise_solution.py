# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 15:49:56 2018

@author: Florian Ulrich Jehn
"""
import pandas as pd
import matplotlib.pyplot as plt
# Import seaborn to get nicer plots
import seaborn as sns
import numpy as np
import random


# Exercise 2
x = [random.randint(0,1000) for i in range(1000)]     
y = [random.randint(0,1000) for i in range(1000)]     
plt.scatter(x, y, color="black", alpha=0.5)
plt.close()


# Exercise 3
x = [i for i in range(50)]
y = [3 * i for i in range(50)]
plt.plot(x,y, label="a wonderful line")
plt.title("Draw a line")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()


# Exercise 4
sample = [random.randint(0, 101) for i in range(30)]
plt.boxplot(sample)


# Exercise 5
sample_hist = [random.random() for i in range(1000)]
plt.hist(sample_hist, histtype="step")


# Exercise 6
pokemon = pd.read_csv("pokemon.csv")
plot_attributes = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]
pokemon_plot = pokemon.loc[:, plot_attributes]
plt.boxplot(pokemon_plot.transpose(), labels=plot_attributes)
ax = plt.gca()
ax.set_facecolor("white")
plt.savefig("pokemon_boxplots.png", dpi=200, bbox_inches="tight")
plt.close()


# Exercise 7
# 7.1 
fao = pd.read_csv("FAO.csv", encoding="'latin-1'")
# The codes are understood as numeric, but are categorical
fao["Area Code"] = fao["Area Code"].astype('category')
fao["Item Code"] = fao["Item Code"].astype('category')
fao["Element Code"] = fao["Element Code"].astype('category')
# print(fao.describe(include="all"))


# 7.2
print(list(fao["Item"].unique()))


# 7.3
# Get the data
food = fao.loc[fao["Element"]=="Food",:].sum()[10:]
food.index = food.index.str.replace("Y", "")
feed = fao.loc[fao["Element"]=="Feed",:].sum()[10:]
feed.index = food.index.str.replace("Y", "")

# Plot food and feed. Here I used quite a lot of different formatting, so
# you can see many of the things you can modify

# I usually fix the alpha somewhere in a variable, so I can change it more easily 
# for all the parts where I use it
alpha = 0.6
# Plot the lines
plt.plot(food, label="Food")
plt.plot(feed, label="Feed")
# Get the current axes object
ax = plt.gca()
# Change the rotation of the ticklabels and only show every fourth
plt.xticks(rotation=90)
for i, label in enumerate(ax.xaxis.get_ticklabels()):
    if i % 4 != 0:
        label.set_visible(False)
# Create a label and make it fit in more nicely
legend = plt.legend(frameon = 1)
frame = legend.get_frame()
frame.set_color('white')
frame.set_edgecolor("lightgray")
for text in legend.get_texts():
    plt.setp(text, alpha=alpha)
# Label everything correctly
plt.ylabel("Worldwide Production [tons]", alpha=alpha)
plt.xlabel("Year", alpha=alpha)
plt.title("Comparison of the Production of Food and Feed 1961 to 2013", alpha=alpha)
plt.ticklabel_format(axis = "y", style = 'plain')
# Get a nice grid in the background
ax.set_facecolor("white")
ax.grid(color="grey", alpha=0.1)
# Make the labels nicer to read
plt.setp(ax.get_xticklabels(), alpha=alpha)
plt.setp(ax.yaxis.get_offset_text(), alpha=alpha)
plt.setp(ax.get_yticklabels(), alpha=alpha)
# Change the size of the figure, so it is wider
fig = plt.gcf()
fig.set_size_inches(10, 1.5)
# Finally save the beauty
plt.savefig("worldwide.png", dpi=300, bbox_inches="tight")
plt.close()


# 7.4
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
plt.title("Barley Amount in Afghanistan (1961)")
plt.xlabel("Amount [tons]")
ax.set_facecolor("white")
ax.yaxis.grid(color="grey", alpha=0.3)
plt.savefig("barley.png", dpi=200, bbox_inches="tight")
plt.close()


# 7.5
area_groups = fao.groupby("Area")
# Create an empty dataframe to store the results in
results = pd.DataFrame(np.nan, index=fao["Area"].unique(), columns=["Total Amount"])
# Go through all countries and calculate the total result
for area, area_df in area_groups:
    total = area_df.iloc[:, 10:].sum().sum()
    results.loc[area,:] = total

# Get the results in the right order
results = results.sort_values(by="Total Amount", ascending=False).iloc[:50,:].sort_values(by="Total Amount", ascending=True)

# Plot
results.plot(kind="barh")
ax = plt.gca()
ax.set_facecolor("white")
ax.legend_.remove()
ax.xaxis.grid(color="grey", alpha=0.3, linestyle="-")
plt.ylabel("Country")
plt.xlabel("Total Amount 1961-2013 [tons]")
plt.ticklabel_format(axis = "x", style = 'plain')
plt.xticks(rotation=-15)
fig = plt.gcf()
fig.tight_layout()
fig.set_size_inches(10,10)
plt.savefig("total_amount.png", dpi=300, bbox_inches="tight")
plt.close()


# 7.6
# Get the data
food = fao.loc[fao["Element"]=="Food",:].sum()[10:]
feed = fao.loc[fao["Element"]=="Feed",:].sum()[10:]
# Plot
plt.scatter(food, feed)
ax = plt.gca()
ax.set_facecolor("white")
ax.grid(color="grey", alpha=0.3, linestyle="-")
plt.xlabel("Yearly Food Amount [tons]")
plt.ylabel("Yearly Feed Amount [tons]")
plt.ticklabel_format(style = 'plain')
plt.xticks(rotation=-15)
fig = plt.gcf()
fig.tight_layout()
plt.savefig("scatter_feed_food.png", dpi=200, bbox_inches="tight")
plt.close()


# 7.7
# Create the right column names with list comprehension
late = ["Y" + str(year) for year in range(2000, 2010)]
early = ["Y" + str(year) for year in range(1990, 2000)]
# Get the data
soy = fao.loc[fao["Item"]=="Soyabeans",:]
soy_north_late = soy.loc[soy["latitude"] > 0,:][late].sum().sum()
soy_north_early = soy.loc[soy["latitude"] > 0,:][early].sum().sum()

soy_south_late = soy.loc[soy["latitude"] < 0,:][late].sum().sum()
soy_south_early = soy.loc[soy["latitude"] < 0,:][early].sum().sum()

# Plot in the subplots
fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True)
ax1 = axes[0]
ax2 = axes[1]

ax1.bar(x=["North", "South"], height=[soy_north_early, soy_south_early])
ax1.set_ylabel("Amount [tons]")
ax1.set_title("\n1990-1999")
ax2.bar(x=["North", "South"], height=[soy_north_late, soy_south_late])
ax2.set_title("\n2000-2009")
# Make a title for both
fig.suptitle("Soybean Amount divided  northern and southern hemisphere\n", fontsize=14)
fig.tight_layout()
plt.savefig("soy.png", dpi=200, bbox_inches="tight")
plt.close()


# 7.8
# Get data
oil = fao.loc[fao["Item"].str.contains("Oil"), :].groupby("Area").sum()["Y2000"]
# Plot
plt.hist(oil, bins=45, histtype="step", color="black", linewidth=1)
ax = plt.gca()
ax.set_facecolor("white")
ax.grid(color="grey", alpha=0.3, linestyle="-")
fig = plt.gcf()
fig.tight_layout()
plt.xlabel("Total Amount [tons]")
plt.ylabel("Count")
plt.title("Distribution of the Amount of Food Oil")
plt.savefig("oil.png", dpi=200, bbox_inches="tight")
plt.close()































