# # Author: Victor Ding
#
# import sys
# import pprint
# import os
#
# # print(sys.argv)
#
# # pprint.pprint(sys.path)
#
# #pprint.pprint(os.system("dir"))
#
# #print(os.system("dir"))
#
# cmd_display = os.system("dir")
#
# print('hey here is the display: ', cmd_display)

# print("victor ding".translate(str.maketrans('abcdefg','1234567')))

list1 = [1,2,4,3,2,5,'5']
set1 = set(list1)
print(set1)

list2 = [6,5,4,7,8,'5']
set2 = set(list2)

set3 = set([6,7,8,9,10])

# print(set1.difference(set2))
# print(set1.intersection(set2))
# print(set1.symmetric_difference(set2))

#isdisjoint() 方法用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False
# print(set1.isdisjoint(set2))
# print(set1.isdisjoint(set3))
#
print(set1 & set2)
print(set1 | set2)

#同样作用的写法
print(set1 - set2)
print(set1.difference(set2))

#同样作用的写法
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
#
# print(set1)
# print(set2)
#
# for l in list1:
#     print(l)
#
# set1.add(11)
# set1.update([11,12,13,12])
#update() 方法用于修改当前集合，可以添加新的元素或集合到当前集合中，如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略。

# 使用discard和remove都可以删除set当中的元素，区别就是remove的元素在set当中没有的话会报错，而discard不会。
# print(set1.remove(5))
# print(set1.discard(5))
# print(set1)
