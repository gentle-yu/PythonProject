#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : test_fixt_addfinalizer.py
@Author: gentle.yu
@Date  : 2020/7/14 10:57
@Desc  : 
'''

import smtplib
import pytest


@pytest.fixture(scope="module")
def smtp_connection(request):
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

    def fin():
        print("teardown smtp_connection")
        smtp_connection.close()

    request.addfinakizer(fin)
    return smtp_connection  # provide the fixture value
