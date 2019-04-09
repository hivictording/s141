class role(object):
    def __init__(self,*args):
        self.name = args[0]
        self.__age = args[1] #私有属性
        self.sex = args[2]

    def findName(self):
        print(f'your name is {self.name}')

    #私有函数，私有方法
    def __findSex(self):
        print(f'Your sex is {self.sex}')

    def findAge(self):
        print(f'Your age is {self.__age}')

r = role('victor',44,'male')

print(r.name)
# print(r.__age)

r.findName()
# r.__findSex()
r.findAge()


