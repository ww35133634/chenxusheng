import xlrd
from xlutils.copy import copy
wb=xlrd.open_workbook('工资表.xls');ws=wb.sheet_by_name('工资表')
nwb=copy(wb);nws=nwb.get_sheet('工资表')
n=0
for cell in ws.col_values(1)[1:]:
    l=[int(n) for n in cell.split('、')]
    l1=['总工资：', '最高工资：', '最低工资：', '月数：', '平均工资：']
    l2=[sum(l),max(l),min(l),len(l),sum(l)/len(l)]
    l3=['元','元','元','个月','元']
    l4=[x+str(y)+z for x,y,z in zip(l1,l2,l3)]
    n+=1
    nws.write(n,2,'\n'.join(l4))
nwb.save('工资表.xls')