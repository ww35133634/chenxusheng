"""
汇总内贸和外贸销售订单
"""
import openpyxl

# """内贸订单数据"""
path_demostic = r"sale_order\0615\机器订单_2020-06-15.xlsx"
wb_demostic = openpyxl.load_workbook(path_demostic, data_only=True)
wb_demostic_ws = wb_demostic["未发汇总"]
wb_demostic_title = list(wb_demostic_ws.values)[0]
demostic_article_number = wb_demostic_title.index("品号")    # 内贸订单品号的索引值
demostict_quantity = wb_demostic_title.index("(数量)")        # 内贸订单数量的索引值
demostic_order_dict = {}       # 定义字典存放内贸数据
for row in list(wb_demostic_ws.values)[1:]:
    if row[0] == "未发":
        demostic_order_dict[str(row[demostic_article_number])] = row[demostict_quantity]
# print(demostic_order_dict)
"""外贸订单数据"""
path_foreign = r"sale_order\0615\外贸机器订单截止_2020-6-16简洁版(1).xlsx"
wb_foreign = openpyxl.load_workbook(path_foreign, data_only=True)
wb_foreign_ws = wb_foreign.active
wb_foreign_title = list(wb_foreign_ws.values)[0]
foreign_article_number = wb_foreign_title.index("品号")  # 外贸订单品号的索引值
foreign_quantity = wb_foreign_title.index("未执行数量")   # 外贸订单数量的索引值
print(foreign_article_number,foreign_quantity)

foreign_order_dict = {}         # 定义字典存放内贸数据
for row in list(wb_foreign_ws.values)[1:]:
    if row[foreign_article_number] != None:
        foreign_order_dict[str(row[foreign_article_number])] = row[foreign_quantity]
# print(foreign_order_dict)

# 直接把字典key转为set集合
# # print(set(demostic_dict))

# 成品机和整机对照表
# comparison_table = openpyxl.load_workbook("comparison table.xlsx")
# comparison_table_ws = comparison_table.active
# comparison_table_title = list(comparison_table_ws.values)[0]
# comparison_finished_article = comparison_table_title.index("成品机品号")
# comparison_unfinshed_article = comparison_table_title.index("整机品号")
# comparison_dict = {}         # 定义字典存放对照表数据
# for row in list(comparison_table_ws.values)[1:]:
#     # print(row)
#     if row[comparison_finished_article] != None:
#         comparison_dict[str(row[comparison_finished_article])] = row[comparison_unfinshed_article]
#     else:
#         comparison_dict[str(row[comparison_unfinshed_article])] = row[comparison_unfinshed_article]
# print(comparison_dict)






