"""
返回值的演示
"""


# def max2(a, b):
#     if a > b :
#         # print(a)
#         return a
#     else:
#         # print(b)
#         return b
#
# c = max2(1,2)
# print(c)



# 是否可以不去接收 返回值
# def max2(a, b):
#     if a > b :
#         # print(a)
#         return a
#     else:
#         # print(b)
#         return b
#
# max2(1,2)
# # print(c)




# def max2(a, b):
#     if a > b :
#         print(a)
#         # return a
#     else:
#         print(b)
#         # return b
#
# c = max2(1,2)
# print(c)



# 多返回值的情况
# def test(): #  一个函数只要执行了return之后 接下来属于函数的代码都不执行 直接结束函数
#     return 1 # break 或者是 continue
#     return 2
#     return 3
#
# i = test()
# print(i)



# 一个return  多个返回值
def test(): #  一个函数只要执行了return之后 接下来属于函数的代码都不执行 直接结束函数
    return 1,2,3 # break 或者是 continue
    # return 2
    # return 3

i,j,o = test() # 数量一致,, 位置一致
print(i)
print(j)
print(o)


















































