"""
演示作用域
"""
# 变量的作用域

# 函数外部的变量 作用域范围大 全局变量
# num2 = 20
#
# def max2(a,b):
#     if a > b:
#         print("%d和%d中的较大的值是%d" % (a,b,a))
#     else:
#         print("%d和%d中的较大的值是%d" % (a,b,b))
#     # 函数内部定义的变量 作用域范围小 局部变量
#     num1 = 10
#     print(num1)
#     print(num2)
#
# def min2(c,d):
#     if c < d:
#         print("%d和%d中的较小的值是%d" % (c,d,c))
#     else:
#         print("%d和%d中的较小的值是%d" % (c,d,d))
#     print(num2)
#
#
# max2(1,2)
# min2(3,4)



# 当全局变量与局部变量起冲突了
# 全局变量
a = 10

def demo():
    # 局部变量
    global a # 让局部变量变成全局变量
    a = 20
    print(a)  # a = 20

demo()
print(a)














































"""
全局变量与局部变量的冲突
"""

# a = 10
# def demo():
#     global a # 变成全局变量
#     a = 20
#     print(a)
#
#
# demo()
# print(a)



































