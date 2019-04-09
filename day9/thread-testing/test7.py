# Author: Victor Ding

# -*- coding: utf-8 -*-

"""
python线程的事件用于主线程控制其他线程的执行，事件主要提供了三个方法wait、clear、set

事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行 event.wait 方法时就会阻塞，如果“Flag”值为True，
那么执行event.wait 方法时便不再阻塞。

clear：将“Flag”设置为False
set：将“Flag”设置为True
用 threading.Event 实现线程间通信，使用threading.Event可以使一个线程等待其他线程的通知，我们把这个Event传递到线程对象中，

Event默认内置了一个标志，初始值为False。一旦该线程通过wait()方法进入等待状态，直到另一个线程调用该Event的set()方法将内置标志设置为True时，
该Event会通知所有等待状态的线程恢复运行。
"""

import threading
import logging
import time

def wait_for_event(e):
    logging.debug("wait for event starting:")
    print(e.is_set())
    event_is_set = e.wait()
    print(e.is_set())
    logging.debug('event set: %s', event_is_set)

def wait_for_event_timeout(e):
    logging.debug("wait for event starting:")
    event_is_set = e.wait(5)
    logging.debug('event set: %s', event_is_set)
    if e.is_set():
        print("event is set set set")
    else:
        print("event is clear clear clear")

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

e = threading.Event();
# e.set()
# t1 = threading.Thread(name='block',target=wait_for_event,args=(e,),)
# t1.start()

t2 = threading.Thread(target=wait_for_event_timeout,name='non-block',args=(e,),)
t2.start()


logging.debug('Waiting before calling Event.set()')
time.sleep(2)
e.set()
logging.debug('Event is set')