import openpyxl

class Excel_Oprate:

    def __init__(self, path, header_row: int = 1, title: str = ""):
        self.path = path
        self.header_row = header_row
        self.title = title
        self.data = dict()

    def read_excel(self, *args):
        """
        前两个参数是 要查找字段的 列名；
        最后一个参数是过滤条件的 列名。
        """
        wb = openpyxl.load_workbook(self.path,data_only=True)
        if self.title == "":
            self.ws = wb.active
        else:
            self.ws = wb[self.title]
        headline = [[c for c in row] for row in list(self.ws.values)][self.header_row-1]
        if None in headline:
            headline = headline[:headline.index(None)]
        # print(headline)
        self.fd_index = [headline.index(s) for fd in args for s in headline if fd == s]
        # print(self.fd_index)

    def get_data(self, condition: str = ""):
        for row in list(self.ws.values)[self.header_row:]:
            if row[self.fd_index[0]] != None:
                if condition == "" or row[self.fd_index[-1]] == condition:
                    if row[self.fd_index[0]] in self.data.keys():
                        self.data[row[self.fd_index[0]]] += row[self.fd_index[1]]
                    else:
                        self.data[row[self.fd_index[0]]] = row[self.fd_index[1]]

        # print(self.data)




