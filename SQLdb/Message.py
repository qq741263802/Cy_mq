#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sqlalchemy import Column, String,Time,Boolean,Integer,DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()
# 定义User对象:
class Test_message(Base):
    db='test'
    # 表名:
    __tablename__ = 'test_message'

    #主键ID
    id = Column(String(100), primary_key=True)
    #异常消息内容
    message = Column(String(2000))
    #创建时间
    created = Column(DateTime)




