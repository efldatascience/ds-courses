import pandas as pd
import keras
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# (1) ---- Import data ----
# Load data
data_raw = pd.read_csv('bank_marketing_balanced.csv')  # Source: https://archive.ics.uci.edu/ml/datasets/bank+marketing#

# get first impression of the data
print(data_raw.head(5))
print(data_raw.shape)  # number of observations and features (-1)
print(data_raw.apply(lambda col: col.unique()))  # Show unique values per column

# (2) ---- Data pre-processing ----
data_pp = data_raw.copy()
# Transform categorical to numeric features
categoricals = ['job', 'marital', 'education', 'default', 'housing', 'loan',
                'contact', 'month', 'day_of_week', 'poutcome', 'y']
df_dummies = pd.get_dummies(data_pp.loc[:, categoricals], drop_first=True)
data_pp = pd.concat([data_pp.drop(categoricals, axis=1), df_dummies], axis=1)
data_pp.rename(columns={'y_yes': 'y'}, inplace=True)
print(data_raw.tail(5))
print(data_pp.tail(5))

# What about class imbalance?
print(data_pp['y'].value_counts())  # show absolute number of observations per value of y
print(sum(data_pp['y'] == 1) / data_pp.shape[0])  # share of observations where y=1

# Split in train and test
X_train, X_test, y_train, y_test = train_test_split(data_pp.drop('y', axis=1), data_pp.loc[:, 'y'], test_size=0.15)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

# Split in train and valid
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.15)
print(X_train.shape, y_train.shape)
print(X_val.shape, y_val.shape)
# Hint: to get precise split of 70-15-15 (train-test-valid), do test_size=0.15 and then test_size=0.15/0.85

# Neural network performs pretty well on features ranging between 0 and 1 --> Rescale features with minmax scaling
minmax = MinMaxScaler()
print(X_train)  # before scaling
X_train.loc[:, :] = minmax.fit_transform(X_train)
print(X_train)  # after scaling
# Transform validation and test data with min & max parameter of training data
X_val.loc[:, :] = minmax.transform(X_val)
X_test.loc[:, :] = minmax.transform(X_test)


# (3) ---- Build, train and evaluate ANN ----
# Construct the model (define layers, their units and activation functions)
no_inputs = X_train.shape[1]

mynn = keras.Sequential([
    keras.layers.Dense(units=5, activation='relu', input_dim=no_inputs), # Hidden layer with 5 units and activation function relu
    keras.layers.Dense(units=1, activation='sigmoid')  # output layer with one unit
])

# Define how the model is trained (defines the process of backward propagation)
mynn.compile(optimizer='Adam', loss='binary_crossentropy', metrics=['binary_accuracy'])

print(mynn.summary())

# Train the model to optimize all weights
mynn.fit(x=X_train, y=y_train, batch_size=32, epochs=5, validation_data=(X_val, y_val), shuffle=True)

# Evaluate the performance of the model on (unseen) test data
mynn.evaluate(x=X_test, y=y_test)

# TODO: HYPERPARAMETER OPTIMIZATION
# TODO: (1) Experiment with different network architectures (e.g. adjust number of units)
# TODO: (2) Experiment with different mini_batch_sizes (=batch_size parameter in keras)
# TODO: (3) Don't forget to store the results of the individual runs!

del mynn