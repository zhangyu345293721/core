# -*- coding:utf-8 -*-
'''
合并数组找中位数
author:zhangyu
date:2020/1/11
'''
from typing import List


def get_median(nums1: List[int], nums2: List[int]) -> float:
    '''
        获取中位数
    Args:
        nums1: 数组1
        nums2: 数组2
    Returns:
        中位数
    '''
    arr = []
    arr.extend(nums1)
    arr.extend(nums2)
    arr.sort()
    length = len(arr)
    if length % 2 == 0:
        return (arr[(length - 1) // 2] + arr[(length - 1) // 2 + 1]) / 2
    else:
        return arr[(length - 1) // 2]


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2, 4]
    num = get_median(nums1, nums2)
    print(num)
