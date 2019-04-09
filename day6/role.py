class role(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.__age = age #私有属性
        self.sex = sex

    def findName(self):
        print(f'your name is {self.name}')

    #私有函数，私有方法
    def __findSex(self):
        print(f'Your sex is {self.sex}')

    def findAge(self):
        print(f'Your age is {self.__age}')

# r = role('victor',44,'male')
#
# print(r.name)
# # print(r.__age)
#
# r.findName()
# # r.__findSex()
# r.findAge()

class canada(role):
    # def __init__(self):
    #     role.__init__(self)

    def findName(self):
        role.findName(self)
        print("Your name is {0} and your nationality is Canada".format(self.name))

c = canada("Mary",38,"Female")
c.findName()

