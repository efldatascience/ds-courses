# Examples discussed in the lecture on "Helpful functions for data preprocessing: Libraries os, re, csv"

# ---- (1) Basics about libraries in Python ----
# All examples do the same thing
import numpy as np

result = np.std([2, 7, 13, 99])
print(result)

from numpy import std

result = std([2, 7, 13, 99])
print(result)

from numpy import std as bestimme_die_std

result = bestimme_die_std([2, 7, 13, 99])
print(result)

# ---- (2) Library os ----
import os

# current working directory you operate in
print(os.getcwd())
path = "/home/tino/data"  # or r“C:\Users\tino\data” under Windows
os.chdir(path)  # change current working dir
print(os.getcwd())

for i in range(10):
    os.mkdir("folder_" + str(i))  # create new folder in current working dir
for i in range(10):
    os.removedirs("folder_" + str(i))  # create new folder in current working dir

# Iterate through directory
path_content = os.listdir(path)  # list of all dirs and files in path
print(path_content)
for f in path_content:  # iterate trough all files and folders in path
    joined = os.path.join(path, f)  # join various path components
    print(joined)  # print all file and folder names in path

# Walk through directory and subdirectories and print files only
path_content = os.walk(path)
for root, dirs, files in path_content:  # walk the tree
    for name in files:
        joined = os.path.join(root, name)  # join various path components
        print(joined)  # print all filenames in path+depper

# ---- (3) Library csv ----
import csv

# create some test data
s_test_string = "this is a test"
data = [(i, j) for i, j in enumerate(s_test_string.split())]
print(data)

# write to file
with open("test.csv", "w", newline="") as testFile:
    writer = csv.writer(testFile, delimiter=",")
    for row in data:
        writer.writerow(row)

# read from file
with open("test.csv", "r") as testFile:
    reader = csv.reader(testFile, delimiter=",")
    output = []
    for row in reader:
        output.append(tuple(row))
print(output)


# ---- (4) numpy (np) ----
import numpy as np

# Create vector
lst = [1, 2, 3]
myvector = np.array(lst)  # alternatively: np.array([1,2,3])
print(myvector.shape)

# Create matrix
mymatrix = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
print(mymatrix.shape)

# Indexing
print(mymatrix[0])  # print first row
print(mymatrix[:, 1])  # print second column
print(mymatrix[2, 1])  # value in last row and second column

# Calculate means
result0 = np.mean(mymatrix, axis=0)
result1 = np.mean(mymatrix, axis=1)
print(result0)
print(result1)

# ---- (5) Library re ----
import re

##find all single integers in a string
re.findall(pattern="[0-9]", string="1 plus 1 yields 2")
##compare these two
re.findall(pattern="[0-9]", string="4 plus 8 yields 12")
re.findall(pattern="[0-9]+", string="4 plus 8 yields 12")

##find all URLs in a string
re.findall("(www[^ ]+)", "my webpage is: www.example.com")
##find all dates in a string
re.findall("([0-9]{4,4})-([A-Za-z]+)-([0-9]{2,2})", "2018-Oct-22-HAL.N-140579834485-Transcript")

# ---- EXERCISE ----

# download the provided zip-file numpy_data.zip and extract it to create a directory that e.g. looks like this
# /mypath/to/folder/numpy_data and contains customer1.csv, customer2.csv, customer3.csv

import numpy as np
import csv
import os

path = "/home/tino/data/numpy_data"
