from sqlalchemy import  Column, String, create_engine,Time
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 初始化数据库连接:
def dbconnector(database):
    db = create_engine('mysql+mysqlconnector://cysaas:SA@#321a@mysql-m1.service.consul:3306/'+database)
    return db


#连接数据库
def dbSession(dbkey):
    db=dbconnector(database=dbkey)
    DBSession = sessionmaker(bind=db)
    # 创建session对象:
    session = DBSession()
    return  session












