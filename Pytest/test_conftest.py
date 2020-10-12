#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : test_conftest.py
@Author: gentle.yu
@Date  : 2020/7/15 17:56
@Desc  : 
'''

import pytest


def test_answers(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    assert 0


if __name__ == '__main__':
    pytest.maim(["-s", "test_case1.py"])

