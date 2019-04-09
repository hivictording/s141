# Author: Victor Ding

# -*- coding: utf-8 -*-

import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("localhost",9100))
print("UDP SERVER BINDING TO PORT 9100")

while True:
    client_data,client_address = server.recvfrom(1024)
    if client_data.decode() == '88':
        print("See you next time!")
        break
    else:
        print("Received: {}".format(client_data.decode()))
        server_response = client_data.decode().upper().encode()
        server.sendto(server_response,client_address)
        print("Sent: {}".format(server_response.decode()))

server.close()

