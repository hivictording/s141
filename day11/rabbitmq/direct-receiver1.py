# Author: Victor Ding

# -*- coding: utf-8 -*-

"""
fanout是即时性的，如果发出来的时候consumer这边还没准备好，那消息就丢失了
"""

import pika
import random
import time
import sys

rabbitmq = '192.168.2.21'
credentials = pika.PlainCredentials('vding','password')

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq,credentials=credentials,))
channel = connection.channel()

channel.exchange_declare(exchange_type='direct',exchange='direct_logs')

queue = channel.queue_declare(queue='',exclusive=True,durable=True)
# queue = channel.queue_declare(queue='broadcast',durable=True)
queue_name = queue.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs',queue=queue_name,routing_key=severity)

def callback(ch,method,properties,body):
    # i = random.randint(1,8)
    print("Message received: {}".format(body.decode()))
    # time.sleep(i)
    time.sleep(10)
    ch.basic_ack(delivery_tag=method.delivery_tag)  #这句话不能省略,和下面的auto_ack搭配使用

channel.basic_qos(prefetch_count=1)  #非常重要，consumer只有等处理完了下一个任务才能继续拿一个任务，否则先启动的consumer会把所有当前的任务拿完

# channel.basic_consume(queue='test1',auto_ack=False,on_message_callback=callback)
channel.basic_consume(queue_name,on_message_callback=callback)  #auto_ack缺省为True

print("Waiting for messages, press CTRL+C to exit")

channel.start_consuming()