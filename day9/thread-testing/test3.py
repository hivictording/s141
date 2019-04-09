# Author: Victor Ding

# -*- coding: utf-8 -*-

import threading
import time

def daemon():
    print("{} is starting".format(threading.current_thread().getName()))
    time.sleep(3)
    print("{} is exiting".format(threading.current_thread().getName()))

def non_daemon():
    print("{} is starting".format(threading.current_thread().getName()))
    print("{} is exiting".format(threading.current_thread().getName()))

d = threading.Thread(name="Daemon",target=daemon,daemon=True)
# d = threading.Thread(name="Daemon",target=daemon)
t = threading.Thread(name="Non_Deamon",target=non_daemon)

d.start()
t.start()

print(threading.enumerate())
# d.join()
d.join(1.5)
# t.join()

print(t.isAlive())
print(d.isAlive())

