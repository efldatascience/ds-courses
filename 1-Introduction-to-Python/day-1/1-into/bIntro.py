#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 10:49:17 2019

@author: wiim
"""

# Hello World
# While small test programs have existed since the development of 
# programmable computers, the tradition of using the phrase 
# "Hello, World!" as a test message was influenced by an 
# example program in the seminal 1978 book The C Programming Language.
# The example program in that book prints "hello, world", 
# and was inherited from a 1974 Bell Laboratories internal memorandum 
# by Brian Kernighan, Programming in C: A Tutorial
print('Hello World')


# Integer:
# int (signed integers) − They are often called just integers or ints, 
# are positive or negative whole numbers with no decimal point.
iOne = 1


# Create two variable 'iOne' and 'iTwo'. 
# Assign the values 2 and 5 to each of these variables. 
iOne = 2
iTwo = 5

# Perform the following operations with the variables and 
# print all results to the console. 
# iMulti is the multiplication of the two variables.
iMulti = iOne * iTwo
print(iMulti)

#iAdd is the addition of the two variables.
iAdd = iOne + iTwo
print(iAdd)

# iSub is the subtraction of the two variables. Started with iOne. 
iSub = iOne - iTwo
print(iSub)

# iDiff is the division of iOne by iTwo.
iDiff = iOne / iTwo
print(iDiff)


# Create two variable 'iOne' and 'iTwo'. 
# Assign the values 2 and 5 to each of these variables. 
dOne = 2.5
dTwo = 5.5

# Perform the following operations with the variables and 
# print all results to the console. 
# dMulti is the multiplication of the two variables.
dMulti = dOne * dTwo
print(dMulti)

#dAdd is the addition of the two variables.
dAdd = dOne + dTwo
print(dAdd)

# dSub is the subtraction of the two variables. Started with dOne. 
dSub = dOne - dTwo
print(dSub)

# dDiff is the division of dOne by dTwo.
dDiff = dOne / dTwo
print(dDiff)

# Chars are symbols.
# In Python, char is short for character.
# All characters in all languages can be represented.
# This representation is in the Unicode format.
# Unicode is a computer encoding methodology that assigns
# a unique number for every character.
# It doesn't matter what language, or computer platform it's on.
# Lets try to allocate a char to a variable and get the unicode number.
# @code: ord() Given a string representing one Unicode character
# @source: https://docs.python.org/3/library/functions.html
char = 'A'
print(ord(char))

# Chars forms strings (words)
#sWord = 'D' + 'A' + 'T' + 'A'
#print(sWord)

# Concatenated string
sWordOne = 'I Love'
sWordTwo = 'data'
sStatement = sWordOne + ' ' + sWordTwo
print(sStatement)

iCountSubStrings = sStatement.count('Love')
print(iCountSubStrings)

sStatementLower = sStatement.lower()
print(sStatementLower)

# Multiply words
sToMultiply = 'Data'
print(3 * sToMultiply)

# Write something
sName = 'Benny'
print('My name is: ' + sName)

# Boolean
# Boolean values are the two constant objects False and True.
# They are used to represent truth values (false or true).
# Logical operations can quickly become complex. 
bTrue = True
bFalse = False
print(bTrue)
print('True and True is:', bTrue and bTrue)
print('False and False is:', bFalse and bFalse)
print('True and False is:', bTrue and bFalse)
print('True and False is:', bTrue and bFalse)

print('True or True is:', bTrue or bTrue)
print('False or False is:', bFalse or bFalse)
print('True or False is:', bTrue or bFalse)
print('True or False is:', bTrue or bFalse)


