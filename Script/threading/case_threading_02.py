#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_threading_.py
@Author: gentle.yu
@Date  : 2020/8/5 11:46
"""

import threading
import time

'''多线程threading之封装式'''


def chi(people):
    print("%s吃火锅的小伙伴-羊肉：%s" % (time.ctime(), people))
    time.sleep(1)
    print("%s吃火锅的小伙伴-鱼丸：%s" % (time.ctime(), people))


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, people, name):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people

    def run(self):  # 把要执行的代码写到run函数里面，线程在创建后会直接运行run函数
        '''重写run方法'''
        print("开始线程：" + self.threadName)

        chi(self.people)  # 执行任务
        print("结束线程：" + self.name)


# 创建新线程
thread1 = myThread("yyc", "Thread-1")
thread2 = myThread("gentle.yu", "Thread-2")

# 开启线程
thread1.start()
thread2.start()

time.sleep(1)
print("退出主线程")
