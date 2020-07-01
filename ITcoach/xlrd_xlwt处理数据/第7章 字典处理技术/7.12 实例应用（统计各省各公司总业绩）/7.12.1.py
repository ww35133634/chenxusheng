# import xlrd,xlwt
# wb=xlrd.open_workbook('业绩表.xls')
# ws=wb.sheet_by_name('Sheet1')
# nwb=xlwt.Workbook(encoding='uft-8')
# r=0;d={}
# while r<ws.nrows-1:
#     r+=1
#     l=ws.row_values(r)
#     if (l[0],l[1]) in d.keys():
#         d[(l[0],l[1])]+=l[5]
#     else:
#         d[(l[0],l[1])]=l[5]
# l1=dict.fromkeys([x for x,y in d.keys()]).keys()
# r=0
# for s in l1:
#     nws=nwb.add_sheet(s)
#     nws.write(0,0,'省份');nws.write(0,1,'公司名');nws.write(0,2,'总金额')
#     l2=[[x[0],x[1],y] for x,y in d.items() if x[0]==s]
#     for val in l2:
#         r+=1
#         nws.write(r,0,val[0]);nws.write(r,1,val[1]);nws.write(r,2,val[2])
#     r=0
# nwb.save('汇总表.xls')

import xlrd,xlwt

wb = xlrd.open_workbook("业绩表.xls")
ws = wb.sheet_by_index(0)


























# import openpyxl
#
# wb = openpyxl.load_workbook("业绩表.xlsx")
# ws = wb.active
# l = list(ws.values)[1:]
# d = {}
# for r in list(ws.values)[1:]:
#     if (r[0], r[1]) in d.keys():
#         d[(r[0], r[1])] += r[-1]
#     else:
#         d[(r[0], r[1])] = r[-1]
# nwb = openpyxl.Workbook()
# nwb.remove(nwb["Sheet"])
# for k in dict.fromkeys([x for x, y in d.keys()]).keys():
#     nws = nwb.create_sheet(k)
#     nws.append(["省份", "公司名", "总业绩"])
#     for l in [(x[0],x[1],y) for x,y in d.items()]:
#         if l[0] == k:
#             nws.append(l)
# nwb.save("汇总表01.xlsx")
