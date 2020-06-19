import xlrd
from xlutils.copy import copy
#-------------------------------
def level(num,l1,l2,l3,l4):
    if num>=l1:
        l='优'
    elif num>=l2:
        l='良'
    elif num>=l3:
        l='中'
    elif num>=l4:
        l='差'
    return l
#-------------------------------
wb=xlrd.open_workbook('分数表.xls')
ws=wb.sheet_by_name('信息表')
nwb=copy(wb);nws=nwb.get_sheet('信息表')
r=0
for c in ws.col_values(1)[1:]:
    r+=1
    nws.write(r,2,level(c,90,85,70,0))
nwb.save('分数表.xls')