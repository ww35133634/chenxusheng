"""
演示默认参数(形参)
"""
# 默认参数
# def demo(a = 1, b = 2):
#     print(a)  # 1  5
#     print(b)  # 2  10
#
# demo(5)  # 实参的优先级是大于默认参数的值的优先级






# # 形参   位置形参    默认形参
# def demo(a, b ,c=3 ,d=4):
#     print(a)  # 1
#     print(b)  # 2
#     print(c)  # 5
#     print(d)  # 6
#
#
# demo(1,2,5,6)




# 位置关系: 默认形参只能够写在位置形参的后面,,--实参都是位置实参的情况下
# 形参   位置形参    默认形参
def demo(a, b ,c = 3 ,d = 4):
    print(a)  # 1
    print(b)  # 2
    print(c)  # 5
    print(d)  # 6


demo(1,2,5,6)

















































