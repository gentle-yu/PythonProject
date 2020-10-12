#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : test_expectation.py
@Author: gentle.yu
@Date  : 2020/7/15 17:12
@Desc  : 
'''

import pytest

@pytest.mark.parametrize("test_input,expected",
                         [

                             ("3 + 5",8),
                             ("2 + 4",6),
                             pytest.param("6 * 9",42, marks=pytest.mark.xfail), #xfail 跳过标记失败的用例
                         ])
def test_eval(test_input,expected):
    assert  eval(test_input) == expected


if __name__ == '__main__':
    pytest.main(["-s", "test_expectation.py"])
