# Author: Victor Ding

# -*- coding: utf-8 -*-

import threading
import time
import queue
import random

NUMBER = 0
q = queue.Queue(10)

def producer(name):
    global q
    count = 1
    while 1:
        if not q.full():
            r = random.randint(1,10)
            q.put(count)
            print("{} produced dumpling {},            {} dumplings left".format(name,count,q.qsize()))
            count +=1
            time.sleep(r)

def consumer(name):
    global q
    while 1:
        if not q.empty():
            r = random.randint(1,5)
            count = q.get()
            print("{} eated dumpling {},               {} dumplings left".format(name,count,q.qsize()))
            time.sleep(r)

p1 = threading.Thread(target=producer,name="producer 1",args=('Victor',),)
c1 = threading.Thread(target=consumer,name="consumer 1",args=('Mary',),)
c2 = threading.Thread(target=consumer,name="consumer 2",args=('Mario',),)


p1.start()
c1.start()
c2.start()

p1.join()
c1.join()
c2.join()

