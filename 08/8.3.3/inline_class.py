#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Car:
    class Door:                     # 内部类
        def open(self):
            print "open door"
    class Wheel:                    # 内部类
        def run(self):
            print "car run"

if __name__ == "__main__":     
    car = Car()                     # 创建car类的实例car
    backDoor = Car.Door()           # 内部类的实例化方法一   创建Door类的实例backDoor   使用类名前导方式创建
    frontDoor = car.Door()          # 内部类的实例化方法二   创建Door类的实例frontDoor   使用对象名前导方式创建
    backDoor.open()                 # 调用open()方法       输出:open door
    frontDoor.open()
    wheel = Car.Wheel()             # 创建Wheel类的实例wheel
    wheel.run()                     # 调用run()           输出：car run




