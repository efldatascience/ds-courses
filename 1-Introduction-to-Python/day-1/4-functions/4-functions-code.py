##function that takes an integer as input an doubles it
def fDoubleMe(int1):
    result = 2*int1
    return result

##call function doubleMe and store it to a variable 
resultFromDoubleMe = fDoubleMe(12)
print(resultFromDoubleMe)

##make doubleMe more robust by checking the type of int1
def fDoubleMe(int1):
    if type(int1) is int:
        result = 2*int1
        return result
    else:
        print("int1 must be of type int.")
        return
        

##check whether the input argument (assumption: type numeric) is positive
def fIsPositive(number): 
    if number>=0: 
        return True 
    elif number<0: 
        return False 
fIsPositive(5)
fIsPositive(-10)


##skeleton for function exercises 
def fSumElems(list1):
    ##use a loop
    sume = 0
    for i in list1:
        sume += i
    return sume

def fSquareElems(list1):
    sq = [i*i for i in list1]
    return sq

##test your functions    
Ltest1 = [1, 6, 20, 12]
fSumElems(Ltest1)
fSquareElems(Ltest1)

##mean function
def fMean(list1):
    me = fSumElems(list1) / len(list1)
    return me

fMean(Ltest1)

##variance function
def fVariance(list1):
    var = fMean(fSquareElems(list1)) - fMean(list1)**2  
    return var

fVariance(Ltest1)

##lambda operator
squareMe = lambda x: x*x

##map operator
for i in range(10):
    print(i*i)
list(map(lambda x: x*x, range(10)))
##or
list(map(squareMe, range(10)))
