"""
演示私有属性和封装
"""

class Man:
    def __init__(self): # __  私有
        self.__id_card = None # 451231321xxxx123351 定义为私有属性 双下划线
        self.name = None

    def get_id_card(self): # 用来得到 获取私有变量的方法
        return self.__id_card

    def set_id_card(self,id_card): # 用来设置 赋值 给私有变量的方法
        self.__id_card = id_card

man1 = Man()
man1.set_id_card("430626XXX")
print(man1.get_id_card())





















































































































