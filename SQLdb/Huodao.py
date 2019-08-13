#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sqlalchemy import Column, String,DateTime,Integer
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()

def to_dict(self):
    return {c.name: getattr(self, c.name, None)
            for c in self.__table__.columns}

Base.to_dict = to_dict

class Machine_Huodao(Base):
    db = 'cy_machine'
    # 表名:
    __tablename__ = 'machine_huodao'

    #主键ID
    Code = Column(String(200), primary_key=True)
    #设备ID
    MachineId=Column(String(200))
    #货道号
    HuodaoID=Column(String(200))
    #货道编号
    SerialPort = Column(String(200))
    #排序
    Sort=Integer()
    #创建时间
    Created = Column(DateTime)





