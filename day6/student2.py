# Author: Victor Ding

class student():
    def __init__(self,name,sex):
        self.name = name
        self.__sex = sex

    def get_status(self):
        print("Your name is {name},your sex is {sex}".format(name=self.name,sex=self.__sex))


class primary_student(student):
    __tution_discount = 0.8

    def __init__(self,name,sex,grade,origin_tution):
        # student.__init__(self,name,sex)
        super(primary_student,self).__init__(name,sex)
        self.__grade = grade
        self.__origin_tution = origin_tution

    @property  #内部装饰器，把函数装饰成属性
    def get_status(self):
        super(primary_student,self).get_status()
        print("And your grade is {grade}".format(grade=self.__grade))

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self,new_grade):
        self.__grade = new_grade

    @property
    def tution(self):
        return self.__origin_tution * primary_student.__tution_discount

    def __gettution__(self):
        return self.__origin_tution * primary_student.__tution_discount

    @classmethod #类方法 可以直接被类调用 不需要默认传对象参数 只需要传一个类参数就可以了
    def change_tution_discount(cls,new_discount):
        cls.__tution_discount = new_discount


s1 = student("Victor","Male")
print(s1._student__sex) #访问内部变量的方式
s1.get_status()

ps1 = primary_student("Mario","Male","SK",10000)
ps1.get_status #实际是函数，但调用方法是属性 因为用了内部装饰器@property
print(ps1.__dict__)
print(ps1._student__sex)


print(ps1.grade)
ps1.grade = 'Grade One'
print(ps1.grade)

ps2 = primary_student("Victor","Male","Grade Two",20000)

print(ps1.tution,ps2.tution)
ps1.change_tution_discount(0.5)
print(ps1.tution,ps2.tution)
print(dir(ps2))
print(ps2.__gettution__())
# print(gettution(ps2))   #为啥不行？

print(isinstance(ps2,primary_student))
print(hasattr(ps1,'name'))
print(hasattr(ps2,'tution'))
print(getattr(ps2,"tution"))
# print(getattr(ps2,"__grade"))
# setattr(ps2,"name",'Mary')
# print(ps1.get_status)
print(hasattr(ps1,'get_status'))
print(getattr(ps1,'get_status'))




