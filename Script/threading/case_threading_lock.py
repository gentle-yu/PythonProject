#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_threading_lock.py
@Author: gentle.yu
@Date  : 2020/8/5 16:06
"""

# 每当一个线程a要访问共享数据时，必须先获得锁定；如果已经有别的线程b获得锁定了，那么就让线程a暂停，也就是同步阻塞；等到b访问完成，释放锁以后，再让a继续

# 用threading.Lock()这个类里面的两个方法  -acquire()锁住     -release()释放锁

import threading
import time


def chi(people, do):
    print("%s吃火锅的小伙伴：%s" % (time.ctime(), people))
    time.sleep(1)
    for i in range(3):
        time.sleep(1)
        print("%s%s正在 %s鱼丸" % (time.ctime(), people, do))
    print("%s吃火锅的小伙伴： %s" % (time.ctime(), people))


class myThread(threading.Thread):  # 继承父类threading.Thread

    lock = threading.Lock()  # 线程锁

    def __init__(self, people, name, do):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people
        self.do = do

    def run(self):
        '''重写run方法'''
        print("开始线程：" + self.threadName)

        # 执行任务之前锁定线程
        self.lock.acquire()

        chi(self.people, self.do)  # 执行任务

        # 执行完之后，释放锁
        self.lock.release()

        print("结束线程：" + self.name)


print("yyc请小伙伴们吃火锅")

# 设置线程组
threads = []

# 创建线程
thread1 = myThread("yyc", "thread-1", "添加")
thread2 = myThread("gentle.yu", "thread-2", "吃掉")

# 添加到线程组
threads.append(thread1)
threads.append(thread2)

# 开启线程
for thread in threads:
    thread.start()

# 阻塞主线程，等待子线程结束
for thread in threads:
    thread.join()

time.sleep(1)
print("退出主线程：吃火锅结束")