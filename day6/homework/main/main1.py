# Author: Victor Ding
# -*- coding: utf-8 -*-

import pickle
import os

current_dir = os.path.dirname(os.getcwd())

list_school = []
list_course = []

try:
    with open(current_dir+"\\database\\schools.pickle","rb") as fh_schools, \
         open(current_dir+"\\database\\courses.pickle","rb") as fh_courses:
         list_school = pickle.load(fh_schools)
         list_course = pickle.load(fh_courses)
except:
    pass

print(list_school)
school_length = len(list_school)
course_length = len(list_course)

class Schools():
    global school_length
    schoolCount = school_length
    def __init__(self,name,location):
        self.schoolName = name
        self.schoolLocation = location
        Schools.schoolCount += 1
        self.__schoolId = Schools.schoolCount
        self.courseId = []

    # def getCourseId(self):
    #     return self.courseId
    #
    # def setCourseId(self,courseId):
    #     self.courseId = courseId

    @property
    def schoolId(self):
        return self.__schoolId

class Courses():
    global course_length
    courseCount = course_length
    def __init__(self,name):
        self.courseName = name
        Courses.courseCount += 1
        self.__courseId = Courses.courseCount

    @property
    def courseId(self):
        return self.__courseId

    @property
    def coursePrice(self):
        return self.__coursePrice

    @coursePrice.setter
    def coursePrice(self,price):
        self.__coursePrice = price

    @property
    def coursePeriod(self):
        return self.__coursePeriod

    @coursePeriod.setter
    def coursePeriod(self, period):
        self.__coursePeriod = period

def root_menu():
    print("Welcome to SonicWALL School!\n")
    print("1            For Students         ")
    print("2            For Teachers         ")
    print("3            For Admins           ")
    print("99            Quit                 ")

def admin_menu():
    print("1            Manage Schools        ")
    print("2            Manage Courses         ")
    print("3            Manage Classes           ")
    print("4            Manager Teachers                 ")
    print("99           Exit                  ")

def admin_school_menu():
    print("1            Add Schools        ")
    print("2            Add courses to school         ")
    print("3            Add classes to school           ")
    print("4            Add teachers to school                 ")
    print("99           Exit                ")

def teacher_menu():
    print("1            View Classes         ")
    print("2            Modify Students Data         ")
    print("5            Exit                ")

def student_menu():
    print("1            Registration         ")
    print("2            Deregistration         ")
    print("5            Exit               ")

dict_school = {}
dict_course = {}

def createSchool(name,location):
    school = Schools(name,location)

    #把类对象转换成字典
    dict_school = dict((name, getattr(school, name)) for name in dir(school) if \
     not name.startswith('__') and not name.startswith('_') and name != 'schoolCount')

    list_school.append(dict_school)
    with open(current_dir+"\\database\\schools.pickle","wb") as fh_schools:
        pickle.dump(list_school,fh_schools)
    print("You have successfully created school: Name: {}; School_ID: {}; Location: {}".format(school.schoolName,school.schoolId,school.schoolLocation))

def updateSchoolCourse(schoolId,courseId):
    school_list = getSchools()
    for school in school_list:
        if schoolId == school.get('schoolId'):
            school['courseId'].append(courseId)
    updateSchools(school_list)


def createCourse(name,price,period):
    course = Courses(name)
    course.coursePrice = price
    course.coursePeriod = period

    #把类对象转换成字典
    dict_course = dict((name, getattr(course, name)) for name in dir(course) if \
     not name.startswith('__') and not name.startswith('_') and name != 'courseCount')
    print(dict_course,type(dict_course))
    list_course.append(dict_course)
    with open(current_dir+"\\database\\courses.pickle","wb") as fh_courses:
        pickle.dump(list_course,fh_courses)
    print("You have successfully created course: Name: {}; Course_ID: {}; Price: {}; Period: {}".format(course.courseName,course.courseId,course.coursePrice,course.coursePeriod))

def getSchools():
    with open(current_dir + "\\database\\schools.pickle", "rb") as fh_schools:
        return pickle.load(fh_schools)

def printSchools():
    list_school = getSchools()

    for school in list_school:
        print("School ID:  {};   School Name: {}".format(school['schoolId'], school['schoolName']))

def updateSchools(obj):
    with open(current_dir + "\\database\\schools.pickle", "wb") as fh_schools:
        pickle.dump(obj,fh_schools)

def getCourses():
    with open(current_dir + "\\database\\courses.pickle", "rb") as fh_courses:
        return pickle.load(fh_courses)

def printCourses():
    list_course = getCourses()

    for course in list_course:
        print("Course ID:  {};   Course Name: {}".format(course.get('courseId'),course['courseName']))

if __name__ == "__main__":

    while True:
        root_menu()
        option = input("\nPlease select an option to continue:       ")
        if option.isdigit():
            if int(option) == 99:
                exit()
            elif int(option) == 3: #管理员
                while True:
                    admin_menu()
                    option = input("\nAdmin, Please select your option:       ")
                    if option.isdigit():
                        if int(option) == 99:
                            break
                        elif int(option) == 1: #管理学校
                            admin_school_menu()
                            option = input("\nAdmin, Please select your option:       ")
                            if option.isdigit():
                                if int(option) == 99:
                                    break
                                elif int(option) == 1: # Add Schools
                                    s_name = input("Please input the school name:       ")
                                    s_location = input("Please input the school location:       ")
                                    createSchool(s_name,s_location)
                                elif int(option) == 2:  # Add courses to school
                                    printSchools()
                                    school_option = input("\nAdmin, Please enter the School ID:       ")
                                    printCourses()
                                    course_option = input("\nAdmin, Please enter the course ID:       ")
                                    if school_option.isdigit() and course_option.isdigit():
                                        updateSchoolCourse(int(school_option),int(course_option))

                        elif int(option) == 2: #管理课程
                            course_name = input("Please input the course name:       ")
                            course_price = input("Please input the price of this course:       ")
                            course_period = input("Please input the period of this course:       ")
                            createCourse(course_name,course_price,course_period)
                        elif int(option) == 3: #管理班级
                            pass
                        elif int(option) == 4: #管理老师
                            pass
                        else:
                            pass

            elif int(option) == 2: #老师
                teacher_menu()
            elif int(option) == 1: #学生
                student_menu()
        else:
            print("Invalid Option!!!\n")
            root_menu()
