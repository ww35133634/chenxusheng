import xlwt
nwb=xlwt.Workbook(encoding='utf-8')
nws=nwb.add_sheet('成绩表')
nws.write(1,2,'Hello!Excel我来了！')
nwb.save('成绩单.xls')