#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sqlalchemy import Column, String,Time,Boolean,Integer
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()

def to_dict(self):
    return {c.name: getattr(self, c.name, None)
            for c in self.__table__.columns}

Base.to_dict = to_dict

class Machine_info(Base):
    db = 'cy_machine'
    # 表名:
    __tablename__ = 'machine_info'

    #主键ID
    Code = Column(String(200), primary_key=True)
    #是否启用
    Is_Use = Column(Integer)
    #设备号
    MachineCode=Column(String(100))
    #SN码(机器序列号)
    MachineSerialer=Column(String(100))
    #创建时间
    #created = Column(Time)




