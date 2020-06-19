import xlrd
from xlutils.copy import copy
wb=xlrd.open_workbook('业绩表.xls')
ws=wb.sheet_by_name('数据')
nwb=copy(wb)
nws=nwb.get_sheet('数据')
r=0;l=[]
while r<ws.nrows-1:
    r+=1
    l+=[ws.row_values(r)]
l.sort(key=lambda x:int(x[1].split(':')[1]),reverse=False)
n=0
for v in l:
    n+=1
    nws.write(n,4,v[0])
    nws.write(n,5,v[1])
nwb.save('业绩表.xls')