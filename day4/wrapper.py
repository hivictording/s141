# Author: Victor Ding

from functools import wraps

def logging(func):
    def wrapper(*args,**kwargs):
        print("This is the name of the function: ",func.__name__)
        res = func(*args,**kwargs)
        print("This is the doc of the function: ",func.__doc__)
        print(res)
    return wrapper

# method 2
# @logging
def addition(a,b):
    print("welcome home")
    return a+b

# # method 1
# addition = logging(addition)
# addition(1,2)

addition = logging(addition)
addition(4,9)

# print(addition.__name__)