# -*- coding:utf-8 -*-
'''
找出字符串的最长回文串
1）找出里面所有的回文串
2）取出最长哪一个
author:zhangyu
date:2020/1/11
'''


def get_longest_substr(strs):
    '''
        获取字符串中最大的子回文串
    Args:
        strs: 字符串

    Returns:
        最长子字符串

    '''
    sub_str_list = []
    for i in range(len(strs)):
        for j in range(len(strs) + 1):
            sub = strs[i:j]
            flag = check_str(sub)
            if flag:
                sub_str_list.append(sub)
    max_sub = sub_str_list[0]
    for i in range(1, len(sub_str_list)):
        if len(max_sub) < len(sub_str_list[i]):
            max_sub = sub_str_list[i]
    return max_sub


def check_str(sub):
    '''
        判断字符串是不是回文串
    Args:
        sub: 字符串
    Returns:
        反转后字符串
    '''
    sub1 = sub[::-1]
    if sub == sub1:
        return True
    return False

def get_longest_substr2(s):
    '''
        获取字符串中最大的子回文串
    Args:
        s: 字符串
    Returns:
        最长子字符串
    '''
    if len(s) <= 1:
        return s
    s1 = ''
    s2 = ''
    for i in range(len(s) - 1):
        if len(s1) < len(max_str(s, i, i)):
            s1 = max_str(s, i, i)
        if len(s2) < len(max_str(s, i, i + 1)):
            s2 = max_str(s, i, i + 1)
    if len(s1) > len(s2):
        return s1
    else:
        return s2

def max_str(s, i, j):
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i + 1, j]

if __name__ == '__main__':
    strs = 'cbbd'
    max_substr = get_longest_substr2(strs)
    print(max_substr)
