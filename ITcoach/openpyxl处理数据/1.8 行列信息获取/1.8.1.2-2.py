# import openpyxl
# wb=openpyxl.load_workbook('test.xlsx')
# ws=wb.worksheets[0]
# for col in list(ws.columns)[1:]:
# #     l=[v.value for v in col]
#     print(l[0],max(l[1:]))

import openpyxl

wb = openpyxl.load_workbook("test.xlsx")
ws = wb.active

# print([[l.value for l in col] for col in list(ws.columns)[1:]])

for col in list(ws.columns)[1:]:
    l = [v.value for v in col]
    print(l[0],max(l[1:]))
    print("%s最大值：%d" %(l[0],max(l[1:])))












