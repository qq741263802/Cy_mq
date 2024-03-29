# -*- coding: utf-8 -*-
import time

import paho.mqtt.client as mqtt

# MQTTHOST = "10.0.0.11"
# MQTTPORT = 6666
MQTTHOST = "94.191.11.107"
MQTTPORT = 32072
mqttClient = mqtt.Client("TTTT123456789996666")


# 连接MQTT服务器
def on_mqtt_connect():
    mqttClient.username_pw_set("cykj168168", "cykj!@#$1234")
    mqttClient.connect(MQTTHOST, MQTTPORT, 60)
    mqttClient.on_connect=on_connect
    mqttClient.loop_forever()


# publish 消息
def on_publish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)



# subscribe 消息
def on_subscribe(topic,qos):
    mqttClient.subscribe(topic, qos)
    mqttClient.on_message = on_message  # 消息到来处理函数



# 消息订阅回调函数
def on_message(lient, userdata, msg):
    print("主题:" + msg.topic + " 消息:" + str(msg.payload))



# 当连接上服务器后回调此函数
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Mqtt连接成功")
    elif rc == 1:
        print("协议版本错误")
    elif rc == 2:
        print("无效的客户端标识")
    elif rc == 3:
        print("服务器无法使用")
    elif rc == 4:
        print("错误的用户名或密码")
    elif rc == 5:
        print("未经授权")



def main():
    on_mqtt_connect()
    on_subscribe("Test1", qos=0)




if __name__ == '__main__':
    main()
