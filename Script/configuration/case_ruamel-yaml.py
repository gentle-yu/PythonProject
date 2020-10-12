#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_ruamel-yaml.py
@Author: gentle.yu
@Date  : 2020/8/17 14:53
"""
import os
from ruamel import yaml

# ######## yaml 文件读写 #########

# 将字典写入到yaml
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '7.0',
    'deviceName': 'A5RNW18316011440',
    'appPackage': 'com.tencent.mm',
    'appActivity': '.ui.LauncherUI',
    'automationName': 'Uiautomator2',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    'noReset': True,
    'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
    }

curlpath = os.path.dirname(os.path.realpath(__file__))
yamlpath = os.path.join(curlpath, "case_ruamel-yaml.yaml")

# 写入到yaml文件
with open(yamlpath, "w", encoding="utf-8") as f:
    yaml.dump(desired_caps, f, Dumper=yaml.RoundTripDumper)