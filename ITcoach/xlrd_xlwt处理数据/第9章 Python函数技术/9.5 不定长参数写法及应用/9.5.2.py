import xlrd
from xlutils.copy import copy
#----------------------------------
def substitute(txt,*repl):
    for x,y in repl:
        txt=txt.replace(x,y)
    return txt
#----------------------------------
wb=xlrd.open_workbook('成绩表.xls')
ws=wb.sheet_by_name('分数表')
nwb=copy(wb)
nws=nwb.get_sheet('分数表')
n=0
while n<ws.nrows-1:
    n+=1
    c=ws.cell_value(n,1)
    val=substitute(c,('、','\n'),('[','('),(']',')'),('：','-'))
    nws.write(n,2,val)
nwb.save('成绩表.xls')