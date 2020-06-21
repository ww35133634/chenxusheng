import xlrd
wb=xlrd.open_workbook('等级表.xls')
ws=wb.sheet_by_name('Sheet1')
n,m=0,0
for l in '优良中差':
    while n<ws.nrows-1:
        n+=1
        c=ws.cell_value(n, 1)
        m+=c.count(l)
    print(l, m)
    n,m=0,0
