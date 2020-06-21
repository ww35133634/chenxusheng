import xlrd
from xlutils.copy import copy
wb=xlrd.open_workbook('招生表.xls')
nwb=copy(wb)
nws1=nwb.add_sheet('上海分校')
nws2=nwb.get_sheet(1)
nws3=nwb.get_sheet('黄河分校')
nws3.write(5,7,'我来也')
nws1.write(0,0,'上海上海')
nwb.save('招生表.xls')
