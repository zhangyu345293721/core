# -*- coding:utf-8 -*-
'''
author:zhangyu
date:2020/1/12
'''


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        '''
            判断栈是否为空
        Returns:
            布尔值
        '''
        return self.stack == []

    def size(self):
        '''
            获取栈的size
        Returns:
            长度
        '''
        return len(self.stack)

    def push(self, element):
        '''
            放入元素
        Args:
            element: 元素
        Returns:
            加元素
        '''
        self.stack.append(element)

    def pop(self):
        '''
            出栈操作
        Returns:
           栈顶元素
        '''
        return self.stack.pop()

    def peek(self):
        '''
            栈顶元素
        Returns:
            栈顶元素
        '''
        return self.stack[-1]


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.peek())
    print(stack.is_empty())
    print(stack.pop())
    print(stack.stack)
