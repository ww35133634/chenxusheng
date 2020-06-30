"""
演示可变参数
"""

# 可以用来接收任意数量的实参  普通的形参 >>> 可变参数

# def sum3(a,b,c):  # 任意三个数的求和
#     sum3 = a + b + c  # 保存着三个数的求和的结果
#     print(sum3)
#
# sum3(1,2,3)  # 实参数量与形参一一对应


#      形参   可变参数 *args : 接收任意数量的实参 并且以一个元组的方式保存
# def demo(*args):
#     print(args)  # 元组
#
# demo(1,2,3)


#       变成一个元组里面可以保存任意数量的数据
# def demo(*args):  # 自动组包 >>>  一个元组
#     for i in args:
#         print(i)
#
# demo(1,2,3)  # 3个数据


# 我们是否可以设置多个可变参数  只能有一个, 多了就会报错
# def demo(*args, *args2):
#     print(args)
#     print(args2)
#
# demo(1,2,3,4)  # 四个实参


#            必须给他传值
# 顺序问题,, 位置形参,   默认参数(形参), 可变参数 *

# def demo(a,b,*args):
#     print(a)
#     print(b)
#     print(args)  # () 空元组
#
# demo(1,2)

#      位置形参  可变参数 位置参数就不能够放在可变参数的后面
#
# def demo(a,b,*args,c):
#     print(a)  # 1
#     print(b)  # 2
#     print(args)  # (3,4,5)
#     print(c)  # 6
#
# demo(1,2,3,4,5,c = 6)  # c = 6  因为是关键字参数,所以可以拿到值


#    位置形参  可变参数:任意数量的实参(位置参数)  不会去接收关键字参数
def demo(a,b,*args,c):
    print(a)
    print(b)
    print(args)
    print(c)

#   位置实参  通过位置来进行传递 a : 1  b : 2  args > *: (3,4,5,6)  c = 6 ???
demo(1,2,3,4,5,c = 6)  # c = 6  因为是关键字参数,所以可以拿到值
#              6 是指定要给c  可变参数有人要的东西我就不要























































