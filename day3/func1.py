# Author: Victor Ding

def test(*args):
    list1 = list(args)
    list1.append(6)
    print(list1[::-1])

# def test2(*args):
#     list = []
#     for i,d in enumerate(args):
#         print(i+1)
#         print(type(d))
#         list.append(d)
#     return list

def test2(**kwargs):
    list = []
    for i,d in kwargs.items():
        print(i,d)
        print(type(d))
        list.append(d)
    return list

test(1,2,3,4,5)

# 列表前面加星号作用是将列表解开成几个独立的参数，传入函数，
test(*[11,12,13,14,15])

# 列表前面加连个星号作用是将字典解开成几个独立的参数，传入函数，
dd = test2(**{'name':'a','sex':'b','age':'c','hometown':'d','country':'e'})

test2(name='victor')

for d in dd:
    print(d)