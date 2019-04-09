# Author: Victor Ding

# -*- coding: utf-8 -*-

from multiprocessing import Process,Pipe
import os

def hello(c):
    # print("Hello World")
    print(c.recv())
    c.close()

if __name__ == "__main__":
    p_conn,c_conn = Pipe()

    # p_list = [Process(target=hello,args=(c_conn,)) for i in range(1)]
    p = Process(target=hello, args=(c_conn,))
    p.start()
    p_conn.send("Hello from  PID {}".format(os.getpid())) #为什么要写在start和join的中间
    p.join()
    # for p in p_list:
    #     p.start()
    #
    # for p in p_list:
    #     p.join()


