import xlrd, xlwt

wb = xlrd.open_workbook('成绩表.xls')
ws = wb.sheet_by_name('分数表')
nwb = xlwt.Workbook(encoding='uft-8')
nws = nwb.add_sheet('Sheet1')
col = ws.col_values(0)
n = 0
for c in col:
    nws.write(n, 0, c[:3])
    nws.write(n, 1, c[4:])
    nws.write(n, 2, ws.cell_value(n, 1))
    n += 1
nwb.save('结果表.xls')
