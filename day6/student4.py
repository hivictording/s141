# Author: Victor Ding

class student(object):
    number = 0
    __slots__ = ('name','age') #定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

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


s1=student()
s1.name = 'Victor'
s1.sex = 'Male'