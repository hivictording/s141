# Author: Victor Ding
#
# -*- coding: utf-8 -*-

from multiprocessing import Process,Pool
import os,time

def hello(i):
    time.sleep(1)
    print("hello:{}".format(i))
    print("in process: {}".format(os.getpid()))
    return i+100
    # time.sleep(1)


def wrap_up(arg):   #arg是hello函数的返回值
    print("wrap-up:{}".format(arg))
    print("Wrap-up PID: {}".format(os.getpid()))

if __name__ == "__main__":
    pool = Pool(5)

    for i in range(10):
        pool.apply_async(func=hello,args=(i,),callback=wrap_up)

    pool.close()
    pool.join()

