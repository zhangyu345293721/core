# -*- coding:utf-8 -*-
'''
author:zhangyu
date:2020/2/20
'''

# -*- coding:utf-8 -*-
'''
字符串操作
author:zhangyu
date:2020/2/20
'''
from typing import List


def bracket_trace(result, s: str, left: int, right: int, n: int):
    if (len(s) == 2 * n):
        result.append(s)
    if left < n:
        bracket_trace(result, s + '(', left + 1, right, n)
    if right < left:
        bracket_trace(result, s + ')', left, right + 1, n);


def generate_parentheses(n: int) -> List[str]:
    result = []
    if n < 1:
        return result
    bracket_trace(result, '', 0, 0, n)
    return result


if __name__ == '__main__':
    '''n = 3
    result = generate_parentheses(n)
    print(result)'''
    print('SKU_GROUP_ALGO_default'.lower())
