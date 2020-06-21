import xlrd,xlwt
wb=xlrd.open_workbook('2018年业绩表.xls')
nwb=xlwt.Workbook(encoding='uft-8');nws=nwb.add_sheet('筛选结果')
r=0
for ws in wb.sheets():
    col=ws.col_values(1)[1:]
    l=[str(int(amount)) for amount in col if amount>=20000]
    nws.write(r,0,ws.name)
    nws.write(r,1,'\\'.join(l))
    r+=1
nwb.save('筛选结果.xls')