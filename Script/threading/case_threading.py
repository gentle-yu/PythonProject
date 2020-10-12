#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_threading.py
@Author: gentle.yu
@Date  : 2020/8/4 20:07
"""
import threading
import time


# 1.Python通过两个标准库thread和threading提供对线程的支持。thread提供了低级别的、原始的线程以及一个简单的锁.Threading模块封装了一些常用的方法，初学者直接学这个模块就行了。

# 2.Python中使用线程有两种方式：函数或者用类来包装线程对象


# def chi():
#     print("%s 吃着火锅开始：" % time.ctime())
#     time.sleep(1)
#     print("%s 吃着火锅：涮羊肉" % time.ctime())
#     time.sleep(1)
#     print("%s 吃着火锅：涮牛肉" % time.ctime())
#     time.sleep(1)
#     print("%s 吃着火锅：贡丸" % time.ctime())
#     time.sleep(1)
#     print("%s 吃火锅结束！" % time.ctime())
#
#
# def ting():
#     print("%s 哼着小曲1！" % time.ctime())
#     time.sleep(1)
#     print("%s 哼着小曲2！" % time.ctime())
#     time.sleep(1)
#     print("%s 哼着小曲3！" % time.ctime())
#     time.sleep(1)
#     print("%s 哼着小曲4！" % time.ctime())
#     time.sleep(1)
#     print("%s 哼着小曲5！" % time.ctime())
#     time.sleep(1)
#
#
# # 创建线程组
# threads = []
#
# # 创建线程t1，并添加到线程数组
# t1 = threading.Thread(target=chi)
# threads.append(t1)
# # 创建线程t2，并添加到线程数组
# t2 = threading.Thread(target=ting)
# threads.append(t2)
#
# if __name__ == '__main__':
#     # 启动线程
#     for t in threads:
#         t.start()

def chi(threadName, name):
    print("%s 吃着%s开始：" % (time.ctime(), threadName))
    time.sleep(1)
    print("%s 吃着火锅：涮羊肉" % time.ctime())
    time.sleep(1)
    print("%s 吃着火锅：涮牛肉" % time.ctime())
    time.sleep(1)
    print("%s 吃着火锅：贡丸" % time.ctime())
    time.sleep(1)
    print("%s 吃着%s结束--" % (time.ctime(), threadName))
    print("%s 运行结束！" % name)


def ting(threadName):
    print("%s 哼着%s1！" % (time.ctime(), threadName))
    time.sleep(1)
    print("%s 哼着小曲2！" % time.ctime())
    time.sleep(1)
    print("%s 哼着小曲3！" % time.ctime())
    time.sleep(1)
    print("%s 哼着小曲4！" % time.ctime())
    time.sleep(1)
    print("%s 哼着小曲5！" % time.ctime())
    time.sleep(1)


# 创建线程数组
threads = []

# 创建线程t1，并添加到线程数组
# 传kwargs参数
t1 = threading.Thread(target=chi, kwargs={"threadName": "火锅", "name": "吃火锅"})
threads.append(t1)
# 创建线程t2，并添加到线程数组
t2 = threading.Thread(target=ting, args=("小曲",))
threads.append(t2)

if __name__ == '__main__':
    # 启动线程
    for t in threads:
        t.start()
