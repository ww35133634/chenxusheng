"""
列表的操作
"""
#        0 1 2 3 4 5
# list1 = [1,2,3,4,5,6]
# 保存多个数据的容器,,

# 使用append去添加数据  并且是默认添加到最后的
# list1.append(8)  # ctrl 鼠标点击  返回值
# print(list1)

# 使用insert插入数据,,
# list1.insert(4,8)  # 插入(索引,数据)
# print(list1)

# 在列表1后面列表2
# list1 = [1,2,3,4,5,6]
# list2 = [7,8,9]
# list1.extend(list2)
# print(list1)


# pop 删除 默认最后一位
# list1 = [1,2,3,4,5,6]
# list1.pop()
# print(list1)

# 列表清空
# list1 = [1,2,3,4,5,6]
# list1.clear()
# print(list1)


# remove 删除第一个指定的数据
# list1 = [1,2,3,4,5,1]
# list1.remove(1)
# print(list1)

# len(列表)列表的长度里面有多少个数据 和count()
# list1 = [1,2,3,4,5,6]
# print(len(list1))
# list1 = [1,2,3,1,1,2,4,5]
# print(list1.count(1))


# 使用sort()排序
# list1 = [1,2,5,3,4,6]
# list1.sort()  # 进行了排序之后,,升序的效果
# print(list1)


# list1 = [1,2,5,3,4,6]
# list1.sort(reverse= True)  # 降序的效果
# print(list1)


# 列表推导式
# list1 = [for i in range(1,101)]

#  for 循环
# for i in range(1,11):  # range(1,11)包前不包后1,2,3,4,5,6,7,8,9,10
#     print(i)  # 被控制着执行次数

# 列表推导式
# 创建一个列表1-100
# list1 = [1,2,3,4,.....,100]
#        i    for循环得到数据给i
# list1 = [i for i in range(1,101)]
# print(list1)




#        i       for循环得到数据给i   只拿偶数
list1 = [i for i in range(1,101) if i % 2 == 0]
print(list1)













































