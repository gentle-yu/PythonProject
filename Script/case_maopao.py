#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_maopao.py
@Author: gentle.yu
@Date  : 2020/8/4 16:39
"""

# 冒泡排序
li = [1, 2, 10, 9, 21, 35, 4, 6]
s = range(len(li))[::-1]
print(s)

for i in s:
    for j in range(i):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]
print(li)