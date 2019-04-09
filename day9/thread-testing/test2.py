# Author: Victor Ding

# -*- coding: utf-8 -*-

import threading
import time
import random

# At start-up, a Thread does some basic initialization and then calls its run() method,
# which calls the target function passed to the constructor. To create a subclass of Thread, override run() to do whatever is necessary.

class People(threading.Thread):
    # def __init__(self, group=None, target=None, name=None,   #参数的写法看不懂，需要再研究
    #              args=(), kwargs=None, *, daemon=None):
    #     # super(People,self).__init__()
    #     super().__init__(group=group, target=target, name=name,daemon=daemon)
    #     print(*args)
    #     self.p_name = args[0]
    #     self.p_age = args[1]

    def __init__(self,p_name,p_age,t_name):
        super().__init__()
        self.p_name = p_name
        self.p_age = p_age
        self.setDaemon(True)
        self.setName(t_name)

    def run(self):
        t = random.randint(1,20)
        print("{} is started for {} seconds".format(threading.current_thread().getName(),t))
        print("My name is {},I am {} years old".format(self.p_name,self.p_age))
        time.sleep(t)
        print("{} is stopped".format(threading.current_thread().getName()))

# t1 = People(args=("Victor",44),name="vding",daemon=True)
# t2 = People(args=("mary",38),name="mzhu")

t1 = People("victor",44,"vding")
t2 = People("victor",38,"mzhu")

t1.start()
t2.start()

main_thread = threading.main_thread()

for th in threading.enumerate():
    if th == main_thread: continue
    if th.isDaemon(): th.join(1)





