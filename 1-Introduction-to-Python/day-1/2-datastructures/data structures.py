# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:42:39 2019

@author: Nicolas Pfeuffer
"""

####Tuples####

Texample = 1, 2
print(Texample)

Texample2 = 1, 2, 3, 4, 5
print(Texample2)

Texample3 = 1, 2, 3.0, "hey", True
print(Texample3)






Texample[1]

Texample[0]

Texample2[4]

Texample2.index(4)

Texample4 = 1,4,3,4,4,5
Texample4.index(4)

Texample5 = 3.0,4.0,12.0
dVarA, dVarB, dVarC = Texample5

Texample6 = 4.0,8.0,16.0
Texample6[1] = 12.0

####Lists####

LNumbers = [1,2,3,4,5]
print(LNumbers)

LVarious = [1, 2, 3.0, "hey", True]
print(LVarious)

LEmpty = list()
print(LEmpty)

LVarious[1]

LVarious.index(2)


LVarious[1:3]

LVariousPart = LVarious[1:3]
print(LVariousPart)

LSpotify = ["Charts","Neuheiten","Podcasts & Video Shows", "Entdecken", "Konzerte"]

LSpotify[0] = "Aktuelle Charts"

LSpotify.append("Deine Songs")

LSpotify.pop()
print(LSpotify)

LSpotify.pop(3)
print(LSpotify)

LSpotify.remove("Neuheiten")
print(LSpotify)

LSpotify.insert(1,"Neuheiten")
LSpotify.insert(3,"Entdecken")
print(LSpotify)

len(LSpotify)

LSpotify.count("Neuheiten")

LSpotify.reverse()
print(LSpotify)
LSpotify.reverse()
print(LSpotify)

sTestString = "Lists are awesome and so are Strings!"
sTestString[3]
sTestString[0:5]
len(sTestString)

####Sets####


SNumbers = {1,2,3,4,5,1}
print(SNumbers)

SVarious = {1, 2, 3.0, "hey"}
print(SVarious)

SEmpty = set()
print(SEmpty)

4 in SVarious

2 in SVarious

LtoSet = [1,2,3,5,2,4,12,523,123,21]
SfromList = set(LtoSet)
print(SfromList)
# {1, 2, 3, 4, 5, 523, 12, 21, 123}

LfromSet = list(SfromList)
print(LfromSet)



# in SNumbers, but not in SVarious
SNumbers - SVarious

# in SNumbers or in SVarious or both
SNumbers | SVarious

# in SNumbers and in SVarious
SNumbers & SVarious

# in SNumbers or in SVarious but not in both
SNumbers ^ SVarious

####Dictionaries####

DNumbers = {"One":1,"Two":2,"Three":3}
print(DNumbers)

DNumbers_nKeys = {1:1,2:2,3:3}
print(DNumbers_nKeys)

DNumbers_sVals = {1:"One",2:"Two",3:"Three"}
print(DNumbers_sVals)

print(DNumbers_sVals[3])
print(DNumbers_sVals[1])

DNumbers_sVals[3] = "I made this."
print(DNumbers_sVals[3])

DNumbers_sVals.get(1,'This is the message, if no such key is in the dict.')
DNumbers_sVals.get(11,'This is the message, if no such key is in the dict.')

print(DNumbers_sVals[4])

DSomeDicts = {"DNumbers":DNumbers, "DNumbers_nKeys": DNumbers_nKeys}
print(DSomeDicts)

DSomeDicts["DNumbers"]
DSomeDicts.get("DNumbers")

DSomeDicts["DNumbers"] = [1,2,3]
print(DSomeDicts)

DNumbers["SomeInt"] = 1337
print(DNumbers)

DNumbers.pop("SomeInt")
print(DNumbers)


#### Exercises ####

# Create a variable of type list "LExercise" with the contents: "Anna", "Charles", "Peter", "Santa", "Eric"
LExercise = ["Anna", "Charles", "Peter", "Santa", "Eric"]
# Get the index of the element named "Santa"
LExercise.index("Santa")
# Get the element with the index 4
LExercise[4]
# Get the last element
LExercise[-1]
# Assign a string Variable with the contents of element with index 3, but only get the first three letters from the element!
SExerciseString = LExercise[3][:3]
####
# Create a variable of type dictionary "DExercise" with the key-value pairs: 4213-"Epic", 532-"Exclusive", 213-"Good", 5321-"Job"
DExercise = { 4213:"Epic", 532:"Exclusive", 213:"Good", 5321:"Job"}
# print the contents of the dictionary.
print(DExercise)
# Retrieve the list of keys.
DExercise.keys
# Retrieve the value for the key 532
DExercise[532]
####
# Create a list variable "LContainer" with the elements: [231,421,324,646],[21423,634,132],[123,765]
LContainer = [[231,421,324,646],[21423,634,132],[123,765]]
# Create a new variable iExampleMultiplication and assign the value of the multiplication between the 
# first element of the first list in LContainer and the third element of the second list in LContainer.
iExampleMultiplication = LContainer[0][0]*LContainer[1][2]