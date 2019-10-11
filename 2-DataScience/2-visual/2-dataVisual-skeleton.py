# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:29:57 2019

@author: Benjamin M. Abdel-Karim
"""

# Import libraries for our data analysis.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy  as np
import os


#########################
## Import the data set ##
#########################
# Import our data set.
# Check your working directory first.
# Is your file in the directory? What is its name?
# Now create a pandas dataframe.
#df = pd.read_csv('dataset_small.csv', sep=',')
os.getcwd()
os.listdir()
df = pd.read_csv('../dataset_small.csv', sep=',')

# Let's have a first look at our Dataset! 
# Let's see what attributes/columns we have. 
# That's quite some columns. How many, actually?
# We can also return a tuple representing the dimensionality 
# of the DataFrame, to see how many records and columns we have.
# So that is the number of columns. Great! Still too little 
# information actually. I wonder, what datatypes those specific columns are.
# So that is the number of columns. 
# Great! Still too little information actually.
# I wonder, what datatypes those specific columns are.
print(df.columns)
print(len(df.columns))
print('Dimensionality of the DataFrame')
print(df.shape)
print(df.info())

#########################
## Pre-Processing ##
#########################
# Data preprocessing is an important step in the data mining process. 
# The phrase "garbage in, garbage out" is particularly applicable 
# to data mining and machine learning projects. 
# So that is the number of columns. Great! Still too little information actually.
# I wonder, what data types those specific columns are.
# Now we're talking. We do have a lot of float values.
# Warning: This plot requires relatively much computing time. 

# plt.figure(figsize=(15,5))
# sns.heatmap(df.isnull(), cbar=False, yticklabels=False, cmap='winter')
# plt.xticks(rotation=45, fontsize=6)
# plt.tight_layout()
# plt.savefig('figures/MissingValues.png')
# plt.show()
# plt.close()

# Summ all NaN Values
df_null_values = df.isnull().sum()
print(df_null_values)

# Drop all useless columns
# Some attributes are droppable, since they do not provide any value to us.
# Let's drop these attributes. This will reduce computational complexity and
# improve clarity of our dataset.
df = df.drop(columns=['id','member_id','url','desc'])

# Fill NA/NaN values using the specified method.
df = df.fillna(0)


#########################
## Overview ##
#########################
# Get all colums with numeric values
dfNum = df._get_numeric_data()
print(dfNum.columns)

# Plot pairwise relationships in a dataset.
# Warning: This plot requires relatively much computing time. 
# Therefore here only a small selection of data

# plt.figure()
# sns.pairplot(df[['loan_amnt', 'int_rate', 'installment', 'annual_inc', 'dti']])
# plt.savefig('figures/Pairplot.pdf')
# plt.show()


#########################
### Countplot ####
#########################
# Question: What is the purpose distribution of loans?
# Why is this question relevant?
# Show the counts of observations in each category.
# bin using bars.
#plt.figure()
#ax = sns.countplot(x='purpose', data=df)
#plt.savefig('figures/Purpose.png')
#plt.show()
#
## Upgrade
#plt.figure()
#ax = sns.countplot(x='purpose', data=df, palette='Greys')
#plt.xticks(rotation=45, fontsize=6)
#plt.xlabel('Purpose')
#plt.ylabel('Count')
#plt.title('Purpose of Use')
#plt.tight_layout()
#plt.savefig('figures/PurposeImprove.png')
#plt.show()
#
#
##########################
#### Boxplot ####
##########################
## Why is this question relevant?
## Update Box plot
## Question: Loan amount by class
#plt.figure()
#sns.boxplot(x='grade', y='loan_amnt', data=df)
#plt.savefig('figures/GradesLoanAmnt.png')
#plt.show()
#
## Upgrade
#plt.figure()
#sns.boxplot(x='grade', y='loan_amnt', data=df, showfliers=False, palette='Greys')
#plt.xticks(rotation=45, fontsize=6)
#plt.title('Loan Amount by Class')
#plt.savefig('figures/GradesLoanAmntImprove.png')
#plt.show()
#
##########################
#### plot.bar ####
##########################
## Selected all loan status.
#print(df['loan_status'].unique())
#
#bad_indicators = ['Charged Off',
#                    'Default',
#                    'Does not meet the credit policy. Status:Charged Off',
#                    'In Grace Period',
#                    'Default Receiver',
#                    'Late (16-30 days)',
#                    'Late (31-120 days)']
#
## Define a bad loan in our DataFrame.
## Add all bad loans in our DataFrame.
#df['bad_loan'] = 0
#df.loc[df.loan_status.isin(bad_indicators), 'bad_loan'] = 1
#dict_risk = df.groupby(['grade'])['bad_loan'].mean().sort_values().to_dict()
#print(dict_risk)
#
#plt.figure()
#df.groupby(['grade'])['bad_loan'].mean().sort_values().plot.bar()
#plt.ylabel('Percentage of Bad Debt')
#plt.savefig('figures/RiskProfil.png')
#plt.show()
#
#
##########################
#### Distribution ####
##########################
## Distribution of interest
## Create a Distplot for the fixed acidity in the data set. 
## What does the data distribution tell us? 
## @code: plt.subplots() for access the axes in the code. 
## @code: ax.spines['right'].set_visible(False) mute the draw line.
#
#fig, ax = plt.subplots()
#sns.distplot(df['int_rate'])
#plt.title('Distribution Interest')
#plt.xlabel('int_rate')
#plt.ylabel('Distribution')
#ax.spines['right'].set_visible(False)
#ax.spines['top'].set_visible(False)
#plt.savefig('figures/Distplot.png')
#plt.show()
#
#
## Advance Filtering with DataFrame.
## 1. Calculate the median of the interest rate.
## 2. Define the two classes lower and bigger than the median
## @code: dIntRateMedian = df['int_rate'].median()
## 3. Set a threshold value: lower and bigger than the median
## @code: bins = ( df['int_rate'].min(), dIntRateMedian, df['int_rate'].max())
## Filtering Int_Rate by given classes with the:
## @code:  pd.cut() method.
## than median and higher than median.
## 4. Add the new interest class information to the df frame. 
#
#LGroup_IntRate = ['lower', 'higher']
#dIntRateMedian = df['int_rate'].median()
#bins = (df['int_rate'].min(), dIntRateMedian, df['int_rate'].max())
#df['IntRateLH'] = pd.cut(df['int_rate'], bins = bins, labels = LGroup_IntRate)
#
## Generate a sub plot for detail view about the two new classes of int_rate.
## Therefore we filter for variable A based on the criterion of variable B. 
## @code: df['A'][df[B]=='criterion'] 
#
#fig, ax = plt.subplots(1, 2)
#sns.distplot( df['int_rate'][df['IntRateLH']=='lower'], ax=ax[0])
#sns.distplot( df['int_rate'][df['IntRateLH']!='lower'], ax=ax[1])
#ax[0].spines['right'].set_visible(False)
#ax[0].spines['top'].set_visible(False)
#ax[1].spines['right'].set_visible(False)
#ax[1].spines['top'].set_visible(False)
#ax[0].set_ylabel('Distribution')
#ax[1].set_ylabel('Distribution')
#plt.savefig('figures/SubPlotDistplot.png')
#
#
#
##########################
#### Boxplot ####
##########################
## Question: Loan interest by class
## Why is this question relevant?
#plt.figure()
#sns.boxplot(x='grade', y='int_rate', data=df)
#plt.savefig('figures/GradesIntRate.png')
#plt.show()
#
## Final 
#plt.figure()
#sns.boxplot(x='grade', y='int_rate', data=df,
#            showfliers=False, palette='Blues',
#            order=['A', 'B', 'C', 'D', 'E', 'F', 'G'])
#plt.xticks(rotation=45, fontsize=6)
#plt.title('Interest Rat and Grade in Order')
#plt.savefig('figures/GradesIntRateOrder.png')
#plt.show()
#
#
##########################
#### Heatmap ####
##########################
## Create a Heatmap for corr()
##  # or df.loc[:, ['C', 'D', 'E']
## Rember data: 
## loanAmnt = The listed amount of the loan applied for by the borrower. 
## If at some point in time, the credit department 
## reduces the loan amount, then it will be reflected in this value.
#
## installment = The monthly payment 
## owed by the borrower if the loan originates.
#
## annualInc	= The self-reported annual income provided 
## by the borrower during registration.
#
## dti = A ratio calculated using the borrower’s total monthly 
## debt payments on the total debt obligations, 
## excluding mortgage and the requested LC loan, 
## divided by the borrower’s self-reported monthly income.
#df_ForCorr = df[['loan_amnt', 'int_rate', 'installment', 'annual_inc', 'dti']]
#corr = df_ForCorr.corr()
#
## Create 
#plt.figure
#sns.heatmap(corr, 
#        xticklabels=corr.columns,
#        yticklabels=corr.columns, annot=True)
#plt.savefig('figures/CoreHeatmap.pdf')
#plt.show()
#
#
## Update the corr plot with mask
## Generate a mask for the upper triangle
## @source: https://seaborn.pydata.org/examples/many_pairwise_correlations.html
#plt.figure()
#mask = np.zeros_like(corr, dtype=np.bool)
#mask[np.triu_indices_from(mask)] = True
#sns.heatmap(corr, 
#        xticklabels=corr.columns,
#        yticklabels=corr.columns, annot=True, mask=mask)
#plt.savefig('figures/CoreHeatmapUpdate.pdf')
#plt.show()
#
#
##########################
#### cloroplot ####
##########################
## More Plots here
## cloroplot
## We define a function for plotting the data on a cloropleth plot. A cloropleth
## plot allows us to plot data on an (interactive) map. Why a function?
## Because we will use it multiple times, so we make our code cleaner.
#
#state_mean = pd.DataFrame(df.groupby('addr_state')['loan_amnt'].mean())
#from plotly.offline import plot
#import plotly.graph_objects as go
#
#def cloroplot(data, z, title):
#    fig = go.Figure(data=go.Choropleth(
#        locations=data.index,  # Spatial coordinates
#        z=data[z].astype(float),  # Data to be color-coded
#        locationmode='USA-states',  # set of locations match entries in `locations`
#        colorscale='Reds',
#        colorbar_title="in USD",
#    ))
#
#    fig.update_layout(
#        title_text=title,
#        geo_scope='usa',  # limite map scope to USA
#    )
#    plot(fig)
#
#cloroplot(state_mean, 'loan_amnt', 'Mean loans by State')
#
#
#
