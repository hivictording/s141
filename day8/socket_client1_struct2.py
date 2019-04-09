# Author: Victor Ding

# -*- coding: utf-8 -*-

import socket
import struct
import json

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

        # server_header_length = client.recv(4)[0]   # 接收header的size
        server_header_length = struct.unpack('i', client.recv(4))[0]

        #接收header,并找到结果的size
        server_data_header_json = client.recv(server_header_length).decode()
        server_data_header_dict = json.loads(server_data_header_json)
        server_data_length = server_data_header_dict['header_length']

        #接收结果
        received_server_data = ""
        received_server_length = 0

        while received_server_length < server_data_length:
            data = client.recv(1024).decode()
            received_server_data += data
            received_server_length += len(data)

        print(received_server_data)

client.close()
exit()