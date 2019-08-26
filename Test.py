# -*- coding: utf-8 -*-
import requests,time,json,uuid,datetime,re,django,threading,os,random,socket
from SQLdb import DbContext,Message,Info,Huodao
from influxdb import InfluxDBClient
from aip import AipOcr
from multiprocessing import Process,Pool
from Tcp import TcpTest


# 全局配置
# APP_ID = '16736859'
# API_KEY = 'fPKH4z5HfbqOK5HBc5TEQdyi'
# SECRET_KEY = 'O0KP7bD6t49gCrgQlsrEupzgYTGss9MR'

#
# info = Info.Machine_Info
# db = DbContext.dbSession(info.db).query(info).filter(info.MachineType == 1 and info.MachineCode!='M30944').order_by(info.Created.desc()).limit(1300)
# print(db.count())

#
# def tcptest(sn):
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect(('94.191.97.65', 30670))
#     s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
#     while True:
#         s.send(bytes(sn + '|01|01|02|00|F0|55', encoding='utf-8'))
#         print('发送消息'+sn+'|01|01|02|00|F0|55')
#         time.sleep(30)


#TcpTest.tcp_thread(200,2)
TcpTest.tcp_thread(1100,1)