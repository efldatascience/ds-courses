# -*- coding: utf-8 -*-
"""
Remember: Either assign the results of your code statements to a variable 
or print them out on the console by wrapping your code statement with "print()".
"""

# Import libraries for our data analysis.
import os
import pandas as pd
import numpy  as np
import csv


######################################
### Data Import and Pandas Intro  ####
######################################


# Import our data set.
# Check your working directory first.
#%%
print("Current working directory:", os.getcwd())
#%%
# Is your file in the directory? What is its name?

print("Files located in the directory:", os.listdir())

#%%
# Change your working directory to where the file is, if the file is not in the current directory
os.chdir(r"...")

#%%
# read the file via csv commands. Print the first ten rows. 
# You can achieve this by converting the csv.reader into a list and then
# iterating on it.
with open("...", "r") as file: 
    reader = csv.reader(file, delimiter=",")  
    rows = list(reader)
    for i in range(...):
        print(rows[i])
 #%%       
# Now we could do some simple operations on the file.
# Since we want to do a lot of data exploration and analysis, this would only
# result in burdensome work and unreadable code. 
# Therefore, this does not help us much.
        
# Another option would be to load the data into a dictionary or list with
# sub- datastructures. This would also get very burdensome and computationally
# inefficient.
    
# Thankfully, there is pandas. Pandas allows us to load files of various
# file types into a data structure called DataFrame.
# This gives us a persistent datastructure to work with and perform our 
# analyses on. 
# DataFrames represent data in a tabular way, much like excel sheets.
# DataFrames therefore consist of rows and columns. Columns are called 
# 'Series' and are a subordinate data structure - that holds a column of data.
# Rows contain the actual data.

# Fantastic! Let's read our csv into a pandas DataFrame.

# Now create a pandas dataframe.
df = ...
#%%
# Great. Pandas is a very useful package for data analysis. Similar to other
# packages, it does not only come with the very useful DataFrame data structure,
# but also a lot of functions.

# Let's see how many functions pandas actually provides.

print(...)
#%%
# DataFrame functions provide direct and matched operations for DataFrame types.
# List the functions to get an overview.

print(...)

# Quite overwhelming how powerful pandas appears to be! In the following section,
# we will look at some of these useful functions and features of pandas
# for data analysis purposes. 

# The functions we are going to go through will empower you to:
#   - Get an overview over the dataset
#   - Get descriptive statistics on the dataset
#   - Find first indices for correlations in the dataset

#%%
#########################
### Data Exploration ####
#########################

# exploring dataset

#info, datatypes in df

# At first, we have to get a grip of the dataset. Let's print the columns.

print(df...)
#%%
# That's quite some columns. How many, actually?

print(...(df...))
#%%
# We can also return a tuple representing the dimensionality of the DataFrame,
# to see how many records and columns we have.
print('Dimensionality of the DataFrame')
df_shape = ...
print(...)
#%%
# So that is the number of columns. Great! Still too little information actually.
# Let's find out, what datatypes those specific columns are.

print('info')
df_info = df....
print(...)
#%%
# In your very first python session, you learned about primitive datatypes,
# such as int, string, float. Complex datatypes are almost always represented
# as objects. Let's print the column 'Name' with the object datatype, to see
# if it is really complex and why it is labeled as object.

# Try to print the 'Name' column. Attention! There are two obvious ways
# to do this.

print(df...)
print(df...)
#%%
# As we can see, the object datatype actually contains strings. Pandas
# initially tries to assign datatypes to the various columns, but sometimes it
# does not get the correct type. Why is that so?
# (See: https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#dtypes)
# Citation: Pandas uses the object dtype for storing strings.

# Problem solved. But what about Year? Should it not be int? Print the column.

print(df...)
print(df...)
#%%
# It should be int, yet it has been assigned float values.
# Again, we find our answer in the pandas documentation
# See: http://pandas-docs.github.io/pandas-docs-travis/user_guide/missing_data.html#integer-dtypes-and-missing-data

# Citation: Because NaN is a float, a column of integers with even 
#           one missing values is cast to floating-point dtype 
#           (see Support for integer NA for more).

# This explains the issue. Let's check for missing values if it is true for
# the dataset.

