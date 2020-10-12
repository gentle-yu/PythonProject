# ******
# 运行失败，查看百度结果是版本问题

# ******

#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : conftest.py
@Author: gentle.yu
@Date  : 2020/7/13 18:20
@Desc  : 
'''

#from selenium import webdriver
import pytest


#driver = None


@pytest.fixture()
def login():
    print("输入账号，密码先登录")


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )

@pytest.fixture
def cmdopt(request):
    return  request.config.getoption("--cmdopt")

"""
@pytest.mark.hookwrapper
def pytest_runtest_makerport(item):
    '''
    测试失败的时候，自动截图，展示到html报告中
    '''
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report,'extra',[])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report,'wasxfail')
        if (report.skipped and xfail) or (report.failes and not  xfail):
            file_name = report.nodeid.replace("::","_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot():
    '''
    截图保存为base64，展示到HTML中
    '''

@pytest.fixture(scope='session',autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Firefox()
    return driver
    
"""