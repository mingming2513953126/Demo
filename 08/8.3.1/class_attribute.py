#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:
    def __init__(self):
        self.__color = "red"

class Apple(Fruit):             # Apple继承了Fruit
    pass
        
if __name__ == "__main__":
    fruit = Fruit()
    apple = Apple()
    print Apple.__bases__       # 输出基类组成的元祖    输出Apple类的父类元组。由于python支持多重继承，所以可能存在多个父类。输出结果：（<class__main__.Fruit at 0x00BE4ae0>）
    print apple.__dict__        # 输出属性组成的字典    输出结果：{’_Fruit__color‘:'red'}
    print apple.__module__      # 输出类所在的模块名    输出结果：__main__
    print apple.__doc__         # 输出doc文档         由于没有定义类的doc字符串，所以输出结果为none



