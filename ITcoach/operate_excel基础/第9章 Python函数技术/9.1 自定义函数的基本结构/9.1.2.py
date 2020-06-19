import xlrd
from xlutils.copy import copy
#-------------------------------------
def age(id,dit):
    l=[id[x:y] for x,y in ((6,10),(10,12),(12,14))]
    date=dit.join(l)
    return date
#-------------------------------------
wb=xlrd.open_workbook('用户信息.xls')
ws=wb.sheet_by_name('信息表')
nwb=copy(wb);nws=nwb.get_sheet('信息表')
r=0
while r<ws.nrows-1:
    r+=1
    nws.write(r,2,age(ws.cell_value(r,1),'-'))
nwb.save('用户信息.xls')