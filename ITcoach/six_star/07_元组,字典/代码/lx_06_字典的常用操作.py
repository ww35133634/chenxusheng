"""
演示字典的操作
"""

# dict1 = {"a":"a1","b":"b1","c":"c1"}
# 根据键名取值
# print(dict1["d"])
# get(), 即使健名不存在,,也会返回None,,不会报错影响程序的执行
# print(dict1.get("d"))

# dict1 = {"a":"a1","b":"b1","c":"c1"}
# 删除 pop 去删除指定的键值对,,拿到该键值对的值
# a = dict1.pop("a")
# print(a)
# print(dict1)

#popitem 删除字典中最后一个键值对,,将他们数据拿到
# b = dict1.popitem()
# print(b)
# print(dict1)

# 添加
# dict1 = {"a":"a1","b":"b1","c":"c1"}
# # dict1["d"] = "d1"
# # print(dict1)
# # 添加键值对,, 如果健名存在,,,而是作为无效的方式存在
# # dict1.setdefault("d","d1") 健名不存在则再最后添加键值对信息
# # print(dict1)
#
# # 按住ctrl
# dict1.setdefault("a","d1") # 健名存在则视为无效语法
# print(dict1)

# 添加 一个字典添加到另一个字典,,
# dict1 = {"a":"a1","b":"b1","c":"c1"}
# dict2 = {"d":"d1","e":"e1"}
# dict1.update(dict2)
# print(dict1)

# 健名相同 会修改原有的value值
# dict1 = {"a":"a1","b":"b1","c":"c1"}
# dict2 = {"d":"d1","e":"e1","a":"a2"}
# dict1.update(dict2)
# print(dict1)


# keys()可以拿到一个列表,,列表里面是所有的健名
# dict1 = {"a":"a1","b":"b1","c":"c1"}
# # for i in dict1:
# #     print(i,end = ",")
# a = dict1.keys()
# print(a)

# 是否可以拿到所有的值,,value
# dict1 = {"a":"a1","b":"b1","c":"c1"}
# b = dict1.values()
# print(b)

# 拿出所有的键值对,,, 一个以键值对为单个元组的列表....
# dict1 = {"a":"a1","b":"b1","c":"c1"}
# print(dict1.items())

# clear 做的 就是一个大扫除的工作
dict1 = {"a":"a1","b":"b1","c":"c1"}
dict1.clear()
print(dict1)

# 就是不可修改数据的列表
# id()

