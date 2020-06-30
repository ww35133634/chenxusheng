"""
演示封装和私有化
"""
# 面向对象的三大特点: 1.封装(2) 2.继承(1) 3.多态(3):理念性的东西 比较的抽象

# 私有属性/成员变量
# class Man:
#     # 成员变量/属性
#     def __init__(self):
#         # self.id_card = None  # 隐私,不想呢让别人去简简单单的访问到
#         # 私有化 >>> 外部直接访问不到, 更加的安全
#         self.__id_card = None  # 加上两个下划线 >>> 将该属性/变量私有化
#
# man1 = Man()
# # print(man1.__id_card)
# print(man1.id_card)






# 私有属性/成员变量
# class Man:
#     # 成员变量/属性
#     def __init__(self):
#         # self.id_card = None  # 隐私,不想呢让别人去简简单单的访问到
#         # 私有化 >>> 外部直接访问不到, 更加的安全
#         self.__id_card = None  # 加上两个下划线 >>> 将该属性/变量私有化
#
#     # 类的内部可以去使用到私有的东西嘛
#     def bobo(self):  #
#         # 返回值
#         return self.__id_card
#
# man1 = Man()
# # 通过成员方法去间接的拿到私有变量/属性
# id_card = man1.bobo()
# print(id_card)


class Man:
    # 成员变量/属性
    def __init__(self):
        # self.id_card = None  # 隐私,不想呢让别人去简简单单的访问到
        # 私有化 >>> 外部直接访问不到, 更加的安全
        self.__id_card = None  # 加上两个下划线 >>> 将该属性/变量私有化

    # 类的内部可以去使用到私有的东西嘛
    def get_id_card(self):  # 间接去调用私有属性的方法, get__
        # 返回值
        return self.__id_card

    # 通过一个间接的方式去修改/设置私有属性/变量
    def set_id_card(self, id_card):
        self.__id_card = id_card  # 应该赋值给私有变量


man1 = Man()
# 外部去给id_card传具体的值,,参数的传递,,
man1.set_id_card('430626xxxxxxx')
# 通过成员方法去间接的拿到私有变量/属性
id_card = man1.get_id_card()
print(id_card)
# 封装 >>>  特殊的属性/变量进行私有化, 






























































