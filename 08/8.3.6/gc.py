#!/usr/bin/python
# -*- coding: UTF-8 -*-

import gc

class Fruit:
    def __init__(self, name, color):         # 初始化 name、color属性    在__init__方法中定义了两个属性，__name 表示水果的名称  __color表示水果的颜色
        self.__name = name
        self.__color = color

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getName(self):
        return self.__name

    def setColor(self, name):
        self.__name = name

class FruitShop:                             # 水果店类
    def __init__(self):
        self.fruits = []                     # 定义了属性fruit  fruit是一个列表，用于存放水果店中的水果

    def addFruit(self, fruit):               # 添加水果   把对象fruit添加到fruits列表
        fruit.parent = self                  # 把fruit类关联到fruitshop类   设置fruit对象的parent属性为self。即把fruitshop实例化对象的引用关联到添加的fruit对象上
        self.fruits.append(fruit)

if __name__ == "__main__":
    shop = FruitShop()
    shop.addFruit(Fruit("apple", "red"))    # 向shop中添加了两个fruit对象
    shop.addFruit(Fruit("banana", "yellow"))
    print gc.get_referrers(shop)            # 调用函数get_ referrers()列出shop对象关联的所有对象
    del shop                                # 删除shop对象，但是shop对象关联的其他对象没有释放
    print gc.collect()                      # 显示调用垃圾回收器   调用函数collect()释放shop对象关联的其他对象，collect()返回结果表示释放的对象个数。输出为：7

