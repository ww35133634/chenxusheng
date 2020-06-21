import xlrd,xlwt
wb=xlrd.open_workbook('成绩表.xls')
ws=wb.sheet_by_name('分数表')
nwb=xlwt.Workbook(encoding='utf-8')
nws=nwb.add_sheet('筛选结果')
n,m=0,0
while n<ws.nrows-1:
    n+=1
    if ws.cell_value(n,1)>=80 and ws.cell_value(n,2)>=80:
        m+=1
        nws.write(m,0,ws.cell_value(n,0))
        nws.write(m,1,ws.cell_value(n,1))
        nws.write(m,2,ws.cell_value(n,2))
nws.write(0,0,'姓名')
nws.write(0,1,'语文')
nws.write(0,2,'数学')
nwb.save('筛选结果.xls')
