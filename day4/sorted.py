# Author: Victor Ding

dict = {
    9: 0,
    1: 9,
    3: 5,
    2: 4,
    6: 6,
    5: 2,
}

# print(dict)
# print(sorted(dict))
# print(sorted(dict.keys()))
# print(sorted(dict.items()))
# print(sorted(dict.values()))
# print(sorted(dict.items(),key=lambda k:k[1]))
# print(sorted(dict.items(),key=lambda k:k[1],reverse=True ))

from operator import itemgetter
# #
# print(sorted(dict.items(),key=itemgetter(1)))

a = [1,2,3]
b = itemgetter(1)#定义函数b，获取对象的第1个域的值
print(b(a))
# 2 
# >>> b=operator.itemgetter(1,0)   //定义函数b，获取对象的第1个域和第0个的值
# >>> b(a) 
# (2, 1) 
#
# 要注意，operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值。

