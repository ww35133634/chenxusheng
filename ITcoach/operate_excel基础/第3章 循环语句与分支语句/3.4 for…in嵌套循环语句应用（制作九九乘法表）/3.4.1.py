import xlwt
wb=xlwt.Workbook(encoding='utf-8')
ws=wb.add_sheet('乘法表')
for x in range(1,13):
    for y in range(1,x+1):
        ws.write(x-1,y-1,'%d×%d=%d'%(x,y,x*y))
wb.save('九九乘法表.xls')