# Author: Victor Ding

# -*- coding: utf-8 -*-

import greenlet

def test1():
    print("12")
    t2.switch()
    print("56")
    t2.switch()

def test2():
    print("34")
    t1.switch()
    print("78")

t1 = greenlet.greenlet(test1)
t2 = greenlet.greenlet(test2)

t1.switch()
