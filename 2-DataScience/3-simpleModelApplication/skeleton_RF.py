# code skeleton for Task 2

# import packages
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd

# load data set
data = pd.read_csv('dataset_small.csv')

# fill missing values
data["dti"]=data["dti"].fillna(data["dti"].mean())

# select X and y from data set
y = ...
X = ...

# get random train and test data from data set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Configure model
...

# Fit regression model
...

# Predict
...

# evaluation
...

# plot tree
...

# export tree to text
...
