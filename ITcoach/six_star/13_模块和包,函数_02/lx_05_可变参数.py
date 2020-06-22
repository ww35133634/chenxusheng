"""
演示可变(不定长参数)参数
"""

# def sum0(a,b,c):
#     sums = a + b + c
#     print(sums)
#
# sum0(1,2,3)

# 组包
# def sum0(*args):
#     # 求和操作
#     sums = 0
#     for i in args:
#         # sums = sums + i
#         sums += i
#     print(sums)
# # 数量不受限制,,可以随便传
# sum0(1,2,3,4,5,6)

# def demo(*args):
#     for i in args:
#         print(i)
#
# demo(1,2,3,4,5)


# def demo(*args,):
#     for i in args:
#         print(i)
#     # for i in args2:
#     #     print(i)
#
# demo(1,2,3,4,5)

# 有了可变参数的存在,,是否还能存在位置参数  位置参数必须在可变参数的前面
# def demo(a,b,*args):
#     print(a)
#     print(b)
#     print(args)
#     # print(c)
# demo(1,2,3,4,5)


# 通过关键字参数去精确传值的形参,,要放在可变参数的后面
def demo(x,y,*args,a,b):
    print(x)
    print(y)
    print(args)
    print(a)
    print(b)

demo(1,2,3,a=4,b=5)














