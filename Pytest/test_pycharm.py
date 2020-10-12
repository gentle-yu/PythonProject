#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : test_pycharm.py
@Author  : gentle.yu
@Time    : 2020/7/12 22:52
"""

import pytest


class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x in 'hello'
        assert hasattr(x, 'check')

    def test_three(self):
        a = 'hello'
        b = 'hello word'
        assert a in b


if __name__ == '__main__':
    pytest.main(['-q test_pycharm.py'])
