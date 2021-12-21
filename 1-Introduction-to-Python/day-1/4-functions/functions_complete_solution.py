# Examples discussed during the lecture Functions - Structure of Functions and Applications

# (1) Function that takes an integer as input an doubles it
def double_me(int1):
    result = 2 * int1
    return result


res = double_me(3)  # Store in variable res
print(res)
print(double_me(4))  # print immediately


# (2) Making double_me more robust by checking the type of int1
def double_me(int1):
    if type(int1) is int:
        result = 2 * int1
        return result
    else:
        print("int1 must be of type int.")
        return


print(double_me(10))

# (3) Function that takes an integer as input an doubles it
def is_positive(number):
    if number >= 0:
        return True
    elif number < 0:
        return False


print(is_positive(5))
print(is_positive(-10))

# ------------ EXERCISES IN THE LECTURE  ------------

# Test all functions using this list
mylist = [1, 6, 20, 12]

# Solutions
def sum_elems(list1):
    # use a loop
    sume = 0
    for i in list1:
        sume += i
    return sume

def square_elems(list1):
    # use a list comprehension
    sq = [i*i for i in list1]
    return sq


print(sum_elems(mylist))
print(square_elems(mylist))

def f_mean(list123):
    iN = len(list123)
    me = sum_elems(list123) / iN
    return me

print(f_mean(mylist))

def f_variance(list1):
    var = f_mean(square_elems(list1)) - f_mean(list1)**2
    return var

print(f_variance(mylist))

# lambda operator for a quick function implementation
square_me = lambda x: x*x

print(square_me(5))

# map operator to apply function to all list elements
res = list(map(square_me, mylist))
print(res)
# alternatively
res = list(map(lambda x: x*x, mylist))
print(res)