import xlwt
y,m=2015,1
while y<=2018:
    nwb=xlwt.Workbook(encoding='uft-8')
    while m<=12:
        nwb.add_sheet('%d年%d月'%(y,m))
        m+=1
    nwb.save('%d年.xls'%y)
    y+=1
    m=1

