#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : test_parameter_02.py
@Author: gentle.yu
@Date  : 2020/7/20 16:13
@Desc  : 
'''

import pytest

# 测试登陆数据
test_login_data = [{'user': 'admin1', 'psw': '111111'},
                   {'user': 'admin2', 'psw': ''}]


@pytest.fixture(scope="module")
def login(request):
    user = request.param['user']
    psw = request.param['psw']
    print("登陆账号：%s" % user)
    print("登陆密码：%s" % psw)
    if psw:
        return True
    else:
        return False


# indirect = True 声明login是个函数
@pytest.mark.parametrize("login", test_login_data, indirect=True)
def test_login(login):
    a = login
    print("测试用例中login的返回值：%s" % a)
    assert a, "失败原因：密码为空"


if __name__ == '__main__':
    pytest.main(["-s", "test_parameter_02.py"])
