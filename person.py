# -*- coding:utf-8 -*-
'''
author:zhangyu
date:2020/1/14
'''
from typing import List, Set


class Person:
    def __init__(self, id, name="丁满", age=10):
        '''
        Args:
            id: 学号
            name: 名字
            age: 年龄
        '''
        self.id = id
        self.name = name
        self.age = age


def generate_students(num) -> List[Person]:
    '''
        生成学生
    Args:
        num: 数量
    Returns:
        学生链表
    '''
    students = []
    for i in range(1, num + 1):
        students.append(i)
    return students


if __name__ == '__main__':
    student_list = generate_students(5)
    print(student_list)
