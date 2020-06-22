"""
演示继承
"""
# 父类
# class Father:
#     def __init__(self):
#         self.name = None
#         self.place = None
#
#
#     def hello(self):
#         print("hello,武汉加油,我是%s" % self.name)
#
# # 子类
# class Son(Father):
#     pass
#
# son1 = Son()
# son1.name = "小明"
# print(son1.name)
# son1.hello()


class Father:
    def __init__(self):
        self.name = None
        self.place = None
        self.__id_card = None

    def hello(self):
        print("hello,武汉加油,我是%s" % self.name)


# 子类
class Son(Father):

    def sing(self):
        print("很会唱歌")


son1 = Son()
son1.name = "小明"
son1.sing()
# son1.__id_card
#













