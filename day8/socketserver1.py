# Author: Victor Ding

# -*- coding: utf-8 -*-

import socketserver
import os
import json
import struct


class server_handler(socketserver.BaseRequestHandler):
    def handle(self):
        # print(self.server)
        # print(self.client_address)
        # print(self.request)
        # print(self.request.laddr)

        print("Client ip address{} port {} has been connected to the server".format(self.client_address[0],self.client_address[1]))
        self.request.send("Hello, Welcome: IP Address: {}, Port: {}".format(self.client_address[0],self.client_address[1]).encode())
        while 1:
            try:
                received = self.request.recv(1024)
                decoded_received = received.decode()
                if decoded_received == "quit" or not decoded_received:
                    break
                else:
                    cmd_method = decoded_received.split()[0]
                    if cmd_method == 'get':
                        file_name = decoded_received.split()[1]
                        file_length = os.stat(file_name).st_size

                        # 生成一个header，内容为包含"结果size"的字典，并计算header的size
                        cmd_header_dict = {"author": "Victor Ding", "header_length": file_length}  # 生成一个报头，内容为包含"结果size"的字典
                        cmd_header_json = json.dumps(cmd_header_dict).encode()
                        cmd_header_length = len(cmd_header_json)

                        self.request.send(struct.pack('i', cmd_header_length))  # 发送header的size
                        self.request.send(cmd_header_json)  # 发送header

                        with open(file_name, "rb", ) as fh:
                            while 1:
                                file_content = fh.read(1024)
                                if file_content:
                                    self.request.send(file_content)  # 发送结果
                                else:
                                    print("File transfer over")
                                    break
            except ConnectionResetError as e:
                print("Client disconnected due to: {}".format(e))
                break


server = socketserver.ThreadingTCPServer(("localhost",9000),server_handler)
server.serve_forever()
