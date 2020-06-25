"""
输入一个1-20间的整数，就从1到这个数的阶层之和，比如输入5， 就是求：1！+ 2！+ 3！+ 4！+ 5！
 阶层功能使用函数实现
"""




import pandas as pd
import openpyxl
path = r"C:\Users\Administrator\Desktop\写真机-121804024-cleaning.xlsx"
cj = pd.read_excel(path)
print(cj)
# temp = cj[["平时1","平时2","平时3","平时4","平时5"]]   #取需要计算的列
# print(temp)
# row_mean = temp.mean(axis=1)  #计算平均值
# cj['平均成绩'] = temp.mean(axis=1) #平均成绩写入到cj表中
# print(cj)
# cj.sort_values(by='平均成绩',inplace=True,ascending=False) #以平均成绩进行降序排序，ascending：False为降序，True为升序
# print(cj)
# with pd.ExcelWriter('newcjavg.xlsx') as writer:
#     cj.to_excel(writer,sheet_name=str(0))