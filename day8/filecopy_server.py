# Author: Victor Ding

# -*- coding: utf-8 -*-

import socket
import os
import struct
import json

server = socket.socket()
server.bind(('localhost',9000))
server.listen()

while 1:
    connection, address = server.accept()
    print("Client: {} has been connected to the server".format(address))
    while 1:
        try:
            received = connection.recv(1024)
            decoded_received = received.decode()
            if decoded_received == "quit" or not decoded_received:
                break
            else:
                file_name = decoded_received + ".rar"
                file_length = os.stat(file_name).st_size

                # 生成一个header，内容为包含"结果size"的字典，并计算header的size
                cmd_header_dict = {"author":"Victor Ding","header_length":file_length}  #生成一个报头，内容为包含"结果size"的字典
                cmd_header_json = json.dumps(cmd_header_dict).encode()
                cmd_header_length = len(cmd_header_json)

                connection.send(struct.pack('i',cmd_header_length))  #发送header的size
                connection.send(cmd_header_json)  #发送header

                with open(file_name,"rb",) as fh:
                    while 1:
                        file_content = fh.read(1024)
                        if file_content:
                            connection.send(file_content)  #发送结果
                        else:
                            print("File transfer over")
                            break
        except ConnectionResetError as e:
            print("Client disconnected due to: {}".format(e))
            break
    connection.close()


