# Author: Victor Ding

# -*- coding: utf-8 -*-

import socket
import os

server = socket.socket()

server.bind(('localhost',7777))
server.listen(2)
print('I am listening')

while True:
    conn, addr = server.accept()
    print(conn)
    while True:
        try:
            data = conn.recv(2048)
            if data.strip():
                decoded_data = data.decode()
                print('data received: {}'.format(decoded_data))
                res = os.popen(data.decode()).read().encode()
                conn.send(res)
        except ConnectionResetError as e:
            print("Client disconnected")
            break
    conn.close()

server.close()