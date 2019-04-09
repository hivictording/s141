# Author: Victor Ding

# -*- coding: utf-8 -*-

"""总结：1. non-daemon, no join(): 主线程会先执行完毕然后被阻塞，不退出，等待子线程执行完毕再退出.
        2. non-daemon with join(): 主线程等待子线程执行完毕，再执行主线程其余部分，执行完退出
        3. daemon, no join(): 主线程执行完毕直接退出，并且子线程也会跟着退出
        4. daemon with join(): 主线程等待子线程执行完毕，再执行主线程其余部分，执行完退出，和第2种的区别在于timeout以后的处理不一样，看第5条
        5. 在none daemon的线程中主线程永远会等待子线程退出后才退出，在daemon的线程中主线程不会等待子线程退出后自己才退出，两种
           线程中的join(timeout=3)或者join()只不过给子线程一个先执行(主线程等待)的机会, 如果子线程执行完毕则退出，
           如果non-daemon的子线程超时则主线程继续等待，如果daemon的子线程超时则主线程直接退出。
    what is Deamon thread?
    Some threads do background tasks, like sending keepalive packets, or performing periodic garbage collection, or whatever.
    These are only useful when the main program is running, and it's okay to kill them off once the other, non-daemon, threads have exited.
    Without daemon threads, you'd have to keep track of them, and tell them to exit, before your program can completely quit.
    By setting them as daemon threads, you can let them run and forget about them, and when your program quits, any daemon threads are killed automatically.
"""


import threading
import time
import random

def student():
    num = random.randint(1,10)
    print("{} start time:{}".format(threading.current_thread().getName(),num))
    time.sleep(num)
    print("{} finished studying:{}".format(threading.current_thread().getName(),num))

main_thread = threading.main_thread()

for i in range(5):
    threading.Thread(target=student,name="student"+str(i),daemon=True).start()

print(threading.enumerate())  #枚举当前所有线程

for i in threading.enumerate():
    if i == main_thread: continue
    i.join()


