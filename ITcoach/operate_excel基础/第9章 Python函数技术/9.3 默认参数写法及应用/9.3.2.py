import xlrd
from xlutils.copy import copy
#------------------------------------------
def text_pos(str,delimiter,position=0):
    n=0;l=[-1]
    while n<str.count(delimiter):
        l.append(str.index(delimiter,l[-1]+1))
        n+=1
    l=l[1:]
    if position==0:
        l=l[0]
    elif position==1:
        l=l[-1]
    elif position==2:
        l=l[:]
    return l
def mid(text,start,num):
    txt=text[start:start+num]
    return txt
#------------------------------------------
wb=xlrd.open_workbook('产品信息表.xls')
ws=wb.sheet_by_name('产品表')
nwb=copy(wb);nws=nwb.get_sheet('产品表')
n=0
for c in ws.col_values(1)[1:]:
    n+=1
    ll=[mid('，'+c,x+1,6) for x in text_pos('，'+c,'，',2)]
    nws.write(n,2,'/'.join(ll))
nwb.save('产品信息表.xls')