# Author: Victor Ding

# -*- coding: utf-8 -*-

import selectors
import socket
#selectors模块默认会用epoll，如果你的系统中没有epoll(比如windows)则会自动使用select
sel = selectors.DefaultSelector()   #生成一个select对象

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False) #设定非阻塞
    sel.register(conn, selectors.EVENT_READ, read)  #新连接注册read回调函数

def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('localhost', 8080))
sock.listen()
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)    #把刚生成的sock连接对象注册到select连接列表中，并交给accept函数处理

