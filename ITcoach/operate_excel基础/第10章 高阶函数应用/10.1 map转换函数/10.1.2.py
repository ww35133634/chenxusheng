import xlrd,xlwt
wb=xlrd.open_workbook('业绩表.xls')
nwb=xlwt.Workbook(encoding='utf-8')
nws=nwb.add_sheet('结果')
#---------------------------------
def counter(list):
    return len([x for x in list if x>=100])
#---------------------------------
n=0
for s in wb.sheets():
    n+=1
    nws.write(n,0,s.name)
    l=s.col_values(1)[1:]
    nws.write(n,1,list(map(counter,[l]))[0])
nws.write(0,0,'月份')
nws.write(0,1,'计数')
nwb.save('统计结果1.xls')