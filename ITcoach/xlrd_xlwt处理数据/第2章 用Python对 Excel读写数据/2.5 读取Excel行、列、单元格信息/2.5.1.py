import  xlrd
ws=xlrd.open_workbook('招生表.xls').sheet_by_name('中山分校')
crow=ws.nrows
ccol=ws.ncols
row_data=ws.row_values(3)
col_data=ws.col_values(1)
cell_data_1=ws.cell_value(2,1)
cell_data_2=ws.cell(1,3).value
print(cell_data_2)