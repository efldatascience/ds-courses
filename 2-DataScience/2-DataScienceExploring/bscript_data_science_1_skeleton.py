# Script
# First Data Science Script
# @author: Dr. Benjamin M. Abdel-Karim
# @since: 2022-12-05
# @version: 1.0

# Import libraries for our data analysis.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import datetime
# --------------
# Setup
# --------------
# Create output folder
now = datetime.datetime.now()
date_time = now.strftime('%Y-%m-%d_%H-%M-%S')
string_log_folder = 'logs/' + 'log' + '_' + date_time
if not os.path.exists(string_log_folder):
    os.makedirs(string_log_folder)
print('// complete ....... execute folder creation: ', string_log_folder)

# %%
# --------------
# Import the data set
# --------------
# Import our data set.
# Check your working directory first.
# Is your file in the directory? What is its name?
# Now create a pandas dataframe.
print(os.getcwd())
print(os.listdir())
df = pd.read_csv('../data/dataset_small.csv', sep=',')

# %%
# --------------
# data important
# --------------
# Import our data set.
# Check your working directory first.
# Is your file in the directory? What is its name?
# Now create a pandas dataframe.
# df = pd.read_csv('dataset_small.csv', sep=',')

os.getcwd()
os.listdir()
df = pd.read_csv('../data/dataset_small.csv', sep=',')

# %%
# Let's have a first look at our dataset!
# Let's see what attributes/columns we have.
print(df.info())
print('// complete ....... data import')

# %%
# --------------
# Pre-Processing
# --------------
# Data preprocessing is an important step in the data mining process.
# The phrase "garbage in, garbage out" is particularly applicable
# to data mining and machine learning projects.
# So that is the number of columns. Great! Still too little information, actually.
# I wonder what data types those specific columns are.
# Now we're talking. We do have a lot of float values.
print(df.info())

# Sum all NaN Values
df_null_values = df.isnull().sum()
print(df_null_values)

# %%
# Create a plot to take another view.
# Warning: This plot requires relatively much computing time.
plt.figure(figsize=(15, 5))
sns.heatmap(df.isnull(), cbar=False, yticklabels=False, cmap='winter')
plt.xticks(rotation=45, fontsize=6)
plt.tight_layout()
plt.savefig(string_log_folder + '/' + 'MissingValues.png', dpi=300)
plt.close()
print('// complete ....... figure: heatmap Missing Values')

# %%
# Fill NA/NaN values using the specified method.
df = df.fillna(0)
print('// complete ....... data pre-processing')

# %%
# Drop all useless columns
# Some attributes are droppable because they do not provide any value.
# Let's drop these attributes. This will reduce computational complexity and
# improve clarity of our dataset.
df = df.drop(columns=['id', 'member_id', 'url', 'desc'])

# %%
# --------------
# Data Exploring
# --------------
# Get all columns with numeric values.
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
df_numbers = df.select_dtypes(include=numerics)
print(df_numbers.columns)

# Get all models
list_unique_grade = df['grade'].unique()
int_unique_count_grade = len(list_unique_grade)
print('// complete ........ data: unique grade: ', list_unique_grade)
print('// complete ........ data: number of grades: ', int_unique_count_grade)

# Super important: Slicing over column names with condition:
# Fore more details see Pandas DataFrame operations from day 2.
# With .iloc and loc als common approach
df_all_a_grades = df[df['grade'] == 'A']

# Select data where people have a high income.
df_high_income = df[df['annual_inc'] >= 75000]

# High income and high grade
df_high_income_and_grade = df[(df['annual_inc'] >= 75000) & (df['grade'] == 'A')]

# Get the interest rats
dMean_int_rate = df['int_rate'].mean()
dMax_int_rate = df['int_rate'].max()
dMin_int_rate = df['int_rate'].min()
print('// complete ........ data int_rate min: ', dMean_int_rate)
print('// complete ........ data int_rate max: ', dMax_int_rate)
print('// complete ........ data int_rate min: ', dMin_int_rate)

# Plot pairwise relationships in a dataset.
# Warning: This plot requires relatively much computing time.
# Therefore, here only a small selection of data
# If True, don’t add axes to the upper (off-diagonal)
# triangle of the grid, making this a “corner” plot.
plt.figure()
sns.pairplot(df[['loan_amnt', 'int_rate', 'installment', 'annual_inc', 'dti']], corner=True)
plt.savefig(string_log_folder + '/' + 'pair_plot.png', dpi=300)
plt.close()

# %%
# --------------
# Count Plot
# --------------
# Question: What is the purpose distribution of loans?
# Why is this question relevant?
# Show the counts of observations in each category.
# We use bars to split our dataset by setting breakpoints.
# In Spyder the quality could be a problem. Therefore, we use dpi param.
# You can also save the image as pdf
plt.figure()
ax = sns.countplot(x='purpose', data=df)
plt.savefig(string_log_folder + '/' + 'Purpose.png')
plt.close()

# Upgrade: Without borderlines
fig, ax = plt.subplots()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax = sns.countplot(x='purpose', data=df, palette='Greys')
plt.xticks(rotation=45, fontsize=6)
plt.xlabel('Purpose')
plt.ylabel('Count')
plt.title('Purpose of Use')
plt.tight_layout()
plt.savefig(string_log_folder + '/' + 'PurposeImprove_300.png', dpi=300)
plt.close()

