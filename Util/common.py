# -*- coding: utf-8 -*-
import uuid,time,datetime

host='http://ams-api.saas.shj188.com'


def getguid():
    guid=uuid.uuid1()
    return str(guid)


def getnowtime():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return now_time


def assertEqual(arg1,arg2,msg):
    if(msg[arg1]!=arg2):
        print('接口请求异常：'+str(msg))




