# Author: Victor Ding

def fib(max):
    n,a,b = 0,0,1

    while n < max:
        yield b
        # a,b = b,a+b
        temp =a
        a =b
        b =temp+b
        n +=1
    print("done")

# for i in fib(50):
#     print(i)

f = fib(5)
print(f)

g=next(f)
print(g)
g = f.__next__()
print(g)
g=next(f)
print(g)
g = f.__next__()
print(g)
