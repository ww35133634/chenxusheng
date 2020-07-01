# import xlrd
# from xlutils.copy import copy
# wb=xlrd.open_workbook('订单.xls')
# ws1=wb.sheet_by_name('全部订单')
# ws2=wb.sheet_by_name('已发货')
# nwb=copy(wb);nws=nwb.get_sheet('未发货')
# l1=[ws1.col_values(0),ws1.col_values(1),ws1.col_values(2)]
# l2=[ws2.col_values(0),ws2.col_values(1),ws2.col_values(2)]
# d1=dict.fromkeys(zip(*l1))
# d2=list(dict.fromkeys(zip(*l2)))[1:]
# for x in d2:
#     d1.pop(x)
# r=0
# for y in d1:
#     nws.write(r,0,y[0])
#     nws.write(r,1,y[1])
#     nws.write(r,2,y[2])
#     r+=1
# nwb.save('订单.xls')

import xlrd,xlwt
from xlutils.copy import copy

wb = xlrd.open_workbook("订单.xls")
ws1 = wb.sheet_by_name("全部订单")
ws2 = wb.sheet_by_name("已发货")
nwb = copy(wb)
nws = nwb.get_sheet("未发货")
ws1_list = [ws1.col_values(0), ws1.col_values(1), ws1.col_values(2)]
ws2_list = [ws2.col_values(0), ws2.col_values(1), ws2.col_values(2)]
d1 = dict.fromkeys(zip(*ws1_list))
d2 = list(dict.fromkeys(zip(*ws2_list)))[1:]
for d in d2:
    d1.pop(d)

r = 0
for c in d1:
    nws.write(r, 0, c[0])
    nws.write(r, 1, c[1])
    nws.write(r, 2, c[2])
    r += 1
nwb.save("订单.xls")





