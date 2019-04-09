# Author: Victor Ding

#实现每生成一个子类就计数的功能，目前搞不清楚直接示用类名和使用classmethod的'cls'的区别
class student(object):
    number = 0

    def __init__(self):
        # student.set_number()
        self.set_number()

    # @classmethod
    def get_number(self):
        return student.number

    # @classmethod
    # def set_number(cls):
    #     cls.number += 1

    def set_number(self):
        student.number += 1

class primary_student(student):
    # def __init__(self):
    #     super(primary_student,self).__init__()
    #     # student.__init__(self)

    # @classmethod
    # def set_number(self):
    #     student.set_number()
    pass

s1 = student()
print(s1.get_number())
s2 = student()
print(s2.get_number())
s3 = student()
print(s3.get_number())
print(primary_student.number)
s4 = primary_student()
print(student.number)
