# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:29:57 2019

@author: Nicolas Pfeuffer
"""

# Import libraries for our data analysis.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy  as np
import os

# Import our data set.

# Check your working directory first.
os.getcwd()
# Is your file in the directory? What is its name?
os.listdir()
# Now create a pandas dataframe.
df = pd.read_csv('dataset_small.csv', sep=',')

# Let's have a first look at our Dataset! Let's see what attributes/columns we
# have.

print(...)

# That's quite some columns. How many, actually?

print(...)

# We can also return a tuple representing the dimensionality of the DataFrame,
# to see how many records and columns we have.
print('Dimensionality of the DataFrame')
df_shape = ...
print(...)

# So that is the number of columns. Great! Still too little information actually.
# I wonder, what datatypes those specific columns are.

print('info')
df_info = ...
print(...)


# Now we're talking. We do have a lot of float values. Also some 'object' types.
# This resembles the look of categorical values, which we might have to convert
# to numericals for our statistics later. A more intruiging problem is that some
# attributes appear to have no records. This describes NaN/Null Values.
# Let's see where the Null values are.

# Let's see the data shape and NaN values.
# This will give number of NaN values in every column.

print('There are nan')
df_null_values = ...
print(...)

# Some attributes are droppable, since they to not provide any value to us.
# Let's drop these attributes. This will reduce computational complexity and
# improve clarity of our dataset.

df = ....(columns=[...,...,...,...])

# Now that we have taken care of this issue, we can proceed with our analysis.
# Why did we not drop the other attributes containing NaN values? Because they
# still might be insightful.

# Let's have a deeper look at the top 5 records now
# to get a better feeling for the dataset.


# DataFrame Manipulations: Remember to save manipulated states as variables,
# so you can look them up again or work on their basis.

# Use the head function from df object to get the top 5 records.

print('Show head')
df_top = ...
print(...)

# It looks like these are too many columns to show at once.
# Let's use a slice to only show the attributes between 'loan_amnt' and 'grade'
# Remember, we want to see the rows 1-5.

# Slicing and indexing

df_top_slice = df.loc[1:5,"loan_amnt":"grade"]
print(...)

# We already see in this subsample, that the loan_amounts greatly diverge.
# Furthermore, the interest rates are also quite different. Referring to our
# research questions, we could take a short look at the different interest
# rates and and loan_amounts.

# Maximum, Minimum measures

print(df.int_rate....)
print(df.int_rate....)

# Dataset subselection, similar to SQL statements
# We want to show a subset of the dataframe, where the loan_amnt is >16000 $
# and the int_rate is higher than 28 %..

subselect_df = df[(...) & (...)]
print(subselect_df[[...,...]])


# We can see that in this relatively high interest rate area only low credit
# score ratings are present. We see, that the general ratings('grade') 
#also have a 'sub_grade'. We will take a closer look at these two.

# Grouping is a way to arrange the data accordingly.
# Group by the the attribute 'sub_grade' and provide the mean score.
# sub_grade: The specific subclass of a credit score rating, i.e. A - A1,A2...

df_sub_grade = ...
print(df_sub_grade)

# Group by the the attribute 'grade'. 

df_grade = ...
print(df_grade)

# Would it not also be interesting to see, what kind of purposes people 
# get a loan for? Let's find out by getting (1) the number of unique values for the
#'purpose' attribute, then the values. Print them.

# Return Series with number of distinct observations. Can ignore NaN values.
print(df['purpose']. ...)

# initialize a list with unique values of the dataframe object and print it.
Lunique_purpose = df['purpose']. ...
print(Lunique_purpose)

# That is quite a list of purposes. What are the average sums of the loans?
# Initialize a dictionary for the purpose of holding the mean loan sum
# per loan purpose. Then print it.

Dmean_purpose = dict()

for ... in ...:
    Dmean_purpose[...] = df[... == ...].loan_amnt.mean()

print(Dmean_purpose)

# Here we can see that there are both larger investments, such as 'car' 
# and 'small_business', but also seemingly smaller investments, 
# such as 'vacation'.

#### Final part of this section ####

# Now that we got a grip and first understanding of the dataset, 
# we will view some sample descriptive statistics to gain further insights 
# for statistical relations in our data.
    
# Print simple stats
print('Simple stats')
df_description = ...
print(df_description)


# Finally, we want to get an overview over insightful correlations. This will
# bring us a step forward in answering our research questions.

corr = ...
corr.style.background_gradient(cmap=='coolwarm')

# As we can see, the categorical variables will not show up. This is because
# they are of the object type. Yet we want to see especially the correlations
# of the credit score ratings. Let's convert them and rerun our analysis.
# Convert the 'grade' and 'sub_grade'
# object types to categorical, then apply codes to category.

for col_name in df.columns:
    if((df[...].dtype == 'object')& (col_name in ['grade','sub_grade'])):
        df[...]= df[...].astype('category')
        df[...]= df[...].cat.codes

corr = ...
corr.style.background_gradient(cmap='coolwarm')


# Great! We have found first evidence about a correlation between important 
# attributes in our lending system! We will further investigate from here on
# using visualizations.

