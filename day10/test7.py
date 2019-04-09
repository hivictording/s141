# Author: Victor Ding

# -*- coding: utf-8 -*-

import gevent
import time

N = 1

def test1(n):
    global N
    n = N + n
    print(str(n+1))
    gevent.sleep(2)
    print(str(n+4))

def test2(n):
    global N
    n = N + n + 1
    print(str(n+1))
    gevent.sleep(1)
    print(str(n+2))

test = gevent.joinall([gevent.spawn(test1,10),gevent.spawn(test2,10)])
