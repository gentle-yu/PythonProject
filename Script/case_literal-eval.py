#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_literal-eval.py
@Author: gentle.yu
@Date  : 2020/8/19 15:22
"""

# 1、eval函数实现的功能
#       ·将字符串string对象转化为有效的表达式参
#       ·求值运算返回计算结果
# 2、语法：eval（expression，globals=None, locals=None）返回的是计算结果
#       ·expression是一个参与计算的Python表达式
#       ·globals是可选参数，如果设置属性不为None的话，就必须是dictionary对象了
#       ·locals也是可选对象，如果设置属性不为None的话，可以是任何map对象了


a = "hello"
b = "world"
# 把字符串里面内容，当成运算
c = eval("a+b")
print(c)  # 返回结果 helloworld

d = eval("2+3+7*2")
print(d)  # 返回结果 19

# str转list

a = '[1, "a", None, True, [1, 2]]'
print(eval(a))
print(type(eval(a)))

# str转tuplue
b = '(1, "a", None, True, [1, 2])'
print(eval(b))
print(type(eval(b)))

# str转dict
c = '{"a": 1, "b": True, "c": None, "d": [1, 2], "e": {"a": 1}}'
print(eval(c))
print(type(eval(c)))

import ast

f = '''{"isSucess":true, "result": '[{"name":"yoyo", "status": "200"}]'}'''
f1 = f.replace("true", "True").replace("false", "False").replace("null", "None")
print(ast.literal_eval(f1))
print(eval(f1))
