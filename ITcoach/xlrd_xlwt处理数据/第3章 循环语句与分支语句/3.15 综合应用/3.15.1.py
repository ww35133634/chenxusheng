import xlrd
from xlutils.copy import copy
wb=xlrd.open_workbook('业绩表.xls')
ws=wb.sheet_by_name('Sheet1')
nwb=copy(wb)
nws=nwb.get_sheet('统计结果')
subtotal=0
for r in range(1,ws.nrows):
    for c in range(1,13):
        subtotal+=ws.cell_value(r,c)
        if subtotal>=1000:
            nws.write(r,0,ws.cell_value(r,0))
            nws.write(r,1,'%d月'%c)
            nws.write(r,2,subtotal)
            break
    subtotal=0
nwb.save('业绩表.xls')