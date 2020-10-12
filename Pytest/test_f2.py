#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : test_f2.py
@Author: gentle.yu
@Date  : 2020/7/13 20:38
@Desc  : 
'''

import pytest


@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")

    yield
    print("执行teardown!")
    print("最后关闭浏览器")


def test_s1(open):
    print("用例1：搜索python-1")


def test_s2(open):  # 不传login
    print("用例2：搜索python-2")


def test_s3(open):
    print("用例3：搜索python-3")


if __name__ == "__main__":
    pytest.main(["-s", "test_f2.py"])