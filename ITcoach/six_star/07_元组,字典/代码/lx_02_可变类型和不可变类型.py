"""
演示可变类型和不可变类型
"""

# id() 内存地址  新的空间>>>保存数据,,内存地址,,
# 可变类型  新的空间>>>123 append pop
# 不可变类型  新的空间>>>321 322

list1 = [1,2,3]
print("list1的定义时候的内存地址是:",id(list1))
tuple1 = (1,2,3)
print("tuple1的定义时候的内存地址是:",id(tuple1))

# 修改操作
list1.append(4)
print(list1)
print("list1增加数据之后的内存地址是:",id(list1))
tuple1 = (1,2,3,4)
print(tuple1)
print("tuple1增加数据之后的内存地址是:",id(tuple1))





