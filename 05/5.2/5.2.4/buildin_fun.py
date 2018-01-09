#!/usr/bin/python
# -*- coding: UTF-8 -*-

# apply()
def sum(x=1, y=2):                  # 定义了函数sum， 并定义了两个参数
    return x + y

print apply(sum, (1, 3))            # 通过apply调用sum(1, 3)   输出:4

# filter()                          # 对某个序列做过滤处理，对“真”过滤
def func(x): 
    if x > 0:
        return x

print filter(func, range(-9, 10))   # 使用range()生成待处理列表，然后把该列表值依次传入func().func()返回结果给filter()，最后filter()把返回的值组成一个列表返回


# reduce()                          # 实现连续处理功能
def sum(x, y):                      # 定义了一个sum函数，该函数需要两个参数，来执行累加操作
    return x + y

print reduce(sum, range(0, 10))     # 对0至9执行累加操作，输出45
print reduce(sum, range(0, 10), 10) # 对10+0+1..+9执行累加计算，输出：55
print reduce(sum, range(0, 0), 10)  # 由于rang(0, 0)返回空列表，所以结果是10

# map()                             # 对tuple元组进行“解包”操作
def power(x): return x ** x         # 定义了一个power()函数，实现了数字的幂运算
print map(power, range(1, 5))       # 把数字1234依次传入函数power中，计算后的结果组成一个列表返回。输出结果：[1,4,27,256]
def power2(x, y): return x ** y     # 定义了一个power()2函数，计算x的y次幂
print map(power2, range(1, 5), range(5, 1, -1))  # 提供了两个列表参数，依次计算1^5,2^4,3^3,4^2,计算后的结果组成一个列表返回，输出：[1,16,27,16]
