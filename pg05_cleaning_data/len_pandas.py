"""
 学习pandas库
"""
import pandas as pd
import numpy as np
# #1、Series 一维数组
# s = pd.Series([0,1,2,3],index=["a","b","c","d"])  #一维数组
# print(s)
# #
# d={"a":1,"b":2,"c":3}    #用字典创建一维数组，key 作为索引，value 作为值
# s2=pd.Series(d)
# print(s2)
# s3 =s2["a"]   #索引
# print(s3)
# # s4 = s2[:2]   #切片
# s4 = s2["a":"b"]
# print(s4)
# s5 = s2.values #输出序列的值
# print(s5)
# s6 = s2.index
# print(s6)
#2、DataFrame 二维数组
# list01 = [["Tom",30],["Emma",27],["Sean",29]]    #使用列表创建数组
# d1 = pd.DataFrame(list01,columns=["name","age"]) #columns 列名
# print(d1)
#
dic = {"name":["Tom","Emma","Sean"],"age":[30,27,29]}  #使用字典创建数组
d2 = pd.DataFrame(dic)
print(d2)

arr01 = np.array([["Tom",30],["Emma",27],["Sean",29]])   #使用数组创建
d3 = pd.DataFrame(arr01,columns=["name","age"],index=['a','b','c'])
print(d3)

d4 = pd.DataFrame(np.random.randn(6,4),columns=["a","b","c","d"])  #用随机数创建6行4列数组
print(d4)

print(d3.values)  #返回d3的值
print(d3.index)   #返回d3的索引号
print(d3.columns.tolist())  #返回d3的列名到列表
print(d3.shape)   #返回d3的形状
print(d3.size)    #返回d3的元素个数
print(d3.ndim)    #返回d3的维度
print(d3.dtypes)  #返回d3的数据类型