# Assignment 4

"""Title: Write python code that loads any dataset from (www.data.gov.in), and does some basic data cleaning. Add component
on data set. """

# imports the library

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the csv file
df=pd.read_csv('Salary.csv')
print(df.head())

# show column name in the dataset
print(df.columns)

# show the index in dataset
print(df.index)

# statistical operation
print(df.describe())

# show count of dataset
print(df.count(axis=0))
# show shape of dataset
print(df.shape)

# datatypes
print(df.dtypes)

# dataframe converted to numpy array
print(df.to_numpy())

# Transpose of matrix
print(df.T)

# sorting data in reverse order axis =0 = row
print(df.sort_index(axis=0, ascending=False))

# sorting data in reverse order axis =1 = column
print(df.sort_index(axis=1, ascending=False))

# find info of all dataset
print(df.info)

# changing / Set the columns name
df.columns = list(["sr_no","Experience","Salary"])
print(df.head())

# Checking the Missing value

#print(df['Experiecnce'].isnull())

# drop some columns or row value (axis =0 -> row, axis =1 ->columns)

print(df.drop(0,axis=0))

# print some specific value
print(df.loc[[1,2],['Experience','Salary']])

# slicing
print(df.loc[20:,['Experience','Salary']])

# modified value to NONE
df['Salary'] = None
print(df['Salary'])

print(df['Salary'].isnull())

# checking NA value
print(df.isna())

