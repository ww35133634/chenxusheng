import xlrd,xlwt
wb=xlrd.open_workbook('排名表.xls')
ws=wb.sheet_by_name('名次表')
nwb=xlwt.Workbook(encoding='uft-8');nws=nwb.add_sheet('结果表')
c=0;s=set()
while c<ws.ncols-1:
    c+=1
    s.update(ws.col_values(c)[1:])
l=list(s)
for n in range(len(l)):
    nws.write(n+1,0,n+1)
    nws.write(n+1,1,l[n])
nws.write(0,0,'序号');nws.write(0,1,'姓名')
nwb.save('去重结果表.xls')

