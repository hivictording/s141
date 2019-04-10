# Author: Victor Ding

# -*- coding: utf-8 -*-

import pika
import time

rabbit = '192.168.2.21'
credentials = pika.PlainCredentials('vding','password')

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit,credentials=credentials,))
channel = connection.channel()

def callback(ch,method,props,body):
    print("RPC SERVER received message: {}".format(body))
    time.sleep(1)
    ch.basic_publish(exchange='',routing_key=props.reply_to,properties=pika.BasicProperties(correlation_id=props.correlation_id,),\
                        body=body.upper())
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.queue_declare(queue='rpc_request',durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_request',on_message_callback=callback)
print("Awaiting RPC calls.....")

channel.start_consuming()