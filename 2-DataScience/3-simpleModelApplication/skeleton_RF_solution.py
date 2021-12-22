# Solution for Task 2

# import packages
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd

# load data set
data = pd.read_csv('dataset_small.csv')

# fill missing values
#data["dti"]=data["dti"].fillna(data["dti"].mean())

#alternative: drop missing values
data = data.dropna(subset = ['dti'])


# select X and y from data set
y = data['int_rate']
X = data[['dti','loan_amnt']]

# get random train and test data from data set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Configure model
regr = RandomForestRegressor(max_depth = 2, n_estimators=100, max_features='sqrt')#, random_state = 42)

# Fit regression model
regr.fit(X_train, y_train)

# Predict
y_1 = regr.predict(X_test)

# evaluation
mse1 = mean_squared_error(y_test, y_1)
r2_1 = r2_score(y_test, y_1)
print('RF: mse = '+ str(mse1) + ' r2 = '+ str(r2_1))

