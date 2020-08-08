# Author: Victor Ding

# -*- coding: utf-8 -*-

import time

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
print(connection)

channel = connection.channel()
print(channel)

channel.queue_declare(queue='test1',durable=True)

def callback(ch,method,properties,body):
    # i = random.randint(1,8)
    print("Message received: {}".format(body.decode()))
    # time.sleep(i)
    time.sleep(3)
    # ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='test1',auto_ack=False,on_message_callback=callback)
# channel.basic_consume(queue='test1',on_message_callback=callback)

print("Waiting for messages, press CTRL+C to exit")

channel.start_consuming()
