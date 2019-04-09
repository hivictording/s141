# Author: Victor Ding

# -*- coding: utf-8 -*-

class testException(Exception):
    def __init__(self,msg1,msg2):
        self.msg1 = msg1
        self.msg2 = msg2

try:
    raise testException(1,2)  #触发异常
except testException as e: #抓住异常
    print(e)
