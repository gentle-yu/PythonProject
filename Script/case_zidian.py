#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_zidian.py
@Author: gentle.yu
@Date  : 2020/8/16 17:20
"""

a = ["a", "b", "a", "c", "a", "c", "b", "d", "e", "c", "a", "c"]

# set集合去重
duixiang = set(a)  # 先去重，取出计数对象

# 保存为dict，一一对应
d = {}
for i in duixiang:
    d[i] = a.count(i)

# 对字典按value排序
a = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(a)