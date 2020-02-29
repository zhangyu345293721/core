# -*- coding:utf-8 -*-
'''
author:zhangyu
date:2020/2/26
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
sql = '''create table person(
    id int not null primary key,
    name varchar(50),
    age int,
    address varchar(100));
'''

engine = create_engine('mysql+pymysql://root:root@localhost/house')
conn = engine.connect()
conn.execute(sql)
engine.connect() #表示获取到数据库连接。类似我们在MySQLdb中游标course的作用。"""

"""
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('mysql+pymysql://root:root@localhost/house')
metadata = MetaData(engine)


student = Table('person2', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(50), ),
            Column('age', Integer),
            Column('address', String(10)),
)

metadata.create_all(engine)"""

"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://root:root@localhost/house')
DBsession = sessionmaker(bind=engine)
session = DBsession()

Base = declarative_base()

class person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    address = Column(String(100))

student1 = person(id=1001, name='ling', age=25, address="beijing")
student2 = person(id=1002, name='molin', age=18, address="jiangxi")
student3 = person(id=1003, name='karl', age=16, address="suzhou")

session.add_all([student1, student2, student3])
session.commit()
session.close()"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)
    address = Column(String(100))
    picture=Column()


engine = create_engine('mysql+pymysql://root:root@localhost/house')
DBSession = sessionmaker(bind=engine)
session = DBSession()

my_stdent = session.query(Student).filter_by(name="karl").first()
print(my_stdent)
