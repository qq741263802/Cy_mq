# -*- coding: utf-8 -*-
import requests,time,json,uuid,datetime,re,django
from SQLdb import DbContext,Message,Info,Huodao
from influxdb import InfluxDBClient
from aip import AipOcr


#数据删除
# mesage = Message.test_message
# db= DbContext.DbSession(mesage.db)
# age=db.query(mesage)
# for k in age:
#     print(k.id)
# for i in age:
#      managerList = db.query(mesage).filter(mesage.id == i.id).update({"message": "99999"})
# db.commit()
# db.close()

#
# json_body = [
#     {
#         "measurement": "message",
#         "tags": {
#             "stuid": "s123"
#         },
#         "fields": {
#             "score": 89
#         }
#     }
# ]
#
# #连接influxdb
# client=InfluxDBClient(
#     host='localhost',
#     port=8086,
#     username='root',
#     password='',
#     database='TestDb'
#     )
# client.write_points(json_body)
# print(client.get_list_database())





#hd = Huodao.machine_huodao
#db = DbContext.DbSession(hd.db).query(hd).filter(hd.MachineId =='d29c51961fc4479d895fb776bea7243f')




APP_ID = '16736859'
API_KEY = 'fPKH4z5HfbqOK5HBc5TEQdyi'
SECRET_KEY = 'O0KP7bD6t49gCrgQlsrEupzgYTGss9MR'

#client = AipOcr(APP_ID, API_KEY, SECRET_KEY)






