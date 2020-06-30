"""
演示字典
"""
# 字典是一个可变类型  id(字典)不会发生改变
#        键名 值   键名 值  键名 值
# dict1 = {'a':'a1','b':'b1','c':'c1'}
# print(dict1)
# print(id(dict1))
# 单个数据
# print(dict1['b'])


# dict1 = {'a':'a1','b':'b1','c':'c1'}
#
# print(dict1)
# print(id(dict1))
# # 修改数据
# print('*' * 50)
# print(dict1)
# print(id(dict1))
# dict1['c'] = 'c2'
# print(dict1)
# print(id(dict1))


# 不存在的键名,,会发生说明情况
# list1 = [1,2,3]
# print(list1[5])
# dict1 = {'a':'a1','b':'b1','c':'c1'}
# print(dict1)
#
# # 修改不存在的键名 >>> 字典会在最后加上新的键值对
# dict1['d'] = 'd1'
# print(dict1)



# 字典for循环取值

dict1 = {'a':'a1','b':'b1','c':'c1'}
for i in dict1:
    print(i,end=',')  # 得到的就是键名
    print(dict1[i])
    # print()



























































































