"""
汇总内贸和外贸销售订单
"""
import openpyxl

path_demostic = r"sale_order\0615\机器订单_2020-06-15.xlsx"
wb_demostic = openpyxl.load_workbook(path_demostic, data_only=True)
for s in wb_demostic.worksheets:
    if s.title == "未发汇总":
        ws = wb_demostic["未发汇总"]
title = list(ws.values)[0]
article_number = title.index("品号")    # 品号的索引号
quantity = title.index("(数量)")        # 数量的索引号
demostic_dict = {}                      # 定义字典存放数据
for rw in [[col for col in row] for row in list(ws.values)[1:]]:
    if rw[0] == "未发":
        demostic_dict[rw[article_number]] = rw[quantity]
print(demostic_dict)
# 直接把字典key转为set集合
print(set(demostic_dict))
