#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_readyaml.py
@Author: gentle.yu
@Date  : 2020/8/16 16:00
"""

import yaml
import os

# 获取当前脚本所在文件夹路径
curpath = os.path.dirname(os.path.realpath(__file__))

# 获取yaml文件路径
#yamlpath = os.path.join(curpath, "case_readyaml.yaml")

# 用open方法打开直接读出来
f = open(yamlpath, 'r', encoding='utf-8')
cfg = f.read()
print(type(cfg))
print(cfg)

d = yaml.load(cfg)
print(d)
print(type(d))