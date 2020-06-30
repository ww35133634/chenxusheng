"""
演示返回值
"""
"""
基础的    零基础:学习能力强 时间花的多
预习,比较难,  网课 走神  听不懂,,,
1,边看边敲,copy
2,看完再敲,
3,需求 案例, 自己敲出来,  预习,  往回看, 温故而知新, 
10  3  3  7
"""

# 求两个数最大值
# def max2(a,b):
#     if a > b:
#         print(a)
#         return a
#     else:  # a < b   a <= b
#         print(b)
#         return b  # 返回值
#
# c = max2(3,4)  # c >> b >>> 4
# print(c + 3)


# print(b + 3)  # 我们是没有真正的去得到函数内部的数据

# 参数,,定义的时候有形参,,  调用的时必须有实参
# 就是定义的时候有返回值 调用的时候必须去接收嘛
# 允许没有变量去接收返回值 成立
# def max2(a,b):
#     if a > b:
#         # print(a)
#         return a
#     else:  # a < b   a <= b
#         # print(b)
#         return b  # 返回值
#
# max2(3,4)  # c >> b >>> 4



# 有变量去接收, 但是呢没有返回值
# def max2(a,b):
#     if a > b:
#         print(a)
#         # return a
#     else:  # a < b   a <= b
#         print(b)
#         # return b  # 返回值
#
# c = max2(3,4)
# print(c)  # C >> None  为空



# 多个return的情况
# def demo():
#     print('函数内部代码...')
#     return 1  # return被执行了之后,所有他之后属于函数内部的代码,,都不会被执行,, break
#     # 1.可以把数据返回出去给别人使用
#     # 2.控制函数的执行流程  break
#     # print('------')
#     # return 2
#     # print('------')
#     # return 3
#
# a = demo()  # 运行完函数内部代码之后,代表的就是返回值本身
# print(a)  # 1



# 多个return是不行的, 返回值
# 一个return 多个返回值可以嘛
def demo():
    print('欢迎来到函数内部...')
    return 1,2,3
    print('你猜猜我会不会执行...')


# a = demo()  # 1.执行函数内部代码, 2,执行完代码之后代表返回值
# # 自动组包的意思,   3个数据  一个容器来装, 自动组包>>>元组
# print(a)
a, b, c = demo()  # 3个数据 3个箱子
print(a)
print(b)
print(c)










































