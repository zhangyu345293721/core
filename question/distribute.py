# -*- coding:utf-8 -*-
'''
拆分数字
author:zhangyu
date:2020/1/7
'''
from random import randint

'''if __name__ == '__main__':
    quantity = 100  # 这两个值任意更改，也可以用sys.argv来设置
    n = 5

    lst = []
    j = quantity
    k = quantity
    for i in range(n - 1):  # 随机生成前面n-1个数
        while j > (k - (n - i)):  # 防止随机数太大，让后面的数不够分
            j = randint(1, k)
        lst.append(j)
        k -= j
        j = k

    lst.append(quantity - sum(lst))  # 最后一个数字，用减法

    print(lst, sum(lst))'''

import random

def divided_sku_quantity(quantity, n):
    '''
        将数字分成固定的分数
    Args:
        quantity: 要分割的数量
        n: 切割分数
    Returns:
        分成份数数组
    '''
    if quantity < n:
        return divided_sku_quantity(quantity, quantity)
    divided = []
    stick = [0] + random.sample(range(1, quantity), n - 1) + [quantity]
    stick.sort()
    for i in range((len(stick) - 1)):
        divided.append((stick[i + 1] - stick[i]))
    return divided



quantity = 2
n = 5
divide = divided_sku_quantity(quantity, n)
print(divide)