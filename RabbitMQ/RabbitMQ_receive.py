#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

import pika

credentials = pika.PlainCredentials('lihuaming', 'qq13434675015@')
connection = pika.BlockingConnection(pika.ConnectionParameters('10.0.0.16', 5672, 'mqtst', credentials))
channel = connection.channel()


# 声明消息队列，消息将在这个队列中进行传递。如果队列不存在，则创建
# channel.queue_declare(queue='wzg')


# 定义一个回调函数来处理，这边的回调函数就是将信息打印出来。
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# 告诉rabbitmq使用callback来接收信息  # no_ack=True表示在回调函数中不需要发送确认标识
channel.basic_consume(callback,
                      queue='jmeterQueue',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理。按ctrl+c退出。
channel.start_consuming()
