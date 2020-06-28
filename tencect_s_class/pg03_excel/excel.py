"""
python 操作 Excel
"""
import xlrd
import xlwt



# #读取Excel文件
# workbook = xlrd.open_workbook(filename)
# #获取所有表名
# sheet_names = workbook.sheets()
#
# # #通过索引顺序获取一个工作表
# sheet0 = workbook.sheets()[0]
# # # or
# sheet1 = workbook.sheet_by_index(1)
# # #通过表名获取一个工作表
# sheet3 = workbook.sheet1
# # for i  in sheet_names:
# print(sheet3)



def read_xlrd(excelTestFile):
    data = xlrd.open_workbook(excelTestFile)  # 打开路径下的文件，并读取
    table = data.sheet_by_index(0)  # 根据sheet的索引，确定表格；也可以根据sheet名称确定，如：table = data.sheet_by_name('用户表')
    for rowNum in range(table.nrows):  # excel表格中的有效行数，从0开始
        rowVale = table.row_values(rowNum)  # row_values返回该行中所有数据组成的一个列表
        for colNum in range(table.ncols):  # excel表格中的有效列数，从0开始
            if rowNum > 0 and colNum == 0:
                print(int(rowVale[0]))
            else:
                print(rowVale[colNum])
        print("#############################")
if __name__ == '__main__':
    excelFile =  r"C:\Users\CXS\Desktop\公司文件\机架信息.xlsm"
    read_xlrd(excelTestFile=excelFile)