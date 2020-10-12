#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_sort_sorted.py
@Author: gentle.yu
@Date  : 2020/8/17 11:39
"""

# Python排序有两种方法，一种是list对象的sort方法，另一种是builtin函数里面的sorted，主要区别是：
#       ·sort仅针对list对象排序，无返回值，会改变原来队列顺序
#       ·sorted是一个单独函数，可以对迭代对象排序，不局限于list，他不改变原生数据，重新生成一个新的队列

''' sort方法    通过.sort()调用 '''

# 参数说明
#   ·key用列表元素的某个属性或函数进行作为关键字
#   `reverse排序规则  reverse = True降序 或者reverse = False升序   默认升序
#   ·return无返回值

a = [-9, 2, 3, -4, 5, 6, 6, 1]

# 按从小到大排序
a.sort()
print(a)  # 结果：[-9, -4, 1, 2, 3, 5, 6, 6]

# 按从大到小排序
a.sort(reverse=True)
print(a)  # 结果：[6, 6, 5, 3, 2, 1, -4, -9]


''' sorted函数 '''

# 参数说明
#   ·iterable 可迭代对象，如：str、list、tuple、dict都是可迭代对象（这里就不局限于list了）
#   ·key 用列表元素的某个属性或函数进行作为关键字（此函数只能有一个参数）
#   ·reverse 排序规则. reverse = True  降序或者 reverse = False 升序，默认升序
#   ·return 有返回值值，返回新的队列

a = [-9, 2, 3, -4, 5, 6, 6, 1]

# 按从小到大排序
b = sorted(a)
print(a)   # a不会变
print(b)   # b是新的队列 [-9, -4, 1, 2, 3, 5, 6, 6]

# 按从大到小排序
c = sorted(a, reverse=True)
print(c)  # 结果：[6, 6, 5, 3, 2, 1, -4, -9]

