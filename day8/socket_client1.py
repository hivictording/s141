# Author: Victor Ding

# -*- coding: utf-8 -*-

import socket

client = socket.socket()
client.connect(('localhost',9000))

while 1:
    cmd = input("Please input your command>>>").strip()
    if not cmd:
        continue
    elif cmd == 'quit':
        client.send(cmd.encode())
        break
    else:
        client.send(cmd.encode())
        len_server_data = int(client.recv(1024).decode())
        print(len_server_data)

        # received_server_data = ""
        # received_server_length = 0
        #
        # while received_server_length < len_server_data:
        #     data = client.recv(1024).decode()
        #     received_server_data += data
        #     received_server_length += len(data)

        received_server_data = client.recv(len_server_data).decode()

        print(len(received_server_data))
        print(received_server_data)

client.close()
exit()