#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:
    price = 0

    def __init__(self):
        self.__color = "red"

    def getColor(self):                     # 定义了公有方法getcolor（）
        print self.__color                  # 静态方法获取属性__color的值
    
    @ staticmethod                          # 静态方法       @ staticmethod指令声明方法getprice为静态方法
    def getPrice():                         # 定义getprice（）方法，该方法没有self参数
        print Fruit.price

    def __getPrice():                       # 定义了__getprice（）方法   该方法没有提供self参数
        Fruit.price = Fruit.price + 10
        print Fruit.price
    
    count = staticmethod(__getPrice)        # 静态方法调用staticmethod（）把__getprice()转换为静态方法，并赋值给变量count。count()即为fruit类的静态方法

if __name__ == "__main__":
    apple = Fruit()
    apple.getColor()                        # 调用fruit对象的方法getcolor()，返回属性__color的值
    Fruit.count()                           # 调用静态方法count（）。由于创建了对象Apple，所以静态属性price执行一次加10的运算。输出结果：10
    banana = Fruit()
    Fruit.count()                           # 由于创建了对象bannana，因此静态方法count()被第二次调用。静态属性price的值为20.输出结果为20
    Fruit.getPrice()                        # 调用静态方法getprice()。输出结果：20
