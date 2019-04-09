# Author: Victor Ding

# -*- coding: utf-8 -*-

import multiprocessing
import os

def info(q):
    # print("Parent process Id:{}".format(os.getppid()))
    # print("Child process Id:{}".format(os.getpid()))
    # print(q.get())
    q.put("TWO")


if __name__ == "__main__":
    # info()
    qq = multiprocessing.Queue()
    # qq.put('ONE')
    # print(qq.get())
    p = multiprocessing.Process(target=info,args=(qq,),)
    p.start()
    print(qq.get())
    p.join()

