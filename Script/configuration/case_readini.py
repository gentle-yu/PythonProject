#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_readini.py
@Author: gentle.yu
@Date  : 2020/8/16 17:00
"""

import configparser
import os
curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "case_readini.ini")
print(cfgpath)  # cfg.ini的路径

# 创建管理对象
conf = configparser.ConfigParser()

# 读ini文件
conf.read(cfgpath, encoding="utf-8")  # python3

# conf.read(cfgpath)  # python2

# 获取所有的section
sections = conf.sections()

print(sections)  # 返回list

items = conf.items('email_163')
print(items)  # list里面对象是元祖