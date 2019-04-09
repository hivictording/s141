# Author: Victor Ding

# -*- coding: utf-8 -*-

import socket
import struct
import json

client = socket.socket()
client.connect(('localhost',9000))

res = client.recv(1024).decode()
print(res)

while 1:
    cmd = input("Please input your command>>>").strip()
    if not cmd:
        continue
    elif cmd == 'quit':
        client.send(cmd.encode())
        break
    else:
        cmd_method = cmd.split()[0]
        file_name = cmd.split()[1]
        new_file_name = file_name.split(".")[0] + ".new." + file_name.split(".")[1]
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

        with open(new_file_name, "wb") as fh:
            while received_server_length < server_data_length:
                size = server_data_length - received_server_length
                # print(received_server_length)
                # print(size)
                if size >= 1024: size = 1024
                data = client.recv(size)
                received_server_length += size
                fh.write(data)

client.close()
exit()