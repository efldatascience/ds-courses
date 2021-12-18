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