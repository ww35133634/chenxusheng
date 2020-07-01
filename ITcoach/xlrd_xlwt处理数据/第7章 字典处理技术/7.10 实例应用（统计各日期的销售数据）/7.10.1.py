# import xlrd
# wb=xlrd.open_workbook('销售表.xls')
# ws=wb.sheet_by_name('Sheet1')
# r=0;d=dict()
# while r<ws.nrows-1:
#     r+=1
#     key=ws.cell_value(r,0)
#     val=ws.cell_value(r,1)
#     if key in d.keys():
#         d[key]+=[val]
#     else:
#         d[key]=[val]
# print(d)
# for k in d:
#     print(k,[sum(d[k]),max(d[k]),min(d[k]),len(d[k])])


import xlrd

wb = xlrd.open_workbook("销售表.xls")
ws = wb.sheet_by_index(0)
r = 0
d = {}
while r < ws.nrows-1:
    r += 1
    key = ws.cell_value(r, 0)
    val = ws.cell_value(r, 1)
    if key in d.keys():
        d[key] += [val]
    else:
        d[key] = [val]
print(d)
for k in d.keys():
    print(k, {"和": sum(d[k]), "最大值": max(d[k]), "最小值": min(d[k]), "个数": len(d[k])})










