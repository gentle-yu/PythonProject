#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_threading_event.py
@Author: gentle.yu
@Date  : 2020/8/14 14:52
"""

# Event()       事件处理的机制：全局定义了一个内置标志Flag，如果Flag值为 False，那么当程序执行 event.wait方法时就会阻塞，如果Flag值为True，那么event.wait 方法时便不再阻塞。
#       -set(): 将标志设为True，并通知素有处于等待阻塞状态的线程恢复运行状态
#       -clear(): 将标志设为False
#       -wait(timeout): 如果标志为True将立即返回，否则阻塞线程至等待阻塞状态，等待其他线程调用set()
#       -isSet(): 获取内置标志状态，返回True或False

import threading
import time

event = threading.Event()


def chi(name):
    # 等待事件，进入等待阻塞状态
    print("%s 已经启动" % threading.currentThread().getName())
    print("小伙伴%s 已经进入就餐状态！" % name)
    time.sleep(1)
    event.wait()
    # 收到事件后进入运行状态
    print("%s 收到通知了." % threading.currentThread().getName())
    print("小伙伴%s 开始吃喽" % name)


# 设置线程组
threads = []

# 创建新线程
thread1 = threading.Thread(target=chi, args=("a",))
thread2 = threading.Thread(target=chi, args=("b",))

# 添加到线程
threads.append(thread1)
threads.append(thread2)

# 开启线程
for thread in threads:
    thread.start()

time.sleep(0.1)

# 发送通知事件
print("主线程通知小伙伴开吃")
event.set()