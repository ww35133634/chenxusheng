import xlrd
from xlutils.copy import copy
#------------------------------------------------
def agg(list,delimiter,num=1,subtotal=sum):
    l = [int(x.split(delimiter)[num]) for x in list]
    return subtotal(l)
#------------------------------------------------

wb=xlrd.open_workbook('2018年业绩表.xls')
ws=wb.sheet_by_name('2018业绩表')
nwb=copy(wb);nws=nwb.get_sheet('2018业绩表')
r=0
while r<ws.nrows-1:
    r+=1
    l=ws.row_values(r)[1:-1]
    nws.write(r,6,agg(delimiter=',',list=l))
nwb.save('2018年业绩表.xls')