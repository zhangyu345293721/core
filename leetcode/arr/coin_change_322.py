# -*- coding:utf-8 -*-
'''
硬币兑换问题
author:zhangyu
date:2020/1/20
'''
import sys
from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    '''
        硬币兑换
    Args:
        coins:货币数组
        amount:数量
    Returns:
        数量
    '''
    if amount == 0:
        return 0
    if coins == None or len(coins) == 0:
        return -1
    dp = [0] * (amount + 1)
    for i in range(1, amount + 1):
        res = sys.maxsize
        for j in range(len(coins)):
            if coins[j] > i:
                continue
            if (dp[i - coins[j]] == -1):
                continue
            dp[i] = 1 + dp[i - coins[j]];
            res = min(res, dp[i])
        dp[i] = res
    return dp[amount]


if __name__ == '__main__':
    arr = [1, 2, 5]
    amount = 11
    sum = coin_change(arr, amount)
    print(sum)
