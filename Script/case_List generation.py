#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_List generation.py
@Author: gentle.yu
@Date  : 2020/8/19 14:46
"""
# 列表生成式

c = [1, 3, -3, 4, -2, 8, -7, 6]
d = []
for i in c:
    if i > 0:
        d.append(i)  # 添加到列表d
print("新生成列表d:%s" % d)


a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d", "e"]

# 多个参数列表生成式
e = [str(x)+str(y) for x, y in zip(b, a)]
print("新生成列表e:%s" % e)