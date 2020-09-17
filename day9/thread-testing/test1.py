# Author: Victor Ding

# -*- coding: utf-8 -*-

# 用线程实现

import threading

import time


def sayhi(name, age, interval):
    time.sleep(1)
    print("My name is {},I am {} years old".format(name, age))
    start_time = time.time()
    print("Thread {} started at {}".format(threading.current_thread().getName(), time.ctime(time.time())))
    time.sleep(interval)
    print("Thread {} stopped at {}".format(threading.current_thread().getName(), time.ctime(time.time())))
    print("Thread {} execution time: {}".format(threading.current_thread().getName(), time.time() - start_time))


thread_list = []
for i in range(10):
    new_thread = threading.Thread(name="vding{}".format(i), target=sayhi, args=('Victor{}'.format(i), i,  i+3))
    new_thread.setDaemon(True)
    thread_list.append(new_thread)

print('main thread start......')


for t in thread_list:
    t.start()
    t.join(1.0)
s_time = time.time()


# t1 = threading.Thread(name="vding", target=sayhi, args=('Victor', 44))
# t2 = threading.Thread(name="mzhu", target=sayhi, args=('Mary', 38))
#
# # t1.setDaemon(True)
# # t2.setDaemon(True)
# t1.start()
# t2.start()
# t1.join()
#
# print(threading.enumerate())
#
# time.sleep(2)
# print(t2.getName())
# print(t1.is_alive())
#
#


while True:
    c_time = time.time()
    if c_time - s_time > 10:
        print(c_time - s_time)
        break

print('main thread end......')
print(f'main thread execution time: {c_time - s_time}')
