#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_threading_join.py
@Author: gentle.yu
@Date  : 2020/8/5 15:23
"""

# 如果想让主线程等待子线程结束后运行的话，就需要用到join()，此方法是在start之后

# join(timeout) 次方法有个timeout参数，是线程超时时间设置

import threading
import time


def chi(people):
    print("%s 吃火锅的小伙伴-羊肉：%s" % (time.ctime(), people))
    time.sleep(1)
    print("%s 吃火锅的小伙伴-鱼丸：%s" % (time.ctime(), people))


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, people, name):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        '''重写run方法'''
        print("开始线程: " + self.threadName)

        chi(self.people)  # 执行任务
        print("结束线程: " + self.name)


print("yyc请小伙伴开始吃火锅：！！！")

# 创建线程
thread1 = myThread("yyc", "Thread-1")
thread2 = myThread("gentle.yu", "Thread-2")

# 开启线程
thread1.start()
thread2.start()

# 阻塞主线程，等子线程结束
thread1.join()
thread2.join()

time.sleep(0.1)
print("退出主线程：吃火锅结束，结账走人")