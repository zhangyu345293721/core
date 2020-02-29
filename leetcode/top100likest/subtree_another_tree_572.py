# -*- coding:utf-8 -*-
'''
判断一棵树是不是另一棵树的子树
author:zhangyu
date:2020/1/14
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_same(t1: TreeNode, t2: TreeNode):
    '''
        判断两棵树是否相等
    Args:
        t1: 树t1
        t2: 树t2
    Returns:
        布尔值
    '''
    if t1 == None and t2 == None:
        return True
    if t1 == None or t2 == None:
        return False
    if t1.val == t2.var:
        return is_same(t1.left, t2.left) and is_same(t1.right, t2.right)
    return False


def is_subtree(s: TreeNode, t: TreeNode):
    '''
        判断一棵树是不是另一颗树的子树
    Args:
        s: 树s
        t: 数t
    Returns:
        布尔值
    '''
    if s == None:
        return False
    if s.val == t.val and is_same(s, t):
        return True
    return is_subtree(s.left, t) or is_subtree(s.right, t)


if __name__ == '__main__':
    pass
