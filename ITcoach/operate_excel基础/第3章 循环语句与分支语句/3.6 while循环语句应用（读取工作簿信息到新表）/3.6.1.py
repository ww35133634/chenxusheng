import xlrd,xlwt
wb=xlrd.open_workbook('招生表.xls')
nwb=xlwt.Workbook(encoding='uft-8')
nws=nwb.add_sheet('统计表')
n=0
while n<wb.sheets().__len__():
    nws.write(n,0,'第%d个表'%(n+1))
    nws.write(n,1,wb.sheets()[n].name)
    n+=1
nwb.save('统计结果.xls')