print('There are missing values')
df_null_values = df....
print(...)
#%%
# Indeed! We have 271 missing values in the Year column, as well as some in the
# publisher column. 
# We could now decide to drop all the rows, where information
# is missing, try to fill it with sample data (not very useful in our case)
# or drop the column (also not useful).

# Since we have a lot of data, we will drop the rows where year and publisher
# data is missing. Use pd.DataFrame.dropna on our dataframe to drop the
# rows. Then print the info on our dataset again.

df = df....(axis=0)
df...()
#%%
# The 306 records have been dropped, such that we now only have 16291 records.
# It appears that Year is still a float. Let's convert it to int.
# See: https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#astype
# Then print info again.
df['Year'] = df['Year']....('int64') 
df.info()
#%%
# Great job! You have successfully cleaned your data from rows with missing
# values and converted a column to its correct datatype.
# Let's start with some manipulation and analysis.

# Let's see what the top rows and the bottom rows look like.


df....()
#%%
df....()
#%%
# Get access to the 55 record. There are two options.

df....

#%%
df....
#%%
# While loc searches the index by named labels (such as strings, but also int),
# iloc searches for row number.
# The differentiation of these two will become much clearer when performing
# slicing operations. Remember the slicing operations for strings and lists.
# In our case, the first part of the slice before the comma refers to the
# records (x-axis), the second to the columns (y-axis).

df_slice_1 = df....
#%%
# This gives us a 3x3 snapshot of the dataframe, starting at the  
# column 0 ( index) and stopping at the column 4 (with index 3)
# does it work the same way with loc? Print the result.
df.... 
#%%
# Nope. we learned that loc works with 'named' labels. Since the rows do have
# numeric labels and include the number 3, the first part should be fine.
# Let's change the second part to the column label. Print the result.

df.... 
#%%
# Another example: find the last element with the ID 16597 with loc and iloc
# Print the result.
df....
#%% Print the result.
df....
#%%
# different story: know that iloc works with indices. We do have a first column
# that is named index, yet is not consistent with our actual dataset index.
# This is sometimes native to the dataset, sometimes caused by record drops.
# 16597 would have been the last element. Let's try to get it another way.
# Print the result.
df....

#%%
# Very good. Now, let's clean up the index with this function.
df = df.reset_index(drop=True)

#%%
# Let's to some advanced stuff now!
# You have learned about basic datastructures yesterday.
# Retain the a subset of the DataFrame containing the records 10-20 (including 10 and 20)
#and columns Platform - NA_Sales.

# do it with iloc.
df.iloc[...]
#%%
# do it with loc.
df.loc[...]
#%%
# write the contents of the last operation to a dict. 
# You will see there is a helpful function for writing a df to a dict.
df_slice = df.loc[...]
Dslice = df_slice....
#%%
# Hmm... this does not look quite right. We want the rows to be the keys,
# not the columns. Let's see what a df.transpose can do.
df_slice_transposed = df_slice....
Dslice_transposed = df_slice_transposed....
#%%
# Perfect, this is what we wanted. What actually just happened?
# By transposing the dataframe, we changed the columns to rows and the rows to
# columns. This can sometimes be very helpful in data analysis, for example
# if you need to convert the data structure or the size of the data structure.
# Especially in Machine Learning and Deep Learning with Neural Nets,
# being able to transpose data structures is an invaluable feature (pun intended).
#%%

######################################################
##  Descriptive Statistics with Pandas ##
######################################################


# Numpy has a multitude of different functions that are useful as well.
# Many of these functions are also inherited by the pandas packages
# and the pandas Dataframe, such as several functions for 
# descriptive statistics.

#descriptive stats
# Try to find these functions within the pandas package and perform them on
# our dataframe!

df_mean = df....()
#%%
df_max = df....()
#%%
df_min = df....()
#%%
df_q3 = df....()
#%%
df_qmed = df....()
#%%
df_q1 = df....()
#%%
df_std = df....()
#%%
df_count = df...()
#%%

# There are also important aggregate functions that deliver the most
# interesting desc. stats at once.

df_description = df.describe()
#%%
# To find first hints on how features (another name for our attributes or
# columns that is used in data analysis) correlate, use the correlation
# function.

df_corr = df.corr()