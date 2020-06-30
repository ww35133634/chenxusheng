"""
演示异常出现的原理-手动制造异常
"""
# NameError: name 'a' is not defined 也相当于一句代码,


a = 1  # a:1
b = 0  # b:0
# i = a // b # ZeroDivisionError: integer division or modulo by zero 除数

# 一旦程序发现了除法操作 去检查这个b是否是等于0
if b == 0:  # 制造这样一个异常 的代码 语法格式
    raise ZeroDivisionError('不能这样做')


























































































