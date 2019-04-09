# Author: Victor Ding

# -*- coding: utf-8 -*-

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
print(connection)

channel = connection.channel()
print(channel)

channel.queue_declare(queue='test1')

def callback(ch,method,properties,body):
    print("Message received: {}".format(body.decode()))

channel.basic_consume(queue='test1',auto_ack=False,on_message_callback=callback)

print("Waiting for messages, press CTRL+C to exit")

channel.start_consuming()
