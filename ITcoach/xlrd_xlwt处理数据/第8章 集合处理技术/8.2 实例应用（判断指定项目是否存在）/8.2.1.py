import xlrd
from xlutils.copy import copy
wb=xlrd.open_workbook('兴趣班报名表.xls')
ws=wb.sheet_by_name('Sheet1')
nwb=copy(wb);nws=nwb.get_sheet('Sheet1')
r=0
while r<ws.nrows-1:
    r+=1
    v=ws.cell_value(r,1)
    s=set(v.split('、'))
    if s=={'钢琴', '书法', '武术', '绘画'}:
        nws.write(r,2,'√')
    else:
        nws.write(r,2,'×')
nwb.save('兴趣班报名表.xls')