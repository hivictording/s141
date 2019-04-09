# Author: Victor Ding

def gene(max):
    n,a,b = 0,0,1

    while n < max:
        yie = yield b
        print(yie)
        a,b = b,b+a
        n +=1

# for i in gene(5):
#     print(i)

g = gene(5)
next(g)
g.send("hello")
next(g)


