# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:30:32 2019

@author: NP & BAK
"""
#Importing required packages.
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, export_text, plot_tree
from sklearn.metrics import mean_squared_error, r2_score, classification_report,accuracy_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

###########################
##### Data Import ######
############################
# Import the data
wine = pd.read_csv('winequality-red.csv')


###########################
##### Pre-Processing ######
###########################
#Let's check how the data is distributed
#Information about the data columns



#############################
#####Data Visualization######
#############################
# Use @code: for describing stats.

# Pairplot for an overview.


# Create a box plot consisting of quality and alcohol acid
# without outliers. 
# Add title, names to the axes and save the plot as pdf.
plt.figure()
sns.boxplot(x='quality', y='alcohol', data = wine)
plt.ylabel('Alcohol')
plt.xlabel('Quality')
plt.title('Boxplot Auality Alcohol')
plt.savefig('figures/BoxPlotForWine.png')
plt.show()

# Create a Distplot for the fixed acidity in the data set. 
# What does the data distribution tell us? 
plt.figure()
sns.distplot(wine['fixed acidity'])
plt.xlabel('Fixed Acidity')
plt.ylabel('Count')
plt.savefig('figures/Distplot.png')
plt.show()


# Create a heatmap with the correlation. Calculate the correlation with 
# numpy and use the mask option in the heatmap. Add also axis names and titles.
# For what is this plot useful? What insight?  
corr = wine.corr()
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
plt.figure(figsize=(9, 6))
sns.heatmap(corr, mask=mask, annot=True,cbar=True, linewidths=.5, cmap="YlGnBu")
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('CorrelationHeatmap.pdf')
plt.show()


##########################################
#####Data Modeling: Data Preparation######
##########################################

# Now it is time to prepare our data for data-modeling
# We want to accomplish two tasks with our machine learning models: 
# 1. A prediction for how much alcohol will be in a wine of certain attributes.
# 2. We want to classify if a wine is good or bad for a given set of wine attributes.

# Let's have a look at the values for the first prediction:
alcohol = set(wine.alcohol.tolist())
print(alcohol)
# This data looks perfect for our regression task.

# Now for the second task: Let's see what values the quality column has.
quality = set(wine.quality.tolist())
print(quality)

#It appears that we only have values between 3 and 8, while 8 being the criterion
# for really good wine, and 3 being a really bad wine.

# Since we only want to distinguish between good and bad wines, we need to make
# bins of values to assign these values to either good or bad category.

# We make a binary classificaion for the quality variable.
# Doing this, we divide the set of quality measures as good as possible
# We do this with the important cut function.
# apply the cut function to the respective subset of wine to fill the
# wine['quality'] column with the new values.

bins = (2, 6.5, 8)
group_names = ['bad', 'good']
wine['quality'] = pd.cut(...)

# Now take a look at the dataframe column quality. Looks better!

# Our models only need 0 and 1 to classify whether the wine is good 
# or not. Thus, we must assign 0 for bad and 1 for good quality.
# We do this with the LabelEncoder.

#Now lets assign a labels to our quality variable
label_quality = LabelEncoder()

#Bad becomes 0 and good becomes 1 
wine['quality'] = label_quality.fit_transform(wine['quality'])

# Count the values of the quality column of wine.
wine['quality'].value_counts()

# Make a seaborn countplot for the values of the quality column of wine.
....

#############################################
####Preparing the data for the first task####
#############################################

# Now seperate the dataset as response variable/ target variable.
# We do this by using the drop function for subset of independent variables
# and only adding the alcohol column to subset for the dependent/target variable.
X = wine.drop('alcohol', axis = 1)
y = wine['alcohol']

#Train and Test splitting of data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# Explain the Train-Test split. Why did we split by the test_size?
# Please explain why we need a train and a test set.

# Applying Standard scaling:
# Standardization of a dataset is a common requirement for many 
# machine learning estimators: they might behave badly if the 
# individual features do not more or less look like standard 
# normally distributed data (e.g. Gaussian with 0 mean and unit variance).
# see: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)


# Now you have all the data you need to train the model.
X_train # training sample (independent variables)
y_train # training sample (dependent variable)
X_test # testing sample (independent variables)
y_test # testing sample (dependent variable)




##########################################
#####Data Modeling: Model Creation #######
##########################################

###########################
######Regression Tree######
###########################

# Please configure the regression tree as learned in the lecture.
# You should also describe, why you set certain parameters such as
# max_depth and what the effect of these parameters was.

# Configure model
regr = ...

# Fit regression model
regr.fit(..., ...)

# Predict
y_pred = ...

# evaluation
mse = mean_squared_error(..., ...)
r2 = r2_score(..., ...)
print('DT: mse = '+ str(mse) + ' r2 = '+ str(r2))
# plotting a tree with text

sTree = ...

# plot tree and save it to pdf
plt.figure()
plot_tree(..., filled = True, feature_names=list(X.columns),fontsize = 9)
plt.savefig('tree.pdf')

# What was the result of your Regression Tree?
# Can it efficiently predict the alcohol of the wines?
# If not, what could be the problem?


#######################
#####RandomForest######
#######################

##############################################
####Preparing the data for the second task####
##############################################

## Now to our most interesting prediction part: we want to know if we can
## classify good and bad wine. Thus, our target variable is the quality.

# We seperate the dataset as response variable/ target variable.
# We do this by using the drop function for subset of independent variables
# and only adding the quality column to subset for the dependent/target variable.
X = wine.drop('quality', axis = 1)
y = wine['quality']

# Now, we have the target label/dependent variable to train the classificator.
# Some machine learning models need a one-hot-encoded version for classification,
# no matter if binary, or multi-class classification.
# see: https://medium.com/@michaeldelsole/what-is-one-hot-encoding-and-how-to-do-it-f0ae272f1179

## we do this by the pd.get_dummies method: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html
y = pd.get_dummies(y)
#Train and Test splitting of data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# Explain the Train-Test split. Why did we split by the test_size?
# Please explain why we need a train and a test set.

# Applying Standard scaling:
# Standardization of a dataset is a common requirement for many 
# machine learning estimators: they might behave badly if the 
# individual features do not more or less look like standard 
# normally distributed data (e.g. Gaussian with 0 mean and unit variance).
# see: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)


# Now we are able to make our classifier.

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train, y_train)
pred_rfc = rfc.predict(X_test)

print ("Train Accuracy :: ", accuracy_score(y_train, rfc.predict(X_train)))
print ("Test Accuracy  :: ", accuracy_score(y_test, pred_rfc))
print(classification_report(y_test, pred_rfc, target_names=['bad','good']))
print(rfc.score(X_test,y_test))

# What was the result of your Random Forest Classifier?
# Could it efficiently predict the quality of the wines?
# If not, what could be the problem? If it was better than the Regression Tree,
# explain why this is the case?

#######################
#####Neural Nets ######
#######################

# This neural net structure is given. 
# Please fill out the missing Parameters in the model.
# Please explain the reason and the effect of the parameters.

from keras.models import Sequential, Model
from keras.layers import Dense, Input
from keras.utils import plot_model


model = Sequential()
##add dense layer, that is a fully connected layer
nFeatures = X.shape[1]
model.add(Dense(..., 
        input_dim=nFeatures, 
        activation="", 
        kernel_initializer="", 
        bias_initializer="zeros"))
##add output layer
nOutput = y.shape[1]
model.add(Dense(nOutput,
        activation="",
        kernel_initializer="", 
        bias_initializer="zeros"))
##set model compiler, https://keras.io/models/sequential/
model.compile(optimizer="", 
        loss="",
        metrics=[""])
##inspect neural network model
model.summary()


# Please fill out the missing training parameters. 
# What number did you set for Batch size? Why? What was the effect when you
# changed it?

# What does the number of Epochs do? Why would somebody use higher values of
# this parameterS?


##Training parameters
iBatchSize = ...
iNumEpochs = ...
##fit model
model.fit(x=X_train,
        y=y_train,
        batch_size=iBatchSize,
        epochs=iNumEpochs,
        validation_split=...,
        verbose=2,
        shuffle=True)


##evaluate model fit using unseen test data
model.evaluate(x=X_test, y=y_test, batch_size=iBatchSize)

# What was the result of your model?
# Please describe the discrepancy of your test, validation and prediction accuracy.