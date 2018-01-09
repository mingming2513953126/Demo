#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:
    def __init__(self, color):         # 初始化属性__color
        self.__color = color
        print self.__color

    def __del__(self):                 # 析构函数    self不可或缺
        self.__color = ""
        print "free ..."

    def grow(self):
        print "grow ..."

if __name__ == "__main__":
    color = "red"
    fruit = Fruit(color)                # 带参数的构造函数
    fruit.grow()                        # 调用方法grow()  当程序执行完方法grow()后，对象fruit将超出其作用域，python会结束对象fruit的生命周期。输出结果：free...
    # del fruit                         # 执行析构函数
