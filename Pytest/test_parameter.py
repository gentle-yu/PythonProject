#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : test_parameter.py
@Author: gentle.yu
@Date  : 2020/7/20 15:58
@Desc  : 
'''

import pytest

# 测试登陆数据
test_login_data = [('admin', '111111'), ('admin', '')]


def login(user, psw):
    print("登陆账号:%s" % user)
    print("登陆密码:%s" % psw)
    if psw:
        return True
    else:
        return False


@pytest.mark.parametrize('user,psw', test_login_data)
def test_login(user, psw):
    result = login(user, psw)
    assert result == True,"失败原因：密码为空"


if __name__ == '__main__':
    pytest.main(["-s", "test_parameter.py"])
