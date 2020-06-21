import xlrd
wb=xlrd.open_workbook('蔬菜统计表.xls')
ws=wb.sheet_by_name('Sheet1')
r=0;d={}
while r<ws.nrows-1:
    r+=1
    item=ws.row_values(r)[1:]
    if item[0] in d.keys():
        d[item[0]]+=item[1]
    else:
        d[item[0]]=item[1]
print(d)