# Author: Victor Ding

list1 = list(i for i in range(10))

list2 = [i for i in range(10)]

list3 = (i for i in range(10))

print(list1)
print(list2)
print(list3)

# for i in list1:
#     print(i)

# for i in list3:
#     print(i)

# print(list3.next())
# print(list3.__next__())


# for i in list3:
#     print(i)

# rozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。

alist = [1,2,3,4,6,3,8,6,1,9,10,11,6]
fs = frozenset(alist)
s = set(alist)
s.add(15)
print(s)

print(globals())  #以字典的方式返回所有变量


