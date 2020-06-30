"""
演示函数间的调用
"""
# 是不是两个数的求和
# def demo1(a,b):
#     return a + b
#
# def demo2(f,g):  # 得到两个数字的评价值
#     d = demo1(f,g)  # 可以方便拿到另一个函数的功能  执行demo1里面的代码,执行完之后代表返回值
#     return d // 2  # 5
#
# # 表面上只调用一个函数, 但是两个函数都被运行才能得到结果
# # 一点都不灵活  可以求导任意两个数的平均值
# e = demo2(4,6)  # 1 执行函数内部代码,执行完之后代表返回值 5
# print(e)





# 函数内部所有的数据,,没有一个是写死,, 最大的灵活性
def demo1(a,b):
    return a + b

def demo2(f,g,h):
    d = demo1(f,g)
    return d // h


e = demo2(4,6,2)
print(e)















































































