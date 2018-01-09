#!/usr/bin/python
# -*- coding: UTF-8 -*-

import myModule
print __doc__               # 调用了模块的__doc__属性，由于该模块没有定义文档字符串，所以输出none
print __doc__               # 属性__doc__可以输出文档字符串的内容