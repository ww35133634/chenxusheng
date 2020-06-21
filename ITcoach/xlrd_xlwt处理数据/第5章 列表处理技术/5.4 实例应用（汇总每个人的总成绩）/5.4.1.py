import xlrd
from xlutils.copy import copy
wb=xlrd.open_workbook('成绩统计表.xls')
ws=wb.sheet_by_name('成绩')
nwb=copy(wb);nws=nwb.get_sheet('Sheet2')
col=ws.col_values(1)[1:]
subtotal,n=0,0
for v in col:
    for score in v.split('-')[1::2]:
        subtotal+=int(score)
    n+=1
    nws.write(n,0,ws.cell_value(n,0))
    nws.write(n,1,subtotal)
    subtotal=0
nwb.save('成绩统计表.xls')
