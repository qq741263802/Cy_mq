# !/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
import pika

credentials = pika.PlainCredentials('lihuaming', 'qq13434675015@')
connection = pika.BlockingConnection(pika.ConnectionParameters('10.0.0.16', 5672, 'mqtst', credentials))
# 创建频道
channel = connection.channel()
# 声明消息队列
channel.queue_declare(queue='order')

# exchange -- 它使我们能够确切地指定消息应该到哪个队列去。向队列插入数值 routing_key是队列名 body是要插入的内容
n = 1
counter = 1
while (1 == 1):
    channel.basic_publish(exchange='',
                          routing_key='order',
                          body='order741263888999123')
    counter += 1
print("开始队列")

connection.close()
