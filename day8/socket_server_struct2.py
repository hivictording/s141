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
            client_cmd = connection.recv(1024)
            decoded_client_cmd = client_cmd.decode()
            if decoded_client_cmd == "quit" or not decoded_client_cmd:
                break
            else:
                cmd_result = os.popen(decoded_client_cmd).read()
                encoded_cmd_result = cmd_result.encode()
                cmd_result_length = len(encoded_cmd_result)

                # 生成一个header，内容为包含"结果size"的字典，并计算header的size
                cmd_header_dict = {"author":"Victor Ding","header_length":cmd_result_length}  #生成一个报头，内容为包含"结果size"的字典
                cmd_header_json = json.dumps(cmd_header_dict).encode()
                cmd_header_length = len(cmd_header_json)

                connection.send(struct.pack('i',cmd_header_length))  #发送header的size
                connection.send(cmd_header_json)  #发送header
                connection.send(encoded_cmd_result)  #发送结果
        except ConnectionResetError as e:
            print("Client disconnected due to: {}".format(e))
            break
    connection.close()


