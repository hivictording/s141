# Author: Victor Ding

# -*- coding: utf-8 -*-

import threading
import time

NUMBER = 0

def producer(c):
    global NUMBER
    time.sleep(1)
    try:
        c.acquire()
        while 1:
            while NUMBER < 100:
                NUMBER += 30
                print("Produced 30 dumplings!")
            else:
                print("We have {} dumplings,that is enough!".format(NUMBER))
                time.sleep(1)
                c.notify()
                c.wait()
    finally:
        c.release()

def consumer(c):
    global NUMBER
    with c:
        c.wait()
        while 1:
            while NUMBER >= 50:
                NUMBER -= 13
                print("Consumed 13 Dumplings!")
            else:
                print("Only {} dumplings left!".format(NUMBER))
                time.sleep(1)
                c.notify()
                c.wait()



cond = threading.Condition()
prod = threading.Thread(target=producer,name='Producer',args=(cond,),)
cons = threading.Thread(target=consumer,name='Consumer',args=(cond,),)

prod.start()
cons.start()
prod.join()
cons.join()
