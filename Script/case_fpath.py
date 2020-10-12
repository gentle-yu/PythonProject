#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_fpath.py
@Author: gentle.yu
@Date  : 2020/8/4 19:39
"""

import os

path = r"/Script/file_deal"


def get_files(path, rule=".py"):
    all = []
    for fpath, dirname, fnames in os.walk(path):
        for f in fnames:
            filename = os.path.join(fpath, f)
            if filename.endswith(rule):
                all.append(filename)
    return all


if __name__ == '__main__':
    b = get_files(r"/Script/file_deal")
    for i in b:
        print(i)
