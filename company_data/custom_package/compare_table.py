"""获取成品机和整机品号对照表"""

import openpyxl


class CompareTable:

    def __init__(self, path: str, name: str, condition1: str, condition2: str, flag: bool = True):
        self.path = path                # Excel文件路径
        self.name = name                # Excel工作表名称
        self.condition1 = condition1    # 查询条件1
        self.condition2 = condition2    # 查询条件2
        self.flag = flag                # Excel工作表是否有标题行，默认包含标题
        self.result_data_dict = {}      # 定义字典存放内贸数据

    def get_index(self):
        wb = openpyxl.load_workbook(self.path, data_only=True)
        self.ws = wb[self.name]
        # d1 = 0
        # d2 = 0
        if self.flag:
            ws_titles = list(self.ws.values)[0]
            for t1 in ws_titles:
                if self.condition1 in t1:
                    d1 = ws_titles.index(t1)
            for t2 in ws_titles:
                if self.condition2 in t2:
                    d2 = ws_titles.index(t2)
            return d1, d2

    def get_result(self, filter_condition: str = ""):
        x, y = self.get_index()
        for row in list(self.ws.values)[1:]:
            if row[0] == filter_condition:
                if not row[x] == None:
                    self.result_data_dict[str(row[x])] = row[y]

            else:
                if not row[x] == None:
                    self.result_data_dict[str(row[x])] = row[y]


if __name__ == '__main__':
    # path = r"F:\pyprogram\ITcoach\company_data\sale_order\0615\外贸机器订单截止_2020-6-16简洁版(1).xlsx"
    # name = "外贸订单跟进情况"
    path = r"F:\pyprogram\ITcoach\company_data\sale_order\0615\机器订单_2020-06-15.xlsx"
    name = "未发汇总"
    a = "品号"
    b = "数量"
    c = "未发"
    obj01 = CompareTable(path, name, a, b)
    obj01.get_result(c)
    print(obj01.result_data_dict)

