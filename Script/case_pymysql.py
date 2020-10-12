#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_pymysql.py
@Author: gentle.yu
@Date  : 2020/8/19 17:09
"""

import pymysql

# 打开数据库
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='test1234',
    db='yyc'
)

# 使用cuersor()方法创建一个游标对象cur
cur = db.cursor()

# 使用execute()方法执行sql语句
cur.execute("select * from test")

# 使用fetchall()方法获取查询结果
data = cur.fetchall()
print(data)

# 关闭数据库
db.close()