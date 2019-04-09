# Author: Victor Ding

class student():
    def __init__(self,name,sex):
        self.name = name
        self.__sex = sex

    def get_status(self):
        print("Your name is {name},your sex is {sex}".format(name=self.name,sex=self.__sex))


class primary_student(student):
    def __init__(self,name,sex,grade):
        # student.__init__(self,name,sex)
        super(primary_student,self).__init__(name,sex)
        self.grade = grade

    def get_status(self):
        super(primary_student,self).get_status()
        print("And your grade is {grade}".format(grade=self.grade))

s1 = student("Victor","Male")
print(s1._student__sex) #访问内部变量的方式

ps1 = primary_student("Mario","Male","SK")
ps1.get_status()
print(ps1.__dict__)
print(ps1._student__sex)



# s1 = student("Mario","Male")
# s1.get_status()
