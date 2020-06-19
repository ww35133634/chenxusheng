import xlrd
wb=xlrd.open_workbook('销售表.xls')
ws=wb.sheet_by_name('Sheet1')
r=0;d=dict()
while r<ws.nrows-1:
    key=ws.cell_value(r,0)
    val=ws.cell_value(r,1)
    d[key]=val
    r+=1
print(d)
