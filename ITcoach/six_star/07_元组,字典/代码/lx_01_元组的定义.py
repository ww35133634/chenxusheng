"""
元组的定义的演示
"""
# 多数据的元组
# tuple1 = (1,2,3,"hello","python",True)
# print(tuple1)

# 单数据的元组 type

# tuple2 = (2)
# print("tuple2的类型是:",type(tuple2))
# tuple3 = (2,)
# print("tuple3的类型是:",type(tuple3))


# 变量名[索引]
# tuple1 = (1,2,3,"hello","python",True)
# print(tuple1[3])

# 不能修改数据
# tuple1 = (1,2,3,"hello","python",True)
# tuple1[0] = 2

# 循环遍历
# tuple1 = (1,2,3,"hello","python",True)
# for i in tuple1:
#     print(i)

# 元组的查询
tuple1 = (1,2,3,"hello","python",True,1,1,2)
# a = tuple1.count(1)
# print(a)
a = tuple1.index(3)
print(a)