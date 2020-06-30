"""
演示匿名函数
"""

# 普通函数的定义
# def add2(a,b):
#     return a + b  # 返回值
#
# # 普通函数的调用
# c = add2(1,2)   # 执行完函数的代码之后,代表的就是返回值
# print(c)  # 3
#
# # 简写 >>>  匿名函数出现了  4 > 3
# # 1 函数名 = lambda 形参 : 返回值  匿名函数
# add2 = lambda a,b : a + b
# c = add2(1,2)
# print(c)
#
# #  3 > 2  结果 = (lambda 形参 : 返回值)(实参1`)
# c = (lambda a,b : a+b)(1,2)
# print(c)
#
# # 2 > 1
# print((lambda a,b : a+b)(1,2))



# 注意事项
"""
1, 无参数, 无返回值
2, 有参数, 无返回值
3, 有参数, 有返回值
"""
# (lambda 形参 : 返回值)(实参1`)

# 1 无参数 无返回值
# c = (lambda  : )()
# print(c)


# 1 无参数 有返回值是可以的
# c = (lambda  : 10)()  # return 10
# print(c)  # 10

# 1 无参数 有返回值 多返回值情况是不允许的
# c,d = (lambda  : 10,20)()  # return 10
# print(c)  # 10 20  (10,20)
# print(d)






























































































