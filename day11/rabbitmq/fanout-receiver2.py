import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange_type='fanout',exchange='logs')

# queue = channel.queue_declare(queue='broadcast',durable=True)
queue = channel.queue_declare(queue='',durable=True)
queue_name = queue.method.queue

channel.queue_bind(exchange='logs',queue=queue_name)

def callback(ch,method,properties,body):
    # i = random.randint(1,8)
    print("Message received: {}".format(body.decode()))
    # time.sleep(i)
    time.sleep(8)
    ch.basic_ack(delivery_tag=method.delivery_tag)  #这句话不能省略

channel.basic_qos(prefetch_count=1)  #非常重要，consumer只有等处理完了下一个任务才能继续拿一个任务，否则先启动的consumer会把所有当前的任务拿完

# channel.basic_consume(queue='test1',auto_ack=False,on_message_callback=callback)
channel.basic_consume(queue_name,on_message_callback=callback)  #auto_ack缺省为True

print("Waiting for messages, press CTRL+C to exit")

channel.start_consuming()