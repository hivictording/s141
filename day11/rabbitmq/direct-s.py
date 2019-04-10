# Author: Victor Ding

# -*- coding: utf-8 -*-

import pika
import random
import sys

rabbitmq = '192.168.2.21'
credentials = pika.PlainCredentials('vding','password')

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq,credentials=credentials,))
channel = connection.channel()

channel.exchange_declare(exchange_type='direct',exchange='direct_logs')

severity = sys.argv[1] if len(sys.argv) > 1 else "info"
msg = '.'.join(sys.argv[2:]) or "hello world"


channel.basic_publish(exchange='direct_logs',routing_key=severity,body=msg)  #delivery_mode为2表示消息持久化
print("Message sent: {}".format(msg))

channel.close()