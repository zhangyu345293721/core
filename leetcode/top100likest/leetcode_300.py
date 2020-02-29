# -*- coding:utf-8 -*-
'''
author:zhangyu
date:2020/2/26
'''

from typing import List
import numpy as np


def longest_increasing_subsequence(nums: List[int]):
    '''
        获取最大递增数组
    Args:
        nums: 数组
    Returns:
        递增数组个数
    '''
    dp = np.zeros(len(nums))
    length = 0
    for num in nums:
        i = binary_search(nums, 0, length, num)
        if i < 0:
            i = -(i + 1)
        dp[i] = num
        if i + 1 > length:
            length = i + 1
    return length


def longest_increasing_subsequence(nums: List[int]):
    '''
        动态规划求递增数组
    Args:
        nums: 数组
    Returns:
        递增数组个数
    '''
    if not nums: return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def binary_search(arr: List[int], l: int, r: int, x: int):
    '''
        二分查找
    Args:
        arr: 输入数组
        l: 开始下标
        r: 结束下标
        x: 要查找的数
    Returns:
        要查找数的下标
    '''
    if r >= l:
        mid = int(l + (r - l) / 2)  # 防止溢出
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1  # 不存在


if __name__ == '__main__':
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    length = longest_increasing_subsequence(arr)
    print(length)
