# Author: Victor Ding

# -*- coding: utf-8 -*-

import socket
import os
import struct

server = socket.socket()
server.bind(('localhost',9000))
server.listen()

while 1:
    connection, address = server.accept()
    print("Client: {} has been connected to the server".format(address))
    while 1:
        try:
            client_cmd = connection.recv(1024)
            decoded_client_cmd = client_cmd.decode()
            if decoded_client_cmd == "quit" or not decoded_client_cmd:
                break
            else:
                cmd_result = os.popen(decoded_client_cmd).read()
                encoded_cmd_result = cmd_result.encode()
                cmd_result_length = len(encoded_cmd_result)

                connection.send(struct.pack('i',cmd_result_length)) # 用struct打包成int类型的4字节固定长度
                connection.send(encoded_cmd_result)
        except ConnectionResetError as e:
            print("Client disconnected due to: {}".format(e))
            break
    connection.close()


