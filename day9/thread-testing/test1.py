# Author: Victor Ding

# -*- coding: utf-8 -*-

#用线程实现

import threading

import time

def sayhi(name,age):
    print("My name is {},I am {} years old".format(name,age))
    print(threading.current_thread().getName())
    time.sleep(3)

t1 = threading.Thread(name="vding",target=sayhi,args=('Victor',44))
t2 = threading.Thread(name="mzhu",target=sayhi,args=('Mary',38))

t1.start()
t2.start()

print(threading.enumerate())

time.sleep(2)
print(t2.getName())
print(t1.isAlive())





