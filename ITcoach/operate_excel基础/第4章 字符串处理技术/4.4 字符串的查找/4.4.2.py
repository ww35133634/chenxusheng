import xlrd
from xlutils.copy import copy
wb=xlrd.open_workbook('等级表.xls')
ws=wb.sheet_by_name('Sheet1')
nwb=copy(wb)
nws=nwb.get_sheet('Sheet1')
n=0
while n<ws.nrows-1:
    n+=1
    s=ws.cell_value(n,1)
    nws.write(n,2,s.count('优',s.find('\n')))
nwb.save('等级表.xls')
