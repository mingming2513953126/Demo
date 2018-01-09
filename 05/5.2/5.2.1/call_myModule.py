#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 调用自定义模块的类和函数
import myModule

myModule.func()                        # 调用模块的函数       调用时需要加前缀，否则python不知道func()所在模块的命名空间。输出：MyModule.func()
myClass = myModule.MyClass()           # 创建类Myclass的实例myclass。这里也需要使用myModule来调用类
myClass.myFunc()                       # 调用类的方法myFunction()    输出结果MyModule.MyClass.myFunc()
