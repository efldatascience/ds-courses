# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:16:21 2020

@author: Jens Lausen
"""

# %% making the data ready for analysis


# Import libraries
import pandas as pd
import numpy as np

#read data to dataframe
df = pd.read_csv("../vgsales.csv")

#perform cleaning from the pandas lecture
#get information on dataframe
print(df.info())

#check missing values
df_null_values = df.isnull().sum()
print(df_null_values)

#drop missing values
df = df.dropna(axis=0)
df.info()

#convert year to int
df['Year'] = df['Year'].astype('int64') 


#reset the index
df = df.reset_index(drop=True)


# %% data analysis 1) information about the data set

# how does the data look like (show first rows)
df.head()

# %%
# shape of the DataFrame
df.shape

# %%
# information of the DataFrame
df.info()



# %% excursus groupby statements
#group data by genre
dfGenre = df.groupby('Genre')

#get keys of groups
dfGenre.groups.keys()

#return indexes of the observations for a specific group
dfGenre.groups['Action']

#return DataFrame of all observations within a specific key
dfGenreAction = dfGenre.get_group('Action')

#perform some aggregate functions on the groups
print(dfGenre['Global_Sales'].sum())
print(dfGenre['Global_Sales'].min())
print(dfGenre['Global_Sales'].max())


#descriptive statistics on the global sales for the year 2010
descriptives = df[df['Year']==2010].groupby('Genre')['Global_Sales'].describe()





# %% data analysis 2) some first statistics

# Question: How many unique Games, Publishers, Platforms, Genres, and Years are in the data set?

#overall statistics
games = df['Name'].unique()
publisher = df['Publisher'].unique()
platforms = df['Platform'].unique()
genres = df['Genre'].unique()
years = df['Year'].unique()

print('Games '+str(len(games)),
      'Publishers '+str(len(publisher)),
      'Platforms '+str(len(platforms)),
      'Genres '+str(len(genres)),
      'Years '+str(len(years)),
      sep = '\n')







# %% data analysis 3) Year wise analysis

# Question: How have Video Game Sales and Releases developed over time?

# Global sales grouped by year (See lecture visualization)
import matplotlib.pyplot as plt
import seaborn as sns

df_groupData = df.groupby(['Year']).sum()
LdfGroupSales = df_groupData['Global_Sales']
LIndexesOfGroupData = df_groupData.index.astype(int)

# Generate the bar plot
plt.figure()
sns.barplot(y=LdfGroupSales, x=LIndexesOfGroupData, color='darkblue')
plt.title('Global Sales Grouped by Year')
plt.xticks(rotation=45, fontsize=6)
plt.ylabel('Global Sales')
plt.xlabel('Years')
plt.savefig('BarChart_GlobalSales.pdf')
plt.show()

# %%
# video game releases by year
LdfReleases =  df.groupby('Year')['Name'].count()
LdfReleases.name = 'Releases'
LIndexesOfReleases = LdfReleases.index.astype(int)

plt.figure()
sns.barplot(y=LdfReleases, x=LIndexesOfReleases, color='darkblue')
plt.title('Video Game Releases by Year')
plt.xticks(rotation=45, fontsize=6)
plt.ylabel('Video Game Releases')
plt.xlabel('Years')
plt.savefig('BarChart_Releases.pdf')
plt.show()



# %% data analysis 4) Publisher wise analysis

# Who are the most succesfull publishers?

#top 10 publishers by video game releases
LdfPubReleases =  df.groupby('Publisher')['Name'].count().reset_index()
LdfPubReleases.columns = ['Publisher', 'Releases']
LdfPubReleases = LdfPubReleases.sort_values('Releases',ascending=False).reset_index(drop = True) # drop drops the old index, otherwise it is saved as a new column

#print the top 10 publishers by releases
print(LdfPubReleases.head(10))


# %%
#top 10 publishers by video game sales
LdfPubSales =  df.groupby('Publisher')['Global_Sales'].sum().reset_index()
LdfPubSales = LdfPubSales.sort_values('Global_Sales',ascending=False).reset_index(drop = True)

#print the top 10 publishers by sales
print(LdfPubSales.head(10))


# %%
#top 10 publishers by video game sales in europe and North America
LdfPubSalesEu =  df.groupby('Publisher')['EU_Sales'].sum().reset_index()
LdfPubSalesEu = LdfPubSalesEu.sort_values('EU_Sales',ascending=False).reset_index(drop = True)

LdfPubSalesNa =  df.groupby('Publisher')['NA_Sales'].sum().reset_index()
LdfPubSalesNa = LdfPubSalesNa.sort_values('NA_Sales',ascending=False).reset_index(drop = True)

#print the top 10 publishers by sales
print('EU_Sales:',
      LdfPubSalesEu.head(10),
      'NA_Sales:',
      LdfPubSalesNa.head(10),
      sep = '\n')

# %%
#top 10 publishers by video game sales between 2010 and 2015
LdfPubSalesYears = df[(df['Year']>= 2010) & (df['Year']<=2015)].groupby('Publisher')['Global_Sales'].sum().reset_index()
LdfPubSalesYears = LdfPubSalesYears.sort_values('Global_Sales',ascending=False).reset_index(drop = True)

#print the top 10 publishers by sales
print(LdfPubSalesYears.head(10))


# %% data analysis 5) Platform wise analysis

# Question: Which platforms are the most (least) successful by sales

LdfPlatSales = df.groupby('Platform')['Global_Sales'].sum().reset_index()
LdfPlatSales = LdfPlatSales.sort_values('Global_Sales',ascending=False).reset_index(drop = True)

plt.figure()
sns.barplot(y=LdfPlatSales['Global_Sales'], x=LdfPlatSales['Platform'], color='darkblue')
plt.title('Video Game Sales by Platform')
plt.xticks(rotation=45, fontsize=6)
plt.ylabel('Video Game Sales')
plt.xlabel('Platforms')
plt.savefig('BarChart_Platforms.pdf')
plt.show()

print('The most successful platform is ' + LdfPlatSales.iloc[0]['Platform'])
print('The least successful platform is ' + LdfPlatSales.iloc[len(LdfPlatSales)-1]['Platform'])



# %% data analysis 6) Genre wise analysis

# Question: What is the most popular Genre by game releases of the ten most succesful platforms?

#get the 10 most successful platforms
Platforms = LdfPlatSales.iloc[0:10]['Platform']

#save results in dictionary
results = dict()

#get most popular Gerne for each platform
for platform in Platforms:
    LdfGenre = df[df['Platform'] == platform].groupby('Genre')['Name'].count().reset_index()
    LdfGenre = LdfGenre.sort_values('Name',ascending=False).reset_index(drop = True)
    results[platform] = LdfGenre.iloc[0]['Genre']

#print results
print(results)





