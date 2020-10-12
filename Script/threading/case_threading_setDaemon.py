#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_threading_setDaemon.py
@Author: gentle.yu
@Date  : 2020/8/5 14:44
"""
# 主线程总，创建了子线程thread1和thread2，并且在主线程中调用了thread.setDaemon()，这个意思是吧主线程设置为守护线程，这时候要是主线程结束，就不管了子线程是否完成，一并和主线程退出

# （注意：必须在start()方法调用之前设置，如果不设置未守护线程，程序就会被无限挂起）

import threading
import time


def chi(people):
    print("%s 吃火锅的小伙伴-羊肉：%s" % (time.ctime(), people))
    time.sleep(1)
    print("%s 吃火锅的小伙伴-鱼丸：%s" % (time.ctime(), people))


class myThread (threading.Thread):   # 继承父类threading.Thread
    def __init__(self, people, name):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people

    def run(self):   # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        '''重写run方法'''
        print("开始线程: " + self.threadName)

        chi(self.people)     # 执行任务
        print("结束线程: " + self.name)


print("yyc请小伙伴开始吃火锅：！！！")

# 创建新线程
thread1 = myThread("yyc", "Thread-1")
thread2 = myThread("gentle.yu", "Thread-2")

# 守护线程
thread1.setDaemon(True)     # 必须在start之前
thread2.setDaemon(True)

# 开启线程
thread1.start()
thread2.start()

time.sleep(0.1)
print("退出主线程：吃火锅结束，结账走人")