# Author: Victor Ding

# -*- coding: utf-8 -*-

"""
死锁解决办法：
1、使用 try..except..finally 语句处理异常、保证锁的释放
2、with 语句上下文管理，锁对象支持上下文管理。只要实现了__enter__和__exit__魔术方法的对象都支持上下文管理。

acquire(blocking=True，timeout=-1)
以阻塞或非阻塞的方式获取一个锁
当 blocking 参数为 True（默认）时，调用者的线程会阻塞直到锁转为“unlocked”状态，随即将之设为“locked”状态并返回 True
当 blocking 参数为 False 时，则不会阻塞。但如果 acquire() 失败（锁已经是 locked状态），则会立即返回一个 False，并继续执行线程
当 timeout 参数为一个正的浮点数时，若发生阻塞，则至多阻塞 timeout 秒；若为 –1 （默认值），则表示会一直阻塞下去。
（注：模块内的 TIMEOUT_MAX 常量仅限制设定 timeout 参数时的最大值，并不会限制“无限阻塞”这种状况的执行）另外不允许当 blocking=False 时设置 timeout 参数。
本方法在获取成功时返回 True，失败则返回 False，比如说 timeout 超时
3.2 新增：timeout 参数
3.2 新增：现在 Lock.acquire() 可以被 POSIX 的信号中断
"""

import threading

NUM = 0
lock = threading.Lock()

def job1():
    global NUM
    with lock:
        for i in range(100):
            NUM += 1
            print("Job One: {}".format(NUM))

def job2():
    global NUM
    lock.acquire()
    for i in range(100):
        NUM += 10
        print("Job Two: {}".format(NUM))
    lock.release()

j1 = threading.Thread(target=job1)
j2 = threading.Thread(target=job2)

j1.start()
j2.start()
j1.join()    # join()只决定main thread和子线程的顺序，不决定子线程之间的顺序，所以不加锁的话执行次序会混乱
j2.join()
