"""
汇总内贸和外贸销售订单
"""
import openpyxl

path_demostic = r"order\0615\机器订单_2020-06-15.xlsx"
wb_demostic = openpyxl.load_workbook(path_demostic, data_only=True)
for s in wb_demostic.worksheets:
    if s.title == "未发汇总":
        ws = wb_demostic["未发汇总"]
title = list(ws.values)[0][:-4]
title = list(title)
title[-1] = "内贸订单数量"
print(title)
# print([[col for col in row] for row in list(ws.values)[1:]])
data_list = []
data_list.append(list(title))
for rw in [[col for col in row] for row in list(ws.values)[1:]]:
    if rw[0] == "未发":
        data_list.append(rw[:-4])
print(data_list)
