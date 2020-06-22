
import xlrd
import xlutils


class Xlrd_Excel:

    def __init__(self, path, title):
        self.path = path
        self.title = title

    def rd_excel(self):
        wb = xlrd.open_workbook(self.path)
        ws = wb.sheet_by_name(self.title)
        return ws

