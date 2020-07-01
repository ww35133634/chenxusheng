# import xlrd,xlwt
# wb=xlrd.open_workbook('业绩表.xls')
# ws=wb.sheet_by_name('Sheet1')
# nwb=xlwt.Workbook(encoding='utf-8');nws=nwb.add_sheet('Sheet1')
# l=[ws.col_values(0),ws.col_values(1),ws.col_values(3)]
# l1=zip(*l)
# d=dict.fromkeys(l1)
# r=0
# for k in d:
#     nws.write(r,0,k[0])
#     nws.write(r,1,k[1])
#     nws.write(r,2,k[2])
#     r+=1
# nwb.save('结果表.xls')

import xlrd,xlwt
from xlutils.copy import copy

wb = xlrd.open_workbook("业绩表.xls")
ws = wb.sheet_by_name("Sheet1")
nwb = copy(wb)
nws = nwb.add_sheet("去重")
# nwb = xlwt.Workbook(encoding="utf-8")
# nws = nwb.add_sheet("Sheet1")
d = dict.fromkeys(zip(*[ws.col_values(0), ws.col_values(1), ws.col_values(3)]))
print(list(d))
r = 0
for k in d:
    print(k)
    nws.write(r, 0, k[0])
    nws.write(r, 1, k[1])
    nws.write(r, 2, k[2])
    r += 1
nwb.save("业绩表.xls")
