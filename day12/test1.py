# Author: Victor Ding

# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,Index
from sqlalchemy.dialects import mysql
from sqlalchemy import ForeignKeyConstraint,PrimaryKeyConstraint,UniqueConstraint,CheckConstraint
from datetime import datetime
from sqlalchemy import desc

#connect to mysql
victordb = create_engine('mysql+pymysql://vding:password@192.168.2.22/victordb',echo=True)
victordb.connect()

#Create session
session = sessionmaker(bind=victordb)
session = session()

# create an instance of declarative_base
base = declarative_base()

class Department(base): # inherit from the declarative_base
    __tablename__ = 'tb_dept'
    id = Column('id',Integer,primary_key=True,nullable=False,autoincrement=True)
    name = Column('name',String(20),nullable=False)
    loc = Column('location',String(50),nullable=False)

    def __repr__(self):
        return ("Department Details: (ID:{};Name:{};Location:{})".format(self.id,self.name,self.loc))

class Student(base):
    __tablename__ = 'tb_stud'
    __table_args__ = (ForeignKeyConstraint(['dept_id'],['tb_dept.id']),CheckConstraint('tuition>0',name='tuition_positive'))
    id = Column('id',Integer,primary_key=True,autoincrement=True,nullable=False)
    name = Column('name',mysql.VARCHAR(20),nullable=False)
    gender = Column('gender',mysql.ENUM('Male','Female'),nullable=False)
    dept_id = Column('dept_id',Integer,nullable=False)
    # either using "ForeignKey" here, or use ForeignKeyConstraint Above
    # dept_id = Column('dept_id',Integer,nullable=False,ForeignKey=('tb_dept.id'))
    tuition = Column('tuition',mysql.FLOAT,nullable=False)
    registration_date = Column('registration_date',mysql.DATE,nullable=False,default=datetime.now())

base.metadata.create_all(victordb) # create the table if the table does not exist;

#插入一条数据
dept_single_data = Department(name='Science',loc='Toronto')
session.add(dept_single_data)
session.commit()

#插入多条数据
dept_data1 = Department(name='Arts',loc='Montreal')
dept_data2 = Department(name='Sports',loc='Ottawa')
session.add(dept_data1)
session.add(dept_data2)
session.flush() #A flush is like a commit; however, it doesn’t perform a database commit and end the transaction.

#批量插入数据
# 方法1
# dept_data = [Department(name='dept'+str(i),loc='loc'+str(i)) for i in range(100)]
# session.bulk_save_objects(dept_data)
# 方法2
# dept_dict = [dict(name='dept'+str(i),loc='loc'+str(i)) for i in range(100)]
# session.bulk_insert_mappings(Department,dept_dict)
# session.commit()
# 方法3
dept_data = [Department(name='dept'+str(i),loc='loc'+str(i)) for i in range(100)]
for dept in dept_data:
    session.add(dept)
session.commit()

#查询数据
#方法1
# departments = session.query(Department).all()
# for dept in departments:
#     print(dept.id,dept.name,dept.loc)

#方法2
# for dept in session.query(Department):
#     print(dept.id,dept.name,dept.loc)

#查询结果的筛选
# result_class = session.query(Department)   #是一个类
# result_list =  session.query(Department).all()  #是一个列表
# print(result_list[0])
# print(dir(result_class))
# print(session.query(Department).get(2))

#切片
# print(session.query(Department)[:2]) #not efficient
# print(session.query(Department).limit(2)) # efficient


#one()函数,Queries all the rows, and raises an exception if anything other than a single result is returned.
# print(session.query(Department).one())

#只查询某些字段
# for dept in session.query(Department.id,Department.name):
#     print(dept.id,dept.name)

#排序
for dept in session.query(Department).order_by(Department.name):
    print(dept.id,dept.name,dept.loc)

#降序
for dept in session.query(Department).order_by(desc(Department.name)):
    print(dept.id, dept.name, dept.loc)






