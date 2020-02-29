# -*- coding:utf-8 -*-
'''
在一个链表中随机选择一些元素
author:zhangyu
date:2020/1/7
'''

import random

foo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_list = random.sample(foo, 5)
print(random_list)
