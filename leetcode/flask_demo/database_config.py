# -*- coding:utf-8 -*-
'''
author:zhangyu
date:2020/2/24
'''
mysql_info = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'db1': 'wms',
    'db2': 'house',
    'port': 3306,
    'charset': 'utf8'
}

mysql_parameter = {
    'url': 'mysql+pymysql://' + mysql_info.get('user') + ':' + mysql_info.get('password') + '@' + mysql_info.get(
        'host') + '/' + mysql_info.get('db2')
}
