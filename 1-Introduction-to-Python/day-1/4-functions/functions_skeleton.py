# Examples discussed during the lecture Functions - Structure of Functions and Applications

#%%
# (1) Function that takes an integer as input an doubles it
def double_me(int1):
    result = 2 * int1
    return result

# Experiment with the function!






#%%
# (2) Function that calculates the base to the power of ex
def expo(base, ex=2): 
    result = base**ex
    return result







#%%
# (3) Function that checks whether number is positive or negative
def is_positive(number):
    if number >= 0:  # zero is defined as positive
        return True
    elif number < 0:
        return False





#%%
# (4) Making double_me more robust by checking the type of int1
def double_me(int1):
    if type(int1) is int:
        result = 2 * int1
        return result
    else:
        print("int1 must be of type int.")
        return




#%%
# ------------ EXERCISES IN THE LECTURE  ------------

# Test all functions using this list
mylist = [1, 6, 20, 12]

#%%
# Solutions
