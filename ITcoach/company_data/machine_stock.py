import pymysql
import pymssql
mysql = pymssql.connect("192.168.21.211","Warehouse Department","CXS","YF_YRONG")
cursor = pymssql.cursor()

board_materials_info = "select distinct 品号 from Y_Unaudited_PURTH where 进货日期 >= '20190101'and (供应商简称 like '%博源%'or 供应商简称 like '%汉森%')"   #提取 品号信息
# sql = "Select 单据日期,工单单别+char(45)+工单单号 as 工单信息,'20'+ substring(工单单号,3,4) as 工单月份,ltrim(rtrim(材料品号)) as 品号,品名,领料数量 from Y_MOCTC_TE_OUT_IN where 单据日期 >= 20200501 and 材料品号 in (" & board_materials_info & ") and 仓库 = '110' order by 单据日期,材料品号"

cursor.execute(board_materials_info)
results = cursor.fetchall()
print(results)

