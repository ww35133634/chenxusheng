"""
列表的增删改查
"""


"""增加数据"""
# list1 = [1,2,3,4,5]
#
# # append 追加数据
# list1.append(6) # 追加到列表的最后
# print("演示append追加的用法:",list1)
#
# #insert 插入
# list1.insert(0,0) #(索引,数据)
# print("演示insert插入的用法:",list1)
#
# # extend 可以将两个列表进行合并
# list2 = [7,8,9]
# list1.extend(list2)
# print("演示extend列表合并的用法:",list1)


"""删除数据"""
# list1 = [1,2,3,4,5]
#
# # del >>> 精准删除, 索引
# del list1[4]
# print("演示del精确索引删除的用法:",list1)
#
# # pop >>> append 删除最后一个数据
# list1.pop()
# print("演示pop删除最后一个数据的用法:",list1)
#
# list1.pop(1)
# print("演示pop精确删除的用法:",list1)
#
# # 清楚列表所有数据>>> clear
# list1.clear()
# print("演示clear的用法",list1)
#
# # remove 删除第一个出现的指定数据..
# list1 = [1,2,3,4,5,1,2]
# list1.remove(1)
# print("演示remove的用法:",list1)


"""修改列表"""
# 列表[索引] = 值
# list1 = [1,2,3,4,5]
# list1[2] = 2
# print("修改数据的演示:",list1)


"""查询列表"""
# 统计,
# list1 = [1,2,3,4,5,1,1,2,2,6,3,5,1,2]
# # 列表里面数据的个数
# a = len(list1)
# print("列表里面一共有多少个数据:",a)
# # list1.__len__()
# #count用来统计特定数据的个数
# b = list1.count(2)
# print("1在列表里面一共有多少个:",b)


# 排序
list1 = [1,2,5,4,3,6]
# list1.reverse()
# print("演示reversr反转:",list1)
#
# # 从小到大的排序>>>升序 sort()
# list1.sort()
# print("使用sort进行升序排序:",list1)
# list1.sort(reverse = True)
# print("降序:",list1)


#从大到小的排序>>>反转 reverse
# list1.reverse()
# print("使用reverse进行降序排序:",list1)



