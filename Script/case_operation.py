#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : case_operation.py
@Author: gentle.yu
@Date  : 2020/8/4 17:28
"""

op_type = {
    "1": "加法",
    "2": "减法",
    "3": "乘法",
    "4": "除法"
}


def add(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    assert b != 0
    return a / b


def menu():
    print('- ' * 16)
    print('|', ' ' * 8, '1、加法运算', ' ' * 8, '|')
    print('|', ' ' * 8, '2、减法运算', ' ' * 8, '|')
    print('|', ' ' * 8, '3、乘法运算', ' ' * 8, '|')
    print('|', ' ' * 8, '4、除法运算', ' ' * 8, '|')
    print('- ' * 16)


if __name__ == '__main__':

    while True:
        print('\nwelcome to here！')
        menu()

        op_type_index_str = input("请输入指定的菜单前面的数字开启运算")
        op_type_index = int(op_type_index_str)

        if op_type_index not in [1, 2, 3, 4]:
            print("*" * 30)
            print("*", " "* 2, "请输入正确的数字开启运算", " " * 2, "*")
            print("*" * 30)
            continue

        print('\n welcome to "%s"运算' % op_type[op_type_index_str])

        input_a = int(input("\n请输入第一个数字"))
        print("接收到你输入的第一个数字是：", input_a)

        input_b = int(input("\n请输入第二个数字"))
        print("接收到你输入的第二个数字是：", input_b)

        print("\n运算结果是：")

        if op_type_index == 1:
            print(add(input_a, input_b))
            continue

        if op_type_index == 2:
            print(subtraction(input_a, input_b))
            continue

        if op_type_index == 3:
            print(multiply(input_a, input_b))
            continue

        if op_type_index == 4:
            print(divide(input_a, input_b))
            continue
