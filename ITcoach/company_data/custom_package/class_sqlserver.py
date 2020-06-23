import pymssql

class SQLServer:

    def __init__(self,server:str,user:str,password:str,database:str):
        self.server = server
        self.user = user
        self.password = password
        self.database = database

    def __GetConnect(self):
        """连接数据库"""
        self.conn = pymssql.connect(server=self.server,user=self.user,password=self.password,database=self.database)
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")  # 将DBC信息赋值给cur
        else:
            return cur

    def ExecQurey(self,sql):
        """执行查询，返回一个包含tuple的list，list是元素的记录行，tuple记录每行的字段数值"""
        cur = self.__GetConnect()
        cur.execute(sql)
        recordset = cur.fetchall()
        self.conn.close()
        return recordset
    @staticmethod
    def main(sql):
        cnn = SQLServer(server="192.168.21.211", user="Warehouse Department", password="CXS", database="YF_YRONG")
        results = cnn.ExecQurey(sql)
        machines_stock = {}
        for x, y in results:
            if x.strip() in machines_stock.keys():
                machines_stock[x.strip()] += int(y)
            else:
                machines_stock[x.strip()] = int(y)
        return machines_stock







