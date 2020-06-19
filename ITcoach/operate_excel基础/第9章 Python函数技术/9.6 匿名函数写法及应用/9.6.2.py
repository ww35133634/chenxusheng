import xlrd
from xlutils.copy import copy
wb=xlrd.open_workbook('员工表.xls')
ws=wb.sheet_by_name('信息')
nwb=copy(wb);nws=nwb.get_sheet('信息')
n=0
for c in ws.col_values(1)[1:]:
    n+=1
    sex=(lambda id:'男' if int(id[-2])%2==1 else '女')(c)
    nws.write(n,2,sex)
nwb.save('员工表.xls')