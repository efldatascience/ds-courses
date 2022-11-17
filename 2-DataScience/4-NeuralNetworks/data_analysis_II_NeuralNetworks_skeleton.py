import pandas as pd
import keras
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
#%%
# (1) ---- Import data ----
# Load data
data_raw = pd.read_csv('bank_marketing_balanced.csv')  # Source: https://archive.ics.uci.edu/ml/datasets/bank+marketing#

#%% get first impression of the data
print(data_raw.head(5))

#%% get detailed impression of the data
for c in data_raw.columns:
    print(c)
    print(data_raw.loc[:, c].unique())  # Show unique values per column

#%%
# (2) ---- Data pre-processing ----
data_pp = data_raw.copy()  # make a copy
# Transform categorical to numeric features
categoricals = ['job', 'marital', 'education', 'default', 'housing', 'loan',
                'contact', 'month', 'day_of_week', 'poutcome', 'y']
df_dummies = pd.get_dummies(data_pp.loc[:, categoricals], drop_first=True)
print(df_dummies.info())

#%% Drop categorical columns
print(data_pp)
data_pp = data_pp.drop(categoricals, axis=1)

#%% Insert dummies representing the categoricals
data_pp = pd.concat([data_pp, df_dummies], axis=1)
print(data_pp)

#%% Rename y_yes back to y
data_pp.rename(columns={'y_yes': 'y'}, inplace=True)

#%% Show output
print(data_raw.tail(5))
print(data_pp.tail(5))

#%% What about class imbalance?
print(data_pp['y'].value_counts())  # show absolute number of observations per value of y
print(sum(data_pp['y'] == 1) / data_pp.shape[0])  # share of observations where y=1


#%% Split in x and y
x = data_pp.drop('y', axis=1)
y = data_pp.loc[:, 'y']

#%% Split in train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

#%% Split in train and valid
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.15)
print(x_train.shape, y_train.shape)
print(x_val.shape, y_val.shape)
# Hint: to get precise split of 70-15-15 (train-test-valid), do test_size=0.15 and then test_size=0.15/0.85

#%% Rescale features with minmax scaling
# Neural networks perform pretty well on features ranging between 0 and 1
minmax = MinMaxScaler()
print(x_train)  # before scaling
x_train = minmax.fit_transform(x_train)
print(x_train)  # after scaling

#%% Transform valid. & test data with min & max parameter of training data
x_val = minmax.transform(x_val)
x_test = minmax.transform(x_test)


#%%
# (3) ---- Build, train and evaluate ANN ----
# Construct the model (define layers, their units and activation functions)
no_inputs = x_train.shape[1]

#%%
mynn = keras.Sequential([
    keras.layers.Dense(units=5, activation='relu', input_dim=no_inputs), # Hidden layer with 5 units and activation function relu
    keras.layers.Dense(units=1, activation='sigmoid')  # output layer with one unit
])

#%%
# Define how the model is trained (defines the process of backward propagation)
mynn.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['binary_accuracy'])

print(mynn.summary())


#%% Train the model to optimize all weights
train_results = mynn.fit(x=x_train, y=y_train, batch_size=32, epochs=5, 
                         validation_data=(x_val, y_val), shuffle=True)
print(train_results.history)

#%%
# Evaluate the performance of the model on (unseen) test data
test_results = mynn.evaluate(x=x_test, y=y_test)
print(test_results)

#%% Delete model and experiment with different setups
del mynn

#%% TODO: HYPERPARAMETER OPTIMIZATION

#%% TODO 1: 
# Experiment with different network architectures (e.g. adjust number of units)

#%% TODO 2: 
# Experiment with different mini_batch_sizes (=batch_size parameter in keras)

#%% TODO 3:
# Try to achieve the highest accuracy at the test set in the class room!


# Don't forget to store the results of the individual runs!
