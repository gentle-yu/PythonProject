#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : test_html_screen.py
@Author: gentle.yu
@Date  : 2020/7/15 15:38
@Desc  : 
'''

from selenium import webdriver
import time


def test_01(browser:webdriver.Firefox):
    browser.get("https://www.cnblogs.com/yoyoketang/")
    time.sleep(2)
    t = browser.title
    assert t =="上海-哟哟"
