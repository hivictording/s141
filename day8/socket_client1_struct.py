# Author: Victor Ding

# -*- coding: utf-8 -*-

import socket
import struct

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
        len_server_data =  struct.unpack('i',client.recv(4))[0] #先读包长度，SERVER端固定为4字节，解包后是一个元组的形式，第一个元素就是真实数据的字节

        print(len_server_data)

        received_server_data = client.recv(len_server_data).decode()

        # received_server_data = ""
        # received_server_length = 0
        #
        # while received_server_length < len_server_data:
        #     data = client.recv(1024).decode()
        #     received_server_data += data
        #     received_server_length += len(data)

        print(received_server_data)

client.close()
exit()