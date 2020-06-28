"""调用pymyssql连接sqlserver数据库"""

from company_data.custom_package.class_sqlserver import SQLServer

sql = "select INVMBMB001 as 品号, sum(INVMCMC007) as 数量 from YR_IM_001 where CMSMCMC002 in ('整机仓','成品仓','整机呆滞仓') group by INVMBMB001"
stock_infos = SQLServer.main(sql)
print(stock_infos)