# -*- coding:utf-8 -*-
'''
author:zhangyu
date:2020/2/26
'''
from io import BytesIO
from typing import List

from sqlalchemy import Column, LargeBinary
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from leetcode.flask_demo.database_config import mysql_parameter

Base = declarative_base()
# 数据库连接池
engine = create_engine(mysql_parameter.get('url'))


def get_session() -> Session:
    '''
        获取session
    Returns:
        session
    '''
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


class AlgorithmParameter(Base):
    __tablename__ = 'algorithm_para'
    algorithm_name = Column(String(255), primary_key=True)
    version = Column(String(40))
    description = Column(String(255))


class AlgorithmFile(Base):
    __tablename__ = 'algorithm_file'
    algorithm_name_version = Column(String(255), primary_key=True)
    # version_description = Column(String(50), primary_key=True)
    algorithm_file = Column(LargeBinary())


def get_algo_parameter(algorithm_name: str) -> str:
    '''
        获取算法的版本
    Args:
        algorithm_name: 算法名字
    Returns:
        返回算法版本
    '''
    session = get_session()
    algo = session.query(AlgorithmParameter).filter_by(algorithm_name=algorithm_name).first()
    return algo


def save_algo_model(version, file):
    '''
        更新模型到数据库
    Args:
        version: 版本
        file: 文件
    '''
    algo = AlgorithmFile(algorithm_name_version=version, algorithm_file=file)
    session = get_session()
    session.add(algo)
    session.commit()
    session.close()


def get_algo_model(algorithm_name_version: str):
    '''
        从数据中读取算法模型
    Args:
        algorithm_name_version: 算法名版本
    Returns:
        算法的模型
    '''
    session = get_session()
    algo = session.query(AlgorithmFile).filter_by(algorithm_name_version=algorithm_name_version).first()
    return algo.algorithm_file


def get_data_by_sql(sql: str):
    '''
       通过sql从数据库中读取数据
    Args:
        sql: sql语句
    Returns:
        从数据库中查询到的数据
    '''
    session = get_session()
    session.execute(sql)
    try:
        proxy = session.execute(sql)
    except Exception as e:
        print(e)
        results = []
    else:
        results = proxy.fetchall()
    return results
