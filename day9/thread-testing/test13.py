# Author: Victor Ding

# -*- coding: utf-8 -*-

"""
信号量通常用于防范容量有限的资源，例如数据库服务器。一般而言信号量可以控制释放固定量的线程。
比如启动100个线程，信号量的控制值设为5，那么前5个线程拿到信号量之后，其余线程只能阻塞，等到这5个线程释放信号量锁之后才能去拿锁。
"""

import threading
import time

class Worker(threading.Thread):
    def __init__(self,i,sem):
        super().__init__()
        self.sem = sem
        self.setName("Worker" + str(i))

    def run(self):
        with self.sem:
            print("{} started working".format(self.name))
            time.sleep(3)
            print("{} stopped working".format(self.getName()))

workers = []
semaphore = threading.Semaphore(2)

for i in range(50):
    workers.append(Worker(i,semaphore))

for w in workers:
    w.start()

for w in workers:
    w.join()