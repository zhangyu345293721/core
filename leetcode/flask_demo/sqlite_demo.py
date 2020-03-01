# -*- coding:utf-8 -*-
'''
测试python内置的sqlite
author:zhangyu
date:2020/3/1
'''
import sqlite3


def get_cur() -> sqlite3.Cursor:
    '''
        # 硬盘上创建连接
    Returns:
       游标
    '''
    con = sqlite3.connect('d:/first.db')
    cur = con.cursor()
    return cur, con


def create_table():
    '''
        创建数据库表
    '''
    sql = 'create table t_person(pno INTEGER PRIMARY KEY  AUTOINCREMENT ,pname varchar(30) NOT NULL ,age INTEGER)'
    cur, con = get_cur()
    try:
        cur.execute(sql)
    except Exception as e:
        print(e)
        print('创建表失败')
    finally:
        cur.close()
        con.close()


def insert_data():
    '''
       插入数据库中所有数据
    '''
    sql = 'insert into t_person(pname,age) values(?,?)'
    cur, con = get_cur()
    try:
        cur.execute(sql, ('张三', 23))
        con.commit()
        print('插入成功')
    except Exception as e:
        print(e)
        print('插入失败')
        con.rollback()
    finally:
        cur.close()
        con.close()


def search_database():
    '''
       查询数据库
    '''
    sql = 'select * from t_person'
    cur, con = get_cur()
    try:
        cur.execute(sql)
        # 获取所有数据
        person_all = cur.fetchall()
        # print(person_all)
        # 遍历
        for p in person_all:
            print(p)
    except Exception as e:
        print(e)
        print('查询失败')
    finally:
        cur.close()
        con.close()


if __name__ == '__main__':
    search_database()
