"""
演示循环遍历
"""

# list1 = [1,2,3,4,5]
# for i in list1: #遍历 # 多少个数据决定他的次数
#     print(i)

# 将一百以内所有的偶数放进一个列表
list1 = []
for i in range(101):# range(101)>>0-100
    if i % 2 == 0:
        list1.append(i) # 将偶数添加到列表list1
print(list1)

# 列表推导式 #
list1 = [i for i in range(1,101) if i % 2 != 0]
print(list1)



















