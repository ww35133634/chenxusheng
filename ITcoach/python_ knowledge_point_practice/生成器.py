"""
生成器是一个特殊的迭代器
生成器的两种形式：
1、列表推导式
2、函数内拥有yield,成为生成器模板
"""
# # 1、列表推导式内存放的是具体的数
# print([i for i in range(1, 10)])  # 列表推导式
# # 生成器  >>>  存放生成数据的代码
# print((i for i in range(1, 10)))  # 生成器
# for x in (i for i in range(1, 10)):
#     print(x,end="\t")


# # 2、使用生成器来完成斐波那契数列，函数内有yield就不再是函数，是生成器模板。
"""
1,1,2,3,5,8,13
第一个数据取自第一组的第二个数据, 第二个数据取自第一组两个数据的相加
"""


def fei_bo(n):
    a, b = 0, 1
    i = 0   # 循环变量
    while i < n:
        yield a
        a, b = b, a + b
        i += 1


data = fei_bo(6)
print(data)
for i in data:
    print(i, end="\t")


"""
生成器对象既没有 __iter__ __nxet__  却可以使用for循环迭代取值>>> 特殊的迭代器
取值利用的是  for 里面调用next()函数
"""

"""
yield的特点
1.可以将数据返回出来
2.返回出来之后,,,回暂停挂起
3.下一次使用next()启动,,从哪里暂停,,代码从哪里开始
"""

# 3、函数方法 和 生成器 对比，生成器存放的是数列，函数返回的是数值。


def fei_bo2(n):
    a, b = 0, 1
    i = 0  # 循环变量
    while i < n:
        num = a
        a, b = b, a + b
        i += 1
    return num


print()
data2 = fei_bo2(6)
print(data2)
