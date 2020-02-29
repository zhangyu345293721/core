# -*- coding:utf-8 -*-
'''
author:zhangyu
date:2020/2/21
'''

# 测试抽象类
from abc import abstractmethod, ABCMeta


class interface:
    __metaclass__ = ABCMeta
    @abstractmethod
    def lee(self):
        pass

    def marlon(self):
        pass


class relalize_interface_lee(interface):
    def __init__(self):
        print('这个是接口')

    def lee(self):
        print('实现方法')

    def marlon(self):
        pass


entity = relalize_interface_lee()
entity.lee()
