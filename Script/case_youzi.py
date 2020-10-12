#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_youzi.py
@Author: gentle.yu
@Date  : 2020/8/4 16:04
"""

# *****假设你有无线数量的邮票，面值分别为6角、7角、8角，请问最大的不可支付邮资是多少元？*****

a = 6
b = 7
c = 8
t = 50  # 票的张数
s = []  # 排列组合

# 生成的组合
for i in range(t + 1):
    s1 = a * i
    s.append(s1)
    for j in range(t + 1):
        s2 = a * i + b * j
        s.append(s2)
        for k in range(t + 1):
            s3 = a * i + b * j + c * k
            s.append(s3)

# 排序
s.sort()
# 去重
news = []
for i in s:
    if i not in news:
        news.append(i)
print("组合生成的最大数%s" % news[-1])

# 提取不再列表中的数字
r = []
for i in range(6 * t):
    if i in news:
        pass
    else:
        r.append(i)

print("组合不能生成的数字%s" % r)
print("不能生成的最大数字为%s" % r[-1])