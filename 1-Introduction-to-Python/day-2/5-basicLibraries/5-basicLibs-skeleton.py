##import libraries
import os

##current working directory you operate in
print(os.getcwd())

for i in range(10):
    ##create new folder
    os.mkdir("folder_"+str(i))
    
for i in range(10):
    ##change current directory, starting point is os.getcwd()
    os.chdir("folder_"+str(i))
    ##open a file here: will follow later
    ##go one step back in folder hierarchy
    os.chdir("..")
    
##further examples:
os.listdir(os.getcwd())

##move a file
os.system("mv inputData.txt folder_0")
os.rename("inputData.txt", "folder_0/inputData.txt")
##and back
os.rename("folder_0/inputData.txt", "inputData.txt")

##remove folders again
for i in range(10):
    os.removedirs("folder_"+i)


######################
##csv
import csv
##create some test data
sTestString = "this is a test"
data = [(i,j) for i,j in enumerate(sTestString.split())]
##write to file
with open("test.csv", "w", newline="") as testFile:
    writer = csv.writer(testFile, delimiter=",")
    ##write row by row to file
    for row in data:
        writer.writerow(list(row))
##close connection to file        
testFile.close()

##read from file
with open("test.csv", "r") as testFile:
    reader = csv.reader(testFile, delimiter=",")
    output = []
    for row in reader:
        output.append(tuple(row))
    
   
######################    
##re
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


######################
##exercises
##1. Create folders test1,…,test100 using os
##and create files named test1.txt,...,test100.txt in the respective folder
for i in range(100):
    ...

##2. open file inputData.txt 
with open("inputData.txt", "r") as txtfile:
    ...

##and write each i-th row of it to test`i'.txt
for i in range(100):
    num = str(i+1)    
    with open(...):
        ...


##3. dict string month to integer
monthDict = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
##iterate through files, extract dates, convert it and store it in output
output = dict()
for i in range(100):
    num = str(i+1)  
    ...

##4. delete all files using os
for i in range(100):
    num = str(i+1)
    ##remove files
    ...
    ##then directory
    ...