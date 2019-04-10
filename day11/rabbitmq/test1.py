# Author: Victor Ding

# -*- coding: utf-8 -*-

import random

import pika

rabbitmq = '192.168.2.21'
credentials = pika.PlainCredentials('vding','password')

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq,credentials=credentials,))
print(connection)

channel = connection.channel()
print(channel)

channel.queue_declare(queue='test1',durable=True)

for x in range(20):
    i = random.randint(1,100)
    msg = 'Hello World ' + str(i)
    channel.basic_publish(exchange='',routing_key='test1',body=msg,properties=pika.BasicProperties(delivery_mode=2,))  #delivery_mode为2表示消息持久化
    print("Message Sent: {}".format(msg))

connection.close()
