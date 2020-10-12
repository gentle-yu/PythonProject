#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : test_f4.py
@Author: gentle.yu
@Date  : 2020/7/13 20:50
@Desc  : 
'''

import smtplib
import pytest


@pytest.fixture(scope="module")
def smtp():
    with smtplib.SMTP("smtp.gmail.com") as smtp:
        yield smtp  # provide the fixture value