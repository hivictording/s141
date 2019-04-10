# Author: Victor Ding

# -*- coding: utf-8 -*-

import pika
import time
import uuid
import random

rabbit = '192.168.2.21'
credentials = pika.PlainCredentials('vding','password')

connection = pika.BlockingConnection(pika.ConnectionParameters(credentials=credentials,host=rabbit,))
channel = connection.channel()

channel.queue_declare(queue='rpc_request',durable=True)

callback_queue = channel.queue_declare('', exclusive=True)
callback_queue_name = callback_queue.method.queue

def on_response(ch,method,props,body):
    global response
    response = body.decode()
    if props.correlation_id == corr_id:
        print("From RPC Server: {}".format(response))

n = 1
msg = 'hello world'

while n<11:
    response = ''
    corr_id = str(uuid.uuid4())

    channel.basic_publish(exchange='',routing_key='rpc_request',body=msg,properties=pika.BasicProperties(delivery_mode=2,correlation_id=corr_id,\
                                                                                                         reply_to=callback_queue_name,))

    channel.basic_consume(queue=callback_queue_name,on_message_callback=on_response,auto_ack=True)

    while not response:
        # 该方法可选填time_limit参数表示最长的阻塞时间. 参数默认为0, 即有消息需要发送或接收时会立即结束阻塞并进行处理.
        # 阻塞期间连接不会被消息代理断开, 该方法起到了保活作用.
        connection.process_data_events()

    # channel.start_consuming()

    n += 1



channel.close()