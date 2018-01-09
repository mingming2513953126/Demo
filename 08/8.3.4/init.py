#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:
    def __init__(self, color):         # 初始化属性__color    __init__是类fruit的初始化函数，即构造函数。该函数根据参数color的值初始化属性__color
        self.__color = color           # 获取参数color的值，对fruit类的属性__color进行赋值，需要前缀self。否则python解释器江认为__color是__init__()中的局部变量
        print self.__color             # 输出赋值后的__color      输出结果：red

    def getColor(self):
        print self.__color

    def setColor(self, color):         # 定义方法setcolor()，设置属性__color的值，如果初始化后需要改变属性__color的值，则调用setcolor()方法
        self.__color = color
        print self.__color

if __name__ == "__main__":
    color = "red"
    fruit = Fruit(color)                # 带参数的构造函数    调用函数 __init__()，并传递变量color的值
    fruit.getColor()                    # 调用方法getcolor() 返回属性__color的值，输出结果red
    fruit.setColor("blue")              # 调用方法setcolor() 重新设置属性__color的值，输出结果blue
