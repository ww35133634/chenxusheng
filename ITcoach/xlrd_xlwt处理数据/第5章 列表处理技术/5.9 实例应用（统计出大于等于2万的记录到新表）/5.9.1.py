import xlrd,xlwt
wb=xlrd.open_workbook('2018年业绩表.xls')
nwb=xlwt.Workbook(encoding='uft-8');nws=nwb.add_sheet('筛选结果')
n=0
for ws in wb.sheets():
    col0=ws.col_values(0)[1:]
    col1=ws.col_values(1)[1:]
    l=[[x,y] for x,y in zip(col0,col1) if y>=20000]
    for l1 in l:
        n+=1
        nws.write(n,0,ws.name)
        nws.write(n,1,l1[0])
        nws.write(n,2,l1[1])
nws.write(0,0,'月份');nws.write(0,1,'日期');nws.write(0,2,'金额')
nwb.save('筛选结果.xls')

