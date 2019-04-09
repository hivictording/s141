# Author: Victor Ding

# -*- coding: utf-8 -*-

from multiprocessing import Process,Manager
import os

def func(dd,ll):
    ll.append(os.getpid())
    dd[os.getpid()] = os.getpid()

if __name__ == "__main__":
    with Manager() as manager:
        a_dict = manager.dict()
        a_dict['name'] = 'Victor'
        a_list = manager.list(range(3))

        p_list = [Process(target=func,args=(a_dict,a_list),) for i in range(3)]
        for p in p_list:
            p.start()
        for p in p_list:
            p.join()   #必须要join,为啥？

        print(a_list)
        print(a_dict)
