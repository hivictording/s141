# Author: Victor Ding

from functools import wraps

def logging(age):
    def inner_logging(func):
        def wrapper(*args, **kwargs):
            print("This is the name of the function: ", func.__name__)
            res = func(*args, **kwargs) + age
            print("This is the doc of the function: ", func.__doc__)
            print(res)
        return wrapper
    return inner_logging


# method 2
@logging(10)
def addition(a,b):
    print("welcome home")
    return a+b

# # method 1
# addition = logging(addition,age=10)


addition(1,2)

