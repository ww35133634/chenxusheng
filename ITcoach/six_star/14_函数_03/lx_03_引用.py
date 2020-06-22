"""
演示引用
"""
# 数值 他是不可变类型
# a = 1 # a → 1（101） a = 2 a → 2（202）

# b = 1 # b → 1
# print(id(a))
# print(id(b))
#
# a = 1 # a → 1
# b = a # b → a → 1


# 列表是可变类型
# 演示列表
# a = [1,2,3] # a 》》》【1，2，3，4】
# a = [1,2,3,4]
#101
#  b = [1,2,3]
# print(id(a))
# print(id(b))


# a = [1,2,3] # a → 【1，2，3】
# print(a)
# print(id(a))
# a.append(4) # a →【1，2，3，4】
# print(a)
# print(id(a))


a = [1,1,1]
print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[2]))



