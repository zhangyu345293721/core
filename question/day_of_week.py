# -*- coding:utf-8 -*-
'''
LeetCode:1185题目：找出一天是星期几
author:zhangyu
date:2020/1/8
'''
from datetime import datetime


def dayOfTheWeek(day: int, month: int, year: int) -> str:
    '''
        输入年月日，计算它的星期
    Args:
        day:天
        month:月
        year:年
    Returns:
        返回星期
    '''
    return datetime(year, month, day).date().strftime('%A')


dayOfTheWeek(31, 8, 2019)
