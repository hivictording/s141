# Author: Victor Ding

# -*- coding: utf-8 -*-

"""
Barriers字面意思是“屏障”，是Python线程（或进程）同步原语。每个线程中都调用wait()方法，当其中一个线程执行到wait方法处会立阻塞；
一直等到所有线程都执行到wait方法处，所有线程再继续执行
"""

import threading
import time

class Workers(threading.Thread):
    def __init__(self,c,i):
        super().__init__()
        self.c = c
        self.setName("Worker"+ str(i))

    def run(self):
        print("{} started waiting, {} workers waiting".format(threading.current_thread().getName(), self.c.n_waiting))
        self.c.wait()
        print("{} started working".format(threading.current_thread().getName()))

barrier = threading.Barrier(5)

w=[]

for i in range(5):
    temp = Workers(barrier,i)
    w.append(temp)

for k in w:
    k.start()
    time.sleep(0.5)

for k in w:
    k.join()
