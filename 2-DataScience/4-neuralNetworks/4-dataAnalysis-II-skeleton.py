from keras.models import Sequential, Model
from keras.layers import Dense, Input
from keras.utils import plot_model
from sklearn.model_selection import train_test_split
import pandas as pd
import re
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


##import data 
data = pd.read_csv("../../1 - introduction Python/0 - data sets/dataset_small.csv")
##create list features used for classification
featuresNum = ["emp_length", "annual_inc", "dti"]
featuresCat = ["home_ownership"]
##for the sake of simplicity:
##delete all observations with NAs
print(data.shape)
data = data[featuresNum+featuresCat+["grade"]].dropna()
print(data.shape)
##employment length (<1 -> 1, 10+ -> 10)
##alternatively: make it catgorical
data["emp_length"].head()
data["emp_length"] = [int(re.findall("[0-9]+",i)[0]) if pd.notna(i) else i for i in data["emp_length"]]
##create X matrix
X = data[featuresNum+featuresCat]
print(X.shape)
##there are some dummy variables: make same categorical_accuracy
X = pd.get_dummies(X, columns=featuresCat)
print(X.shape)
##create y vector
y = data["grade"]
##and as well to categorical
y = pd.get_dummies(y)
##create train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)


##create sequential model, see https://keras.io/models/sequential/
##i.e., linear stack of layers
model = Sequential()
##add dense layer, that is a fully connected layer
nFeatures = X.shape[1]
model.add(Dense(20, 
        input_dim=nFeatures, 
        activation="relu", 
        kernel_initializer="random_normal", 
        bias_initializer="zeros"))
##add output layer
nOutput = y.shape[1]
model.add(Dense(nOutput,
        activation="softmax",
        kernel_initializer="random_normal", 
        bias_initializer="zeros"))
##set model compiler, https://keras.io/models/sequential/
model.compile(optimizer="adam", 
        loss="categorical_crossentropy",
        metrics=["categorical_accuracy"])
##inspect neural network model
model.summary()


##Training parameters
iBatchSize = 50
iNumEpochs = 5
##fit model
model.fit(x=X,
        y=y,
        batch_size=iBatchSize,
        epochs=iNumEpochs,
        validation_split=0.1,
        verbose=2,
        shuffle=True)

##evaluate model fit using unseen test data
model.evaluate(x=X_test, y=y_test, batch_size=iBatchSize)     


##TASKS: hyperparameter optimization
##run the code for different sizes of the network (layers and nodes)
##using a loop
##store the respective validation loss
output = dict()
for l in range(1,11):
    ...

##plot the loss wrt the network size
