#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql,sqlalchemy

dbhost='mysql-m1.service.consul'
dbuser='cysaas'
dbpass='SA@#321a'
dbdatabase='cy_notify'
Machineserialer_sql="select machineserialer from cy_machine.machine_info i limit 1000"

def get_machineserialer():
    try:
        list = []
        db = pymysql.connect(dbhost, dbuser, dbpass, dbdatabase)
        cursor = db.cursor()
        cursor.execute(Machineserialer_sql)
        results = cursor.fetchall()
        for row in results:
            list += row
        db.close()
        return list
    except:
        print("查询数据异常")





def dal_insert(sql):
    try:
        db = pymysql.connect(dbhost, dbuser, dbpass, dbdatabase)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()
    except:
        print(exec())





