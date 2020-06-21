import xlrd
wb=xlrd.open_workbook('获奖名单.xls')
ws1=wb.sheet_by_name('Sheet1')
ws2=wb.sheet_by_name('统计表')
n=0;l=[]
while n<ws1.nrows-1:
    n+=1
    l+=ws1.row_values(n)[1:]
l2=[x+':'+str(l.count(x)) for x in ws2.col_values(0)[1:]]
print(l2)
