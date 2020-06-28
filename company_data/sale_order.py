from company_data.custom_package.class_excel import Excel_Oprate
import openpyxl

# # 外贸订单
# path = r"F:\python\ITcoach\company_data\外贸订单\外贸机器订单截止_2020-6-23简洁版.xlsx"
# obj01 = Excel_Oprate(path)
# fd01 = "品号"; fd02 = "未执行数量"
# obj01.read_excel(fd01, fd02)
# obj01.get_data()
# foreign_order = obj01.data

# # 内贸订单
# path = r"F:\python\ITcoach\company_data\内贸订单\机器订单_2020-06-18.xlsx"
# obj02 = Excel_Oprate(path)
# fd01 = "品号"; fd02 = "(数量)"; fd03 = "状态"
# obj02.read_excel(fd01, fd02, fd03)
# obj02.get_data("未发")
# demostic_order = obj02.data

# # 备货计划
# path = r"F:\python\ITcoach\company_data\销售预测\2020年7月份备货计划20200619.xlsx"
# obj03 = Excel_Oprate(path, 2)
# fd01 = "整机"; fd02 = "7月备货"; fd03 = "7月备货"
# obj03.read_excel(fd01, fd02, fd03)
# obj03.get_data()
# l = [(x, y) for x, y in obj03.data.items() if x != "总计" and y != None and y != "是否"]
# predicted_plan = dict(l)
# print(predicted_plan)

# 成品机整机机架对照表

path = r"F:\python\ITcoach\company_data\成品整机机架对照表\成品整机机架对照表.xlsx"
obj04 = Excel_Oprate(path)
fd01 = "成品机品号"; fd02 = "整机品号"
obj04.read_excel(fd01,fd02)
obj04.get_data()
print(obj04.data)







