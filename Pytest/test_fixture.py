#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : test_fixture.py
@Author: gentle.yu
@Date  : 2020/7/13 17:25
@Desc  :
'''

import pytest


# 不带参数时默认scope="function"
@pytest.fixture()
def login():
    print("输入账号、密码登陆")


def test_s1(login):
    print("用例1：登录之后其它动作111")


def test_s2():
    print("用例2：不需要登录，操作222")


def test_s3(login):
    print("用例3：登录之后其它动作333")


if __name__ == '__main__':
    pytest.main(["-s","test_fixtrue.py"])
