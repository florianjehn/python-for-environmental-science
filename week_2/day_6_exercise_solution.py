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

