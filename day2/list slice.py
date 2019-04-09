# Author: Victor Ding

list1 = [1,2,3,4,5,6,8,7,9,10,11,12,13,14,15]

print(list1[::-1]) # reverse the list
# 若  step < 0, 则表示从右向左进行切片。 此时，start必须大于end才有结果，否则为空。列如: s[5: 0: -1]的结果是'fedcb'
# 那么，s[::-1]表示从右往左，以步长为1进行切片; s[::2] 表示从左往右以步长为2进行切片

print(list1[::-2])

print(list(reversed(list1)))

print(sorted(list1))

print(list1)