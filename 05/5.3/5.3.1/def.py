#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 函数的定义
from __future__ import division
def arithmetic(x, y, operator):          # 定义函数arichmetic(),x.y是四则运算的两个操作数，operator是运算符。这三个参数的值是从实际参数传递过来的。
    result = {
        "+" : x + y,
        "-" : x - y,
        "*" : x * y,
        "/" : x / y 
    }
    return result.get(operator)          # 返回计算结果

# 函数的调用
print arithmetic(1, 2, "+")
