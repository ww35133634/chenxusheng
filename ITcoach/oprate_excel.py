import pandas as pd
import openpyxl
path = r"C:\Users\CXS\Desktop\cj.xlsx"
cj = pd.read_excel(path)
print(cj)
temp = cj[["平时1","平时2","平时3","平时4","平时5"]]   #取需要计算的列
print(temp)
row_mean = temp.mean(axis=1)  #计算平均值
cj['平均成绩'] = temp.mean(axis=1) #平均成绩写入到cj表中
print(cj)
cj.sort_values(by='平均成绩',inplace=True,ascending=False) #以平均成绩进行降序排序，ascending：False为降序，True为升序
print(cj)
with pd.ExcelWriter('newcjavg.xlsx') as writer:
    cj.to_excel(writer,sheet_name=str(0))