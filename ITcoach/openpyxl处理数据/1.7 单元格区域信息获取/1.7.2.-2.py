# import openpyxl
# wb=openpyxl.load_workbook('test.xlsx')
# ws=wb.active
# print(['%s-%d'%(row[0],sum(row[1:])) for row in list(ws.values)[1:]])

import openpyxl

wb = openpyxl.load_workbook("test.xlsx")
ws = wb.worksheets[0]
# name = [row[0] for row in list(ws.values)[1:]]
# result = [sum(row[1:]) for row in list(ws.values)[1:]]
# for n,r in zip(name,result):
#     print("%s-%d"%(n,r))
#
# print(["%s-%d" %(row[0],sum(row[1:])) for row in list(ws.values)[1:]])



