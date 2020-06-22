"""
演示切片
"""

list1 = [1,2,3,4,5,6,7,8]
# list1[开始索引:结束索引:步长]
list2 = list1[1:5:1] # 包头不包尾
print("索引的演示:",list2)

# 2 4 6
list3 = list1[1:7:2]
print("演示步长为2的效果:",list3)

#有正有反
list4 = list1[5:1:-1] # 包头不包尾
# 倒过来取
print(list4)

list1[5] >>> list1[5:6:1]



















