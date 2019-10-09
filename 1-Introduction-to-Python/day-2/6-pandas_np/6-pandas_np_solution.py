




# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:19:47 2019

@author: nicol
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

os.getcwd()

# Is your file in the directory? What is its name?

os.listdir()

# read the file via csv commands. Print the first ten rows. 
# You can achieve this by converting the csv.reader into a list and then
# iterating on it.
with open("vgsales.csv", "r") as file: 
    reader = csv.reader(file, delimiter=",")  
    rows = list(reader)
    for i in range(11):
        print(rows[i])
        
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
df = pd.read_csv('vgsales.csv', sep=',')

# Great. Pandas is a very useful package for data analysis. Similar to other
# packages, it does not only come with the very useful DataFrame data structure,
# but also a lot of functions.

# Let's see how many functions pandas actually provides.

print(dir(pd))

# DataFrame functions provide direct and matched operations for DataFrame types.
# List the functions to get an overview.

print(dir(pd.DataFrame))

# Quite overwhelming how powerful pandas appears to be! In the following section,
# we will look at some of these useful functions and features of pandas
# for data analysis purposes. 

# The functions we are going to go through will empower you to:
#   - Get an overview over the dataset
#   - Get descriptive statistics on the dataset
#   - Find first indices for correlations in the dataset


#########################
### Data Exploration ####
#########################

# exploring dataset

#info, datatypes in df

# At first, we have to get a grip of the dataset. Let's print the columns.

print(df.columns)

# That's quite some columns. How many, actually?

print(len(df.columns))

# We can also return a tuple representing the dimensionality of the DataFrame,
# to see how many records and columns we have.
print('Dimensionality of the DataFrame')
df_shape = df.shape
print(df_shape)

# So that is the number of columns. Great! Still too little information actually.
# Let's find out, what datatypes those specific columns are.

print('info')
df_info = df.info()
print(df_info)

# In your very first python session, you learned about primitive datatypes,
# such as int, string, float. Complex datatypes are almost always represented
# as objects. Let's print the column 'Name' with the object datatype, to see
# if it is really complex and why it is labeled as object.

# Try to print the 'Name' column. Attention! There are two obvious ways
# to do this.

print(df.Name)
print(df['Name'])

# As we can see, the object datatype actually contains strings. Pandas
# initially tries to assign datatypes to the various columns, but sometimes it
# does not get the correct type. Why is that so?
# (See: https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#dtypes)
# Citation: Pandas uses the object dtype for storing strings.

# Problem solved. But what about Year? Should it not be int? Print the column.

print(df.Year)
print(df['Year'])

# It should be int, yet it has been assigned float values.
# Again, we find our answer in the pandas documentation
# See: http://pandas-docs.github.io/pandas-docs-travis/user_guide/missing_data.html#integer-dtypes-and-missing-data

# Citation: Because NaN is a float, a column of integers with even 
#           one missing values is cast to floating-point dtype 
#           (see Support for integer NA for more).

# This explains the issue. Let's check for missing values if it is true for
# the dataset.

print('There are missing values')
df_null_values = df.isnull().sum()
print(df_null_values)

# Indeed! We have 271 missing values in the Year column, as well as some in the
# publisher column. 
# We could now decide to drop all the rows, where information
# is missing, try to fill it with sample data (not very useful in our case)
# or drop the column (also not useful).

# Since we have a lot of data, we will drop the rows where year and publisher
# data is missing. Use pd.DataFrame.dropna on our dataframe to drop the
# rows. Then print the info on our dataset again.

df = df.dropna(axis=0)
df.info()

# The 306 records have been dropped, such that we now only have 16291 records.
# It appears that Year is still a float. Let's convert it to int.
# See: https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#astype
# Then print info again.
df['Year'] = df['Year'].astype('int64') 
df.info()

# Great job! You have successfully cleaned your data from rows with missing
# values and converted a column to its correct datatype.
# Let's start with some manipulation and analysis.

# Let's see what the top rows and the bottom rows look like.
#head, bottom
# loc, iloc
# slicing
# getting list, dict from dataset values 

df_head = df.head()
df.tail()

# Get access to the 55 record. There are two options.

df.loc[54]
df.iloc[54]

# While loc searches the index by named labels (such as strings, but also int),
# iloc searches for row number.
# The differentiation of these two will become much clearer when performing
# slicing operations. Remember the slicing operations for strings and lists.
# In our case, the first part of the slice before the comma refers to the
# records (x-axis), the second to the columns (y-axis).

df.iloc[:3, :3]
# This gives us a 3x3 snapshot of the dataframe, starting at the  
# column 0 ( index) and stopping at the column 4 (with index 3)
# does it work the same way with loc?
df.loc[:3, :3]

# Nope. we learned that loc works with 'named' labels. Since the rows do have
# numeric labels and include the number 3, the first part should be fine.
# Let's change the second part to the column label.

df.loc[:2, :'Platform']

# Another example: find the last element 16597 with loc and iloc
df.loc[16597]
df.iloc[16597]
# different story: know that iloc works with indices. We do have a first column
# that is named index, yet is not consistent with our actual dataset index.
# This is sometimes native to the dataset, sometimes caused by record drops.
# 16597 would have been the last element. Let's try to get it another way.
df.iloc[-1]
# Very good. Now, let's clean up the index with this function.
df = df.reset_index(drop=True)


# Let's to some advanced stuff now!
# You have learned about basic datastructures yesterday.
# Retain the a subset of the DataFrame containing the records 10-20 (including 10 and 20)
#and columns Platform - NA_Sales.

# do it with iloc.
df_sliceExample = df.iloc[10:21,2:7]
# do it with loc.
df.loc[10:21,'Platform':'NA_Sales']

# write the contents of the last operation to a dict.
df_slice = df.loc[10:21,'Platform':'NA_Sales']
Dslice = df_slice.to_dict() 

# Hmm... this does not look quite right. We want the rows to be the keys,
# not the columns. Let's see what a df.transpose can do.
df_slice_transposed = df_slice.transpose()
Dslice_transposed = df_slice_transposed.to_dict()

# Perfect, this is what we wanted. What actually just happened?
# By transposing the dataframe, we changed the columns to rows and the rows to
# columns. This can sometimes be very helpful in data analysis, for example
# if you need to convert the data structure or the size of the data structure.
# Especially in Machine Learning and Deep Learning with Neural Nets,
# being able to transpose data structures is an invaluable feature (pun intended).

################# 
## Numpy Intro ##
#################

# A main task in data analysis is calculus and statistics.
# On your first day, you have learned to code basic calculations and
# mathematical functions in python.

# Because more sophisticated mathematical operations require a lot of code
# and are often highly standardizable, packages such as "numpy" reduce your work
# and are ideal for performing mathematical operations on data.

# Numpy brings various features of linear algebra and statistics into python.
# On top of that, it enriches python with flexible datastructures for these
# operations called ndarrays. Fun fact: The Pandas Library and data structures
# are for a large part built on top of numpy!

# Let's try it out.
# We start by initializing a python list along with a numpy ndarray, to show
# the differences.

LexampleLista = [1,2,3,4,5,6,7,8,9]
a_exampleArraya = np.array([1,2,3,4,5,6,7,8,9])

# The datatype of numpy arrays is int32, a very basic datatype.
# This is made so computational efforts are reduced to a minimum.
# Result: Faster computations.
# Yet it does not look so different, does it? Let's make the array multidimensional.

LexampleListb = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
a_exampleArrayb = np.array([[1,2,3,4,5,6,7,8,9],
                          [1,2,3,4,5,6,7,8,9],
                          [1,2,3,4,5,6,7,8,9]])

# This is where the array can shine: While elements within lists need to be
# accessed via indexing, elements in arrays are arranged in tables and can be
# accessed directly. 

# Numpy arrays are also referred to as matrices or vectors, because of their
# mathematical origin and purpose.
    
# Hence, mathematical operations can be performed quite
# easily, fast and on multiple elements.

# Let's multiply all elements by themselves(matrix multiplication)

a_matmul_arraya = np.matmul(a_exampleArrayb,a_exampleArrayb)

# Hmm, this does not look right. Let's look at the error message:
# shapes (3,9) and (3,9) not aligned: 9 (dim 1) != 3 (dim 0)

# Well, this looks like we should use one transpose to get the right shape for
# the data. Since the Pandas DataFrame inherits many functions from 
# the ndarray, transposing is available for the ndarray as well.
# Let's try transposing.

a_matmul_arraya = np.matmul(a_exampleArrayb,
                            a_exampleArrayb.transpose())
print(a_matmul_arraya)
aTransposed =  a_exampleArrayb.transpose()
# This is what happens when we transpose the first parameter. Let's
# transpose the second.

a_matmul_arrayb = np.matmul(a_exampleArrayb.transpose(),
                            a_exampleArrayb)
print(a_matmul_arrayb)

# What just happened? The different transposes resulted in different
# result matrices. This is the typical mathematical behavior of a matrix-
# multiplication: The result matrix has the number of rows of Matrix A
# and the number of columns of matrix B.

# There are also element-wise operations possible. Similar to simple
# python lists, ndarray elements are also accessible by indices.

# Let's access the elements and perform operations.
# Access the element at 0,0 and print it. Then add three to it and
# assign the new value. Finally multiply all elements by 3 and assign
# the new value to the matrix.

print( a_matmul_arraya[0,0])

a_matmul_arraya[0,0] = a_matmul_arraya[0,0] +3

a_matmul_arraya = a_matmul_arraya *3

######################################################
## From Numpy to Descriptive Statistics with Pandas ##
######################################################


# Numpy has a multitude of different functions that are useful as well.
# Many of these functions are also inherited by the pandas packages
# and the pandas Dataframe, such as several functions for 
# descriptive statistics.

a_matmul_arraya.mean()
a_matmul_arraya.max()
a_matmul_arraya.min()
np.quantile(a_matmul_arraya,0.75)
np.quantile(a_matmul_arraya,0.50)
np.quantile(a_matmul_arraya,0.25)
np.std(a_matmul_arraya)
np.count(a_matmul_arraya)

#descriptive stats
# Try to find these functions within the pandas package and perform them on
# our dataframe!

df_mean = df.mean()
df_max = df.max()
df_min = df.max()
df_q3 = df.quantile(q=0.75)
df_qmed = df.quantile(q=0.50)
df_q1 = df.quantile(q=0.25)
df_std = df.std()
df_count = df.count()

# There are also important aggregate functions that deliver the most
# interesting desc. stats at once.

df_description = df.describe()

# To find first hints on how features (another name for our attributes or
# columns that is used in data analysis) correlate, use the correlation
# function.

df_corr = df.corr()