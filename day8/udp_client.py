# Author: Victor Ding

# -*- coding: utf-8 -*-

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

alist = ['hello world',"here you go","thanks buddy","88"]

for a in alist:
    client.sendto(a.encode(),("localhost",9100))
    print("Sent: {}".format(a))
    server_data = client.recv(1024).decode()
    print("Received: {}".format(server_data))

client.close()
