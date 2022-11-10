# Appendix 
# No worries: Not relevant for final exercise!

# ---- (4) Library csv ----
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
