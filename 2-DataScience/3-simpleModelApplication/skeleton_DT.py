# code skeleton for Task 1

# import packages
from sklearn.tree import DecisionTreeRegressor, plot_tree, export_text
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd


# load data set
data = pd.read_csv('dataset_small.csv')

# fill missing values
data["dti"]=data["dti"].fillna(data["dti"].mean())

#%%

#alternative: drop missing values
data = 

#%%

# select X and y from data set
y =
X = 

#%%

# get random train and test data from data set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

#%%

# Configure model
regr = 

#%%

# Fit regression model

#%%

# Predict
y_1 =

#%%

# evaluation
mse1 = 
r2_1 = 

print('DT: mse = '+str(mse1) + ' r2 = '+str(r2_1))

#%%
# plot tree
import matplotlib.pyplot as plt



#%%

# export tree to text
sTree = export_text(regr, feature_names = list(X_train.columns))






