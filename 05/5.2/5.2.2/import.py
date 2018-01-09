#!/usr/bin/python
# -*- coding: UTF-8 -*-

import myModule                         # 导入 myModule 模块
print "count =", myModule.func()        # 调用函数func()
myModule.count = 10                     # 给模块myModule中变量count赋值，此时count=10
print "count =", myModule.count         # 获取变量count的值   输出：10

import myModule                         # 再次导入 myModule 模块     变量count的初始值为10
print "count =", myModule.func()        # 调用func(),变量count的值加1. 输出结果：count=11

# import置于条件语句中
if myModule.count > 1:                  # 判断myModule.count的值是否大于1
    myModule.count = 1                  # 如果count的值大于1，则把count变成1.  之前：11   所以变成1
else:
    import myModule                     # 如果count的值小于1，则把count变成myModule模块
print "count =", myModule.count         # 输出：1
