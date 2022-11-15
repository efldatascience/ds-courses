# Examples discussed in the lecture on "Helpful functions for data preprocessing: Libraries os, re, csv"

# ---- (1) Basics about libraries in Python ----
# All examples do the same thing!
lst = [2, 7, 13, 99]

#%%
# Import library with plain import statement
import numpy 
result1 = numpy.std(lst)
print(result1)

#%%
# Import library using alias
import numpy as np

result2 = np.std(lst)
print(result2)

#%%
# Import submodule from library 
from numpy import std

result3 = std(lst)
print(result3)

#%%
# Import submodule from library using alias
from numpy import std as bestimme_die_std

result4 = bestimme_die_std(lst)
print(result4)

#%%
# Generate module with x1=1, x3=3 and a function fct1 that sums up two elements
from libraries_user_module import fct1

y1 = fct1(5,6)
print(y1)

from libraries_user_module import x1, x3
y2 = fct1(x1, x3) 
print(y2)

# Alternative: 
import libraries_user_module
y3 = libraries_user_module.fct1(libraries_user_module.x1,
                                libraries_user_module.x3
                                )
print(y3)


#%%
# ---- (2) Library os ----
import os

#%%
# 2.1 Basic commands 

#%%
# Show current working directory you operate in
print(os.getcwd())

#%%
# Change current working directory
path = r"C:\Users\cesto\Documents\GitHub\efl-DS-Kurs-TC"  # or r“C:\Users\tino\data” under Windows
os.chdir(path)  # change current working dir
print(os.getcwd())

#%%
# List all files in current working directory
print(os.listdir())

#%%
# create a folder in current working directory
os.mkdir('Folder1')

#%%
# delete a folder in current working directory
os.removedirs('Folder1')

#%%
# create a folder at your desktop
folderpath = r'C:\Users\cesto\Desktop\FolderNew'
os.mkdir(folderpath)

#%%
# delte folder at your desktop
os.removedirs(folderpath)

#%%
# 2.2 Some Applications

#%%
# Automatically generate folders
for i in range(10):
    os.mkdir("folder_" + str(i))  # create new folder in current working dir
#%%
# Automatically delete folders
for i in range(10):
    os.removedirs("folder_" + str(i))  # create new folder in current working dir

#%%
# Iterate through directory
path_content = os.listdir(path)  # list of all dirs and files in path
print(path_content)
for f in path_content:  # iterate trough all files and folders in path
    joined = os.path.join(path, f)  # join various path components
    print(joined)  # print all file and folder names in path

#%%
# Outlook:
# Walk through directory and subdirectories and print files only
path_content = os.walk(path)
for root, dirs, files in path_content:  # walk the tree
    for name in files:
        joined = os.path.join(root, name)  # join various path components
        print(joined)  # print all filenames in path+depper


#%%
# ---- (3) numpy (np) ----
import numpy as np

#%%
# Create vector
lst = [1, 2, 3]
vec1 = np.array(lst)
vec2 = np.array([4,5,6])

#%% 
# Print shape
print(vec1.shape, vec2.shape)

#%%
# Vector indexing
print(vec1[1])  # second element
print(vec1[-1])  # first element when counting from the end

#%%
# Addition of both vectors
vec3 = vec1 + vec2 
print(vec3)

#%%
# Create matrix
mtrx1 = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
mtrx2 = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])
#%% 
# Print shape
print(mtrx1.shape, mtrx2.shape)

#%%
# Matrix indexing
print(mtrx1[0])  # print first row
print(mtrx1[:, 1])  # print second column
print(mtrx1[2, 1])  # value in last row and second column

#%%
# Addition of both matricies
mtrx3 = mtrx1 + mtrx2 
print(mtrx3)

#%%
# Element-wise multiplication of both matricies
mtrx4 = mtrx1 * mtrx2 
print(mtrx4)

#%%
# Matrix multiplication of both matricies
mtrx5 = np.dot(mtrx1, mtrx2)
print(mtrx5)

#%%
# Calculate means
result0 = np.mean(mtrx1)
result1 = np.mean(mtrx1, axis=0)
result2 = np.mean(mtrx1, axis=1)
print(result0)
print(result1)
print(result2)


#%%
# ---- EXERCISE ----

#%%
# download the provided zip-file numpy_data.zip and extract it to create a directory that e.g. looks like this
# /mypath/to/folder/numpy_data and contains customer1.csv, customer2.csv, customer3.csv

import numpy as np
import os

path = r'C:\Users\cesto\Documents\GitHub\efl-DS-Kurs-TC\numpy_data'
files = os.listdir(path)
print(files)
overall_consumption = np.zeros(shape=(5, 3))  # store data of each customer

#%%
for file in files:
    filepath = os.path.join(path, file)
    customer_data = np.genfromtxt(filepath, delimiter=',')  # read data
    customer_data = customer_data[1:, 1:]  # filter for integer values

    # Print average consumption for customer i across the 5 days
    print(f"Mean consumption of {file.split('.')[0]}")
    print("Apples, Bananas, Citrons")
    print(customer_data.mean(axis=0))
    
    # Print standard deviation
    print(f"Standard deviation of {file.split('.')[0]}")
    print("Apples, Bananas, Citrons")
    print(customer_data.std(axis=0))
    
    
    # Add customer consumption to overall consumption
    overall_consumption = overall_consumption + customer_data
    
#%%
print(f"Mean consumption across all customers")
print("Apples, Bananas, Citrons")
print(overall_consumption.mean(axis=0))

print(f"Standard deviation across all customers")
print("Apples, Bananas, Citrons")
print(overall_consumption.std(axis=0))


