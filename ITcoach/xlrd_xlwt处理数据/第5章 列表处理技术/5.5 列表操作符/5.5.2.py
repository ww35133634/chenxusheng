import xlrd
from xlutils.copy import copy
wb=xlrd.open_workbook('值班表.xls');ws=wb.sheet_by_name('值班表')
nwb=copy(wb);nws=nwb.get_sheet('值班表')
row_count=ws.nrows-1
n=0
while n<row_count:
    n+=1
    if '岳成周' in ws.row_values(n)[1:-1]:
        nws.write(n,6,'√')
    else:
        nws.write(n,6,'×')
nwb.save('值班表.xls')
