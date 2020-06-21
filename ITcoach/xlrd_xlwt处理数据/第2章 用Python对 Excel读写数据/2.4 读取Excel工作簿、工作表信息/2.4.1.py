import xlrd
wb=xlrd.open_workbook('招生表.xls')
ws=wb.sheets()
wsname=wb.sheet_names()
ws1=wb.sheet_by_name('中山分校')
ws2=wb.sheet_by_index(0)
ws3=wb.sheets()[0]
print(ws3.name)