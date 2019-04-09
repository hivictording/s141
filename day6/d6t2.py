# Author: Victor Ding

# -*- coding: utf-8 -*-

class people():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print("{} is talking about his age,which is {}".format(self.name, self.age))


def eat(self):
    print("{} is eating breakfast".format(self.name))

# 反射：反射就是通过字符串的形式，导入模块；通过字符串的形式，去模块寻找指定函数，并执行。
# 利用字符串的形式去对象（模块）中操作（查找/获取/删除/添加）成员，一种基于字符串的事件驱动！
victor = people("Victor", 44)
print(hasattr(victor, 'talk'))

getattr(victor, 'talk')()
setattr(victor, 'age', 22)
getattr(victor, 'talk')()

setattr(victor,'breakfast',eat)
victor.breakfast(victor)
