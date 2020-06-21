import xlrd,xlwt
wb=xlrd.open_workbook('各战队比赛名次.xls')
ws=wb.sheet_by_name('2018年各战队排名')
nwb=xlwt.Workbook(encoding='uft-8');nws=nwb.add_sheet('统计结果')
r=0
while r<ws.nrows-1:
    r+=1
    l=ws.row_values(r)
    l1=[x.split('-')[1] for x in l[1].split(',')]
    l2=[l[0],'/'.join({'%s:共%d人'%(x,l1.count(x)) for x in l1})]
    nws.write(r,0,l2[0]);nws.write(r,1,l2[1])
nwb.save('统计结果.xls')