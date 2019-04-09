# Author: Victor Ding

# -*- coding: utf-8 -*-

import socket

client = socket.socket()

client.connect(('localhost',7777))

while True:
    text = input("sys>")
    if not text.strip():continue
    client.send(text.encode())

    data = client.recv(2048).decode()
    print("data received: {}".format(data))

client.close()