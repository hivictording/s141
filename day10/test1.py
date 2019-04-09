# Author: Victor Ding

# -*- coding: utf-8 -*-

import threading,multiprocessing
import time

def ttt(t):
    print("This is Thread {}".format(t))
    time.sleep(5)

def sayhi():
    tlist = [threading.Thread(target=ttt,args=("name%s"%(str(i)),),) for i in range(3)]
    for i in tlist:
        i.start()
    for i in threading.enumerate():
        print("Hello, I am thread:%s" % (i.name))
    for i in tlist:
        i.join()

    # time.sleep(2)
    # print("Hello World")

if __name__ == '__main__':
    p = multiprocessing.Process(target=sayhi)
    p.start()