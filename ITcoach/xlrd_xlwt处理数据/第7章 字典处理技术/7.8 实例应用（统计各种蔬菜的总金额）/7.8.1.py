# import xlrd
# # wb=xlrd.open_workbook('蔬菜统计表.xls')
# # ws=wb.sheet_by_name('Sheet1')
# # r=0;d={}
# # while r<ws.nrows-1:
# #     r+=1
# #     item=ws.row_values(r)[1:]
# #     if item[0] in d.keys():
# #         d[item[0]]+=item[1]
# #     else:
# #         d[item[0]]=item[1]
# # print(d)

import xlrd, xlwt
from xlutils.copy import copy

wb = xlrd.open_workbook("蔬菜统计表.xls")
ws = wb.sheet_by_index(0)
nwb = copy(wb)
nws = nwb.add_sheet("汇总")
d = dict()
for c, v in zip(ws.col_values(1, 1), ws.col_values(2, 1)):
    if c in d.keys():
        d[c] += v
    else:
        d[c] = v
r = 0
for k, v in d.items():
    print(k, v)
    nws.write(r, 0, k)
    nws.write(r, 1, v)
    r += 1
nwb.save("ss.xls")





