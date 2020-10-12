#!/usr/bin/env python# -*- encoding: utf-8 -*-
"""
@File    : test_sample.py
@Author  : gentle.yu
@Time    : 2020/7/12 21:13
"""


def func(x):
    return x + 1


def test_naswer():
    assert func(3) == 5
