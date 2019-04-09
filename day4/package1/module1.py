# Author: Victor Ding

def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

if __name__ == '__main__':
    add(2,3)
else:
    print("You're calling the module %s" %__name__)