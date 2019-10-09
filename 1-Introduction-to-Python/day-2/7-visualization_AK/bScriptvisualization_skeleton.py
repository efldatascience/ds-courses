# -*- coding: utf-8 -*-
# @author: Benjamin M. Abdel-Karim
# @since: 2019-10-08
# @version: 2019-10-08

# Import libraries for our data analysis.
import pandas as pd
import matplotlib.pyplot as plt

# Import our data set.
# Check your working directory first.
#os.getcwd()
# Is your file in the directory? What is its name?
#os.listdir()
# Now create a pandas dataframe.
df = pd.read_csv('vgsales.csv', sep=',')

# Let's have a first look at our Dataset! Let's see what attributes/columns we
# have.
# print(df.columns)

# That's quite some columns. How many, actually?
# print(len(df.columns))

# We can also return a tuple representing the dimensionality of the DataFrame,
# to see how many records and columns we have.
# print('Dimensionality of the DataFrame')
df_shape = df.shape
# print(df_shape)

# So that is the number of columns. Great! Still too little information actually.
# I wonder, what datatypes those specific columns are.
# print('info')
df_info = df.info()
# print(df_info)


#########################
### Pre-processing ######
#########################
# Data pre-processing
# Let's check the dataset for missing values.
# @code: 0, or ‘index’ : Drop rows which contain missing values.
# Let's see where the Null values are.
# Let's see the data shape and NaN values.
# This will give number of NaN values in every column.
# print('There are nan')
df_null_values = df.isnull().sum()

# print(df_null_values)
# print('NANs?', df.isnull().sum())
df = df.dropna(axis=0)

#########################
### Visualizations ######
#########################

#########################
### Pie Plot ######
#########################
# First of all, we want a scatter plot. 
# Therefore we need to extract the data. 
# Extract the data by using DataFrame. 
# Access to the data for pie plot. 
# Data frame df['Genre']!
#@code: plt.pie()
LSizes = df['Genre'].value_counts()
LLabels = df['Genre'].value_counts().index

# Try to create a Pie Plot with the data of df['Genre']. 







#########################
### Scatter Plot ######
#########################
# Try to create a scatter plot with the Global Sales and Year Information.
# Now we would like to use Matplotlib .
# Matplotlib is a Python 2D plotting library which produces 
# publication quality figures.  
# Matplotlib can be used in Python scripts
# Let's try it out.
# @code: plt.scatter(LYears, LGlobal_Sales)
# Access to the data for scatter. 








#########################
####### seaborn #########
#########################
# For using seaborn we need to use the bib.
import seaborn as sns

#########################
### Joint Plot ######
#########################
# Try to create a joint plot with the df.Year, df.Global_Sales.
# Use the optional parameters: size=8, ratio=9, color="blue", alpha=0.1
# @code: sns.jointplot










#########################
### Bar Plot ######
#########################
# Access data for the bar plt.
# In our case we need the sum of the 'Global Sales' data for each year.
# @code: df_groupData Grouped data by years and summed up.
# @code: LIndexesOfGroupData years converted as int!









#########################
### Box Plot ######
#########################
# Box plots
# Access data for our box plot. We would like to create the plot 
# for publisher Nintendo. 
dfNintendo = df[df.Publisher == 'Nintendo']

# What is the problem in the plot. 







# Update 2







# Update 3










