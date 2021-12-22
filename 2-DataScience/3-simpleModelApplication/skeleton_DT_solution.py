# Solution for Task 1

# import packages
from sklearn.tree import DecisionTreeRegressor, plot_tree, export_text
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
regr = DecisionTreeRegressor(max_depth = 2)

# Fit regression model
regr.fit(X_train, y_train)

# Predict
y_1 = regr.predict(X_test)

# evaluation
mse1 = mean_squared_error(y_test, y_1)
r2_1 = r2_score(y_test, y_1)
print('DT: mse = '+ str(mse1) + ' r2 = '+ str(r2_1))

# plot tree
import matplotlib.pyplot as plt
plt.figure()
plot_tree(regr, filled = False, feature_names=list(X.columns), fontsize = 7)
plt.savefig('dt1_result.pdf', transparent=True)

# export tree to text
sTree = export_text(regr, feature_names = list(X_train.columns))


