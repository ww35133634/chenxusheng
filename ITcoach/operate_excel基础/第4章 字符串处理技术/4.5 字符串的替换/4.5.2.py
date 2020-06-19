import xlrd
from xlutils.copy import copy
wb=xlrd.open_workbook('等级表.xls')
ws=wb.sheet_by_name('Sheet1')
nwb=copy(wb)
nws=nwb.get_sheet('Sheet1')
n=0
while n<ws.nrows-1:
    n+=1
    val=ws.cell_value(n, 0)
    nws.write(n,1,val.replace('-','(',1).replace('-',')',1))
nwb.save('等级表.xls')