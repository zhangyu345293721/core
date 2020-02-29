# -*- coding:utf-8 -*-
'''
author:zhangyu
date:2020/1/17
'''


class People:
    country = 'China'

    # 初始化参数
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def secret(self):
        print('%s的年龄是%d' % (self.name, self.__age))

    @classmethod
    def get_country(self):
        return self.country


'''mi = People('小爱同学')
mi.country="japan"
print(mi.country)
mi._People__secret()
# print(mi.__age)
print(mi._People__age)'''

mi = People('小爱同学')
print(mi.get_country())
print(People.get_country())
