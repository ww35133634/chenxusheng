"""
学习numpy库
"""
import numpy as np

# arr1 = np.array([1,2,3,4])    #可以接列表或元组
# print(type(arr1))
# print(arr1)
# #
# arr1 = np.array([1,2,3,4],dtype=str)   #可指定生成数据类型
# print(arr1)
#
# arr2 = np.arange(1,10,2)    #类似python中range 前闭后开  迭代器
# print(arr2)
#
# arr3 = np.linspace(1,11,5,endpoint=True)   #生成等差数组,endpoint=True 包含结束值 11
# print(arr3)
#
# arr4 = np.zeros([4,5])   #生成4行5列 值为0 的二维数组
# arr5 = np.zeros(4)       #生成1行 4个值为0 的一维数组
# print(arr4)
# print(arr5)
#
# arr6 = np.ones([4,5])    #生成4行5列 值为0 的二维数组
# print(arr6)
# arr7 = arr6 + 1.5        #对arr6内的数据分别增加1.5
# print(arr7)
#
# # 判断数组的维度
# print(arr7.ndim)      #返回值是 2   表示二维数组
# print(arr7.shape)     #返回值是(4,5)  表示4行5列
# print(arr5.shape)     #返回值是(4,)   表示一维数组
# print(arr7.size)      #返回值是20  表示数组内的元素个数
# print(arr7.dtype)     #返回数组的类型

#数组的读取
# tuple01 = ((4,5,6,7),(5,6,7,8),(1,2,3,8))
# arr8 = np.array(tuple01)     #用元组生产数组
# print(arr8)
#读取数组内1--2行（左闭右开）
# arr9 = arr8[0:2]
# print(arr9)
# 读取单个元素（本例读取  数组内 第三行，第三列对应的数值）
# arr10 = arr8[2,2]
# arr10 = arr8[2][2]
# print(arr10)
# 读取数组内2-3列（左闭右开）
# arr11 = arr8[:,2]   #读取单列数据
# print(arr11)
# arr12 = arr8[:,1:3] #读取多列数据
# print(arr12)

# numpy内的函数
#一维数组的排序
# s = np.array([1, 3, 85, 45, 25, 362, 45, 8, 6, 7, 564])
# print(s)
# arr_sort = np.sort(s)  # 升序排列
# print(arr_sort)
# arr_reverse = sorted(s, reverse=True)  # 用python函数对数组降序排列,在numpy不能进行降序排列
# print(arr_reverse)
# arr1 = np.argsort(s)  # 返回排序后，元素在数组的之前索引
# print(arr1)
#二维数组的排序
# arr1 = np.array([[1,5,6,4],[12,52,5,3],[-1,5,-8,9]])
# print(arr1)
# # axis 官方的说法，1表示横轴，方向从左到右；0表示纵轴，方向从上到下。
# # 当axis=1时，数组的变化是横向的，而体现出来的是列的增加或者减少。
# # arr2 = np.concatenate([arr1,arr1],axis=1)       #横向 数组增加
# # print(arr2)
# # arr3 = np.concatenate([arr1,arr1],axis=0)       #竖向 数组增加
# # print(arr3)
# # 排序
# arr4 = np.sort(arr1,axis=0)     #竖向
# print(arr4)
# arr5 = np.sort(arr1,axis=1)     #横向
# print(arr5)
# arr6 = np.sort(arr1)
# print(arr6)
#
# s = np.array([1, 3, 85, 45, 25, 362, 45, 8, 6, 7, 564])
# # arr1 = np.where(s > 45,1,-1)   #数组s内大于45的赋值1，否则赋值-1
# arr1 = np.where(s > 45, s, -1)  # 数组s内大于45的赋值s的元素，否则赋值-1
# print(arr1)
#
# arr2 = np.extract(s>45,s)  #筛选出满足条件的元素。
# print(arr2)
