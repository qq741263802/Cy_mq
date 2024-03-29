# -*- coding: utf-8 -*-
import time,threading
import paho.mqtt.client as mqtt
from SQLdb import Info,DbContext
# MQTTHOST = "10.0.0.11"
# MQTTPORT = 1883
MQTTHOST = "94.191.11.107"
MQTTPORT = 32072
t = time.time()
clid = str(round(t * 1000))
mqttClient = mqtt.Client("cy895124233")


lock = threading.Lock()

# 连接MQTT服务器
def on_mqtt_connect(sn):
    mqttClient.username_pw_set("cykj168168", "cykj!@#$1234")
    mqttClient.connect(MQTTHOST, MQTTPORT, 60)
    mqttClient.on_connect = on_connect
    on_publish("Test1", sn, qos=0)
    mqttClient.loop_forever()


# publish 消息
def on_publish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)



# subscribe 消息
def on_subscribe(topic, qos):
    mqttClient.subscribe(topic, qos)
    mqttClient.on_message = on_message


# 消息订阅回调函数
def on_message(lient, userdata, msg):
    print(msg.topic + " " + ":" + str(msg.payload))



def mqtt_thread(sn_number,machinetype):
    info = Info.Machine_Info
    db = DbContext.dbSession(info.db).query(info).filter(
        info.MachineType == machinetype and info.MachineCode != 'M30944').order_by(info.Created.desc()).limit(sn_number)
    for i in db:
        lock.acquire()
        try:
            th=threading.Thread(target=on_mqtt_connect, args=(i.MachineSerialer,))
            th.start()
        finally:
            lock.release()


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
    mqtt_thread(1,1)



if __name__ == '__main__':
    main()
