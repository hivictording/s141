# Author: Victor Ding

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。是生成器

a = [1,2,3]
b = [4,5,6]

i1,i2,i3 = zip(a,b)
print(i1,i2,i3)

zipped = zip(a,b)
i1,i2,i3 = [*zipped]
print(i1,i2,i3)

zipped = zip(a,b)
# print(list(zipped))
# print(next(zipped))
for z in zipped:
    print(z)

zipped = zip(a,b)
# print(zipped)
# print(*zipped)
a1,a2=zip(*zipped)
print(a1)
print(list(a1),list(a2))

# from itertools import zip_longest  # 相当于python 2中的 zipped = map(None,a,b)
#
# a = [1,2,3]
# b = [4,5,6,7,8,9,10]
# c = [11,12,13,14,15,16,17,18]
#
# zipped = zip_longest(a,b,c,fillvalue=88)
#
# for i in zipped:
#     print(i)
#
# zipped = zip_longest(a,b,c,fillvalue=88)
# a1,b1,c1 = zip_longest(*zipped)
# print(a1,b1,c1)






