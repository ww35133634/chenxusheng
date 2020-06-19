import xlrd
from xlutils.copy import copy
wb=xlrd.open_workbook('成绩表.xls')
ws=wb.sheet_by_name('分数表')
nwb=copy(wb)
nws=nwb.get_sheet('分数表')
n=0
while n<ws.nrows-1:
    n+=1
    subtotal=ws.cell_value(n,1)+ws.cell_value(n,2)
    if subtotal>=180:
        nws.write(n,3,'优')
    elif subtotal>=160:
        nws.write(n,3,'良')
    elif subtotal>=120:
        nws.write(n,3,'中')
    else:
        nws.write(n,3,'差')
nwb.save('成绩表.xls')