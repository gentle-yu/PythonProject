#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_BMI.py
@Author: gentle.yu
@Date  : 2020/8/4 17:23
"""

# 根据BMI公式（体重除以身高的平方）计算BMI指数,并根据BMI指数分析身体健康状况
'''
        低于18.5：过轻
        18.5-25：正常
        25-28：过重
        28-32：肥胖
        高于32：严重肥胖
'''

height = input("height/m:请输入您的身高")
weight = input("weight/kg:请输入您的体重")

h = float(height)/100
w = float(weight)

bim = w/(h*h)
print(bim)

if bim < 18.5:
    print("过轻")
elif 18.5 <= bim < 25:
    print("正常")
elif 25 <= bim < 28:
    print("过重")
elif 28 <= bim < 32:
    print("肥胖")
else:
    print("严重肥胖")
