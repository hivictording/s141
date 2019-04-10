# Author: Victor Ding

# -*- coding: utf-8 -*-

import pika
import random

rabbitmq = '192.168.2.21'
credentials = pika.PlainCredentials('vding','password')

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq,credentials=credentials,))
channel = connection.channel()

channel.exchange_declare(exchange_type='fanout',exchange='logs')

for i in range(50):
    number = random.randint(1,100)
    msg = "Hello World " + str(number)
    channel.basic_publish(exchange='logs',routing_key='',body=msg,properties=pika.BasicProperties(delivery_mode=2,))  #delivery_mode为2表示消息持久化
    print("Message sent: {}".format(msg))

channel.close()