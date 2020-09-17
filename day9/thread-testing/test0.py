# Author: Victor Ding

# -*- coding: utf-8 -*-

# 用进程实现

import threading

import time


def sayhi(name, age):
    print("My name is {},I am {} years old".format(name, age))
    time.sleep(3)


sayhi("Victor", 44)
sayhi("Mary", 38)
print(threading.enumerate())
