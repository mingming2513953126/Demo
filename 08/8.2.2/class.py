#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Fruit:                          # 定义了一个fruit类
    def grow(self):                   # 创建了一个grow方法
        print "Fruit grow ..."

if __name__ == "__main__":
    fruit = Fruit()                   # 对fruit类实例化
    fruit.grow()                      # 调用fruit类的grow方法

