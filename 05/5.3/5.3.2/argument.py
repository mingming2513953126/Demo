#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import division

def append(args=[]):                       # 定义了一个append()函数，参数是一个带默认值的列表
    if len(args) <= 0:                     # 使用len()判断列表args的长度是否大于0，如果小于等于0，则把args置为空列表，即取消函数参数的绑定
        args = []
    args.append(0)                         # 在列表中追加一个元素“0”
    print args

append()
append([1])                                # 传递了一个列表[1],append()中追加一个元素“0”输出结果[1,0]
append()                                   # 调用append(),通过len(args)的判断，取消了参数的名字绑定。输出结果[0]

# 函数的默认参数
def arithmetic(x=1, y=1, operator="+"):         # 使用赋值表达式的方式定义参数的默认值
    result = {
        "+" : x + y,
        "-" : x - y,
        "*" : x * y,
        "/" : x / y 
    }
    return result.get(operator)                 # 返回计算结果

print arithmetic(1, 2)                          # 参数x,y的值分别赋值为1,2  参数operator使用默认值“+”  输出3
print arithmetic(1, 2, "-")                     # 提供了3个实际参数，这3个值将分别覆盖形式参数的默认值。输出“-1”
print arithmetic(y=3, operator="-")             # 指定参数y，operator的值。输出 “-2”   这里必须使用赋值表达式的方式传递参数，否则，python解释器将误认为x=3，y=“-”
print arithmetic(x=4, operator="-")             # 指定参数x，operator的值。输出3
print arithmetic(y=3, x=4, operator="-")        # 使用赋值表达式传递参数，可以颠倒参数列表的顺序。输出结果1，参数可以是变量，也可以是元组，列表等内置数据结构



# 列表作为参数传递
def arithmetic(args=[], operator="+"):                # 把参数xy合并为一个参数，通过args列表传递xy的值
    x = args[0]                                       # 从列表中取出参数值分别赋值给变量xy
    y = args[1]
    result = {
        "+" : x + y,
        "-" : x - y,
        "*" : x * y,
        "/" : x / y 
    }
    return result.get(operator)     # ���ؼ�����

print arithmetic([1, 2])                              # 把列表[1,2]传递给arichmetic(),输出：3

# 传递可变参数
def func(*args):                                      # 在参数args前使用标识符*
    print args

func(1, 2, 3)                                         # 调用函数    由于参数使用了“*args”的形式，因此传入的实际参数被“打包”到一个元组中，其中的参数123成为args元组的元素，输出123

# 传递可变参数
def search(*t, **d):                                 # “*t”与第12行代码中的“one”“three”对应，one three组成一个元组t。**d 与 one=1 two=2 three=3对应，生成一个字典{one：1，two2，three3}
    keys = d.keys()
    values = d.values()
    print keys                                       # 输出['three','two','one']
    print values                                     # 输出['3','2','1']
    for arg in t: 
        for key in keys: 
            if arg == key:
                print "find:",d[key]

search("one", "three", one="1",two="2",three="3")   # 7到10行代码在字典d中查找元组t中的值，如果找到，则输出，输出：find1   find3
        
    


