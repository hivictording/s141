# Author: Victor Ding

from functools import reduce

print(sum(range(1,101,2)))

def minus(a,b):
    return a+b

def minus1(a,b,c):
    return a+b+c

def test(a):
    return a **2

print(reduce(minus,range(1,101,2)))

print(reduce(lambda x,y:x+y,range(1,101,2)))
#
print(reduce(lambda x,y:x+y, range(1,101,2)))

# print(list(map(test,range(100))))
#
# print(list(map(lambda x:x**2,range(100))))
#
print(list(map(minus1,range(100),range(100),range(100))))
#
# print(list(map(lambda a,b:a+b,range(100),range(100))))
#
# ge = filter(lambda x:x % 3 ==0,range(1000))
#
# for i in ge:
#     print(i, end="+")


l = list(i for i in range(1,10,2))
print(l)
l = [i for i in range(1,10,2)]
print(l)
l = (i for i in range(1,10,2))
print(l)

l = (i for i in range(1,10,2))
print(*l)

website = ["www.pythontab.com","bbs.vlan.com","docs.cisco.com"]

def wordCount(string):
    return len(string)

siteNameLength = list(map(wordCount, website))
print(siteNameLength)

siteNameLength = list(map(lambda s:len(s),website))
print(siteNameLength)

siteNameLength = [len(s) for s in website]
print(siteNameLength)

siteNameLength = (len(s) for s in website)
print(siteNameLength)



