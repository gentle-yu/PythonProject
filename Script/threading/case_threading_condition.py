#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_threading_condition.py
@Author: gentle.yu
@Date  : 2020/8/6 13:57
"""

# condition（条件变量）通常与一个锁关联。需要在多个condition中共享一个锁时，可以传递一个lock/Rlock实例给构造方法，否则它将自己生成一个Rlock实例。

# Condition():
#       -acquire():线程锁
#       -release():释放锁
#       -wait(timeout):线程挂起，直到收到一个notify通知或者超时才会被唤醒继续运行。wait()必须在已获得lock前提下使用
#       -notify(n=1):通知其他线程，那些挂起的线程接到这个通知之后会开始运行，默认是通知一个正在等待该condition的线程，最多则唤醒n个等待的线程。必须在已获得lock前提下使用
#       -natifyAll():如果wait状态线程比较多，notifyAll的作用就是通知所有线程

import threading
import time

con = threading.Condition()

num = 0


# 生产者
class Producer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # 锁定线程
        global num
        con.acquire()
        while num < 5:
            print("开始添加！！")
            num += 1
            print("火锅里鱼丸个数：%s" % str(num))
            time.sleep(1)

        if num >= 5:
            print("火锅里面鱼丸个数已经够5个了，无法添加了")
            # 等待唤醒的线程
            con.notify()  # 唤醒小伙伴开吃啦

        # 释放锁
        con.release()


# 消费者
class Consumers(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        con.acquire()
        global num
        while num > 0:
            print("开吃啦")
            num -= 1
            print("火锅里剩余的鱼丸数量%s" % str(num))
            time.sleep(1)

        if num <= 0:
            print("锅里没货啦，赶紧加鱼丸吧！")
            con.wait()
        con.release()


a = Producer()
b = Consumers()
a.start()
b.start()
