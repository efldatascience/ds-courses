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
df = pd.read_csv("vgsales.csv")

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
df.

# %%
# shape of the DataFrame
df.

# %%
# information of the DataFrame
df.



# %% excursus groupby statements
#group data by genre
dfGenre = 

#get keys of groups
dfGenre.

#return indexes of the observations for a specific group
dfGenre.

#return DataFrame of all observations within a specific key
dfGenreAction = 

#perform some aggregate functions on the groups
print() #sum
print() #min
print() #max


#descriptive statistics on the global sales for the year 2010
descriptives = 





# %% data analysis 2) some first statistics

# Question: How many unique Games, Publishers, Platforms, Genres, and Years are in the data set?

#overall statistics
games = 
publisher = 
platforms = 
genres = 
years = 

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
LdfReleases =  








# %% data analysis 4) Publisher wise analysis

# Who are the most succesfull publishers?

#top 10 publishers by video game releases
LdfPubReleases =  
#print the top 10 publishers by releases
print()




# %%
#top 10 publishers by video game sales
LdfPubSales = 

#print the top 10 publishers by sales
print()




# %%
#top 10 publishers by video game sales in europe and North America
LdfPubSalesEu =

LdfPubSalesNa =

#print the top 10 publishers by sales
print()




# %%
#top 10 publishers by video game sales between 2010 and 2015
LdfPubSalesYears =

#print the top 10 publishers by sales
print()










# %% data analysis 5) Platform wise analysis

# Question: Which platforms are the most (least) successful by sales

LdfPlatSales =

print('The most successful platform is ')
print('The least successful platform is ')



# %% data analysis 6) Genre wise analysis

# Question: What is the most popular Genre by game releases of the ten most succesful platforms?

#get the 10 most successful platforms
Platforms =

#save results in dictionary
results = dict()

#get most popular Gerne for each platform
for platform in Platforms:
    LdfGenre =

#print results
print(results)