# %%
# --------------
# Boxplot
# --------------
# Question:
# What is the interest rate per class?
plt.figure()
sns.boxplot(x='grade', y='loan_amnt', data=df, showfliers=False, palette='Greys')
plt.xticks(rotation=45, fontsize=6)
plt.title('Loan Amount by Class')
plt.savefig(string_log_folder + '/' + 'GradesLoanAmountImprove.png')
plt.close()


# %%
# --------------
# plot.bar
# --------------
# Selected all loan status.
print(df['loan_status'].unique())

LBad_indicators = ['Charged Off',
                    'Default',
                    'Does not meet the credit policy. Status:Charged Off',
                    'In Grace Period',
                    'Default Receiver',
                    'Late (16-30 days)',
                    'Late (31-120 days)']

# Define a bad loan in our DataFrame.
# Add all bad loans in our DataFrame.
df['bad_loan'] = 0
df.loc[df.loan_status.isin(LBad_indicators), 'bad_loan'] = 1

# Using croup by
dict_risk = df.groupby(['grade'])['bad_loan'].mean().sort_values().to_dict()
print(dict_risk)

plt.figure()
df.groupby(['grade'])['bad_loan'].mean().sort_values().plot.bar()
plt.ylabel('Percentage of Bad Debt')
plt.savefig(string_log_folder + '/' + 'RiskProfile.png')
plt.close()


# %%
# --------------
# Boxplot
# --------------
# Question: Loan interest by class
# Why is this question relevant?

plt.figure()
sns.boxplot(x='grade', y='int_rate', data=df)
plt.savefig(string_log_folder + '/' + 'GradesIntRate.png')
# plt.show()
plt.close()

# # Final plot.
plt.figure()
sns.boxplot(x='grade', y='int_rate', data=df,
             showfliers=False, palette='Blues',
             order=['A', 'B', 'C', 'D', 'E', 'F', 'G'])
plt.xticks(rotation=45, fontsize=6)
plt.title('Interest Rat and Grade in Order')
plt.savefig(string_log_folder + '/' + 'GradesIntRateOrder.png')
# plt.show()
plt.close()
print('// complete ....... data exploring part I')


# %%
# --------------
# Heatmap
# --------------
# Create a Heatmap for corr()
#  # or df.loc[:, ['C', 'D', 'E']
# Rember data:
# loanAmnt = The listed amount of the loan applied for by the borrower.
# If at some point in time, the credit department
# reduces the loan amount, then it will be reflected in this value.

# installment = The monthly payment
# owned by the borrower if the loan originates.

# annualInc = The self-reported annual income provided
# by the borrower during registration.

# dti = A ratio calculated using the borrower’s total monthly
# debt payments on the total debt obligations,
# excluding mortgage and the requested LC loan,
# divided by the borrower’s self-reported monthly income.

df_ForCorr = df[['loan_amnt', 'int_rate', 'installment', 'annual_inc', 'dti']]
corr = df_ForCorr.corr()

# Create Corr figure with headmap.
plt.figure()
sns.heatmap(corr,
        xticklabels=corr.columns,
        yticklabels=corr.columns, annot=True)
plt.tight_layout()
plt.savefig(string_log_folder + '/' + 'CoreHeatmap.pdf')
# plt.show()
plt.close()


# %%
# Update the corr plot with mask.
# Generate a mask for the upper triangle.
# @source: https://seaborn.pydata.org/examples/many_pairwise_correlations.html
# @code: np.zeros_like() return an array of zeros with the same shape and type as a given array.
# @code: np.triu_indices_from() return the indices for the upper-triangle of arr.

plt.figure()
mask = np.zeros_like(corr, dtype=bool)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(corr,
        xticklabels=corr.columns,
        yticklabels=corr.columns, annot=True, mask=mask)
plt.tight_layout()
plt.savefig(string_log_folder + '/' + 'CoreHeatmapUpdate.pdf')
plt.close()
print('// complete ....... data exploring part II')


# %%
# --------------
# cloroplot
# --------------
# More plots here
# We define a function for plotting the data on a cloropleth plot. A cloropleth
# plot allows us to plot data on an (interactive) map. Why should we use a function?
# Because we will use it multiple times, so we make our code cleaner.
# Type in your terminal: pip3 install plotly

state_mean = pd.DataFrame(df.groupby('addr_state')['loan_amnt'].mean())
from plotly.offline import plot
import plotly.graph_objects as go

def cloroplot(data, z, title):
    fig = go.Figure(data=go.Choropleth(
        locations=data.index,  # Spatial coordinates
        z=data[z].astype(float),  # Data to be color-coded
        locationmode='USA-states',  # set of locations match entries in `locations`
        colorscale='Reds',
        colorbar_title="in USD",
    ))

    fig.update_layout(
        title_text=title,
        geo_scope='usa',  # limite map scope to USA
    )
    plot(fig)
cloroplot(state_mean, 'loan_amnt', 'Mean loans by State')
print('// complete ....... data exploring part III')
