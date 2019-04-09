# Author: Victor Ding


def logging_1(func):
    def wrapper(*args,**kwargs):
        print("This is the first wrapper of ",func.__name__)
        func(*args,**kwargs)
        print("This is the end of first wrapper of ",func.__name__)
    return wrapper

def logging_2(func):
    def wrapper(*args,**kwargs):
        print("This is the second wrapper of ",func.__name__)
        print(func(*args,**kwargs))
        print("This is the end of second wrapper of ",func.__name__)
    return wrapper

# @logging_1
# @logging_2
def test1(a,b,c):
    return a+b+c

@logging_1
@logging_2
def test2(a,b):
    return a-b

@logging_1
@logging_2
def test3(a):
    return a+1


test1 = logging_1(logging_2(test1))
test1(9,6,10)

test2(9,6)

test3(9)