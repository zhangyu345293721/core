# -*- coding:utf-8 -*-
'''
author:zhangyu
date:2020/1/6
'''

arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
arr2 = [7, 8]

# subtract = []

'''for num in arr1:
    if num not in arr2:
        subtract.append(num)
print(subtract)'''


def sku_2_shelf(arr, distribute_shelf):
    '''
        list分配到货架
    Args:
        arr: 要分配的商品
        distribute_shelf: 分配到货架的数量
    Returns:
        分配的list
    '''

    division = len(arr) / float(distribute_shelf)
    return [arr[int(round(division * i)): int(round(division * (i + 1)))] for i in range(distribute_shelf)]


list_part = sku_2_shelf(arr1, 3)
print(list_part)
