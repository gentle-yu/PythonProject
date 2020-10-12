#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : test_assert.py
@Author: gentle.yu
@Date  : 2020/7/16 11:05
@Desc  : 
'''


def f():
    return 5


def test_answer():

    a = f()
    assert a % 2 == 0,"判断a为偶数，当前a的值为：%s"%a #添加异常信息