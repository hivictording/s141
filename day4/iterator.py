# Author: Victor Ding

from collections import Iterable
from collections import Iterator

print(isinstance([],Iterator))
print(isinstance([],Iterable))

a = [pow(x,2) for x in range(10)]
for i in a:
    print(i,end=' ')
b = iter(a)
print(isinstance(a,Iterable))
print(isinstance(a,Iterator))

print(isinstance(b,Iterable))
print(isinstance(b,Iterator))


