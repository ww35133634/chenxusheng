import xlrd,xlwt
wb=xlrd.open_workbook('业绩达标表.xls');ws=wb.sheet_by_name('业绩')
nwb=xlwt.Workbook(encoding='uft-8');nws=nwb.add_sheet('结果')
col1=ws.col_values(0)[1:]
col2=ws.col_values(1)[1:]
s=set(zip(col1,col2))
s1={'%d月'%m for m in range(1,13)}
s2=set(col1)
r=0
for m in s2:
    s3='/'.join(s1-{y for x,y in s if m==x})
    nws.write(r,0,m);nws.write(r,1,s3)
    r+=1
nwb.save('统计结果.xls')