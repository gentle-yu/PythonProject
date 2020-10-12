#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_num-count.py
@Author: gentle.yu
@Date  : 2020/8/4 17:26
"""

# 输入一个数字并判断是几位数及每个数字出现的次数

a = str(int(input('请输入一个正整数')))

if a.lstrip('-'):
    lena = len(a) - 1
else:
    lena = len(a)
    print('数字{}是{}位数'.format(a, lena))

for i in a:
    if i == '-':
        continue
    print('数字{}重复{}次'.format(i, a.count(i)))

for i in reversed(a):
    print('数字：{}是{}位数，依次打印分别为：{}'.format(a, lena, i))