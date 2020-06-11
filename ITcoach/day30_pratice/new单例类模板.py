
# 方法1：调用类变量
class Single_Model01:
    instance = None
    t_list = []
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(Single_Model01)
        return cls.instance

    def __init__(self, t):
        self.t = t

    def merge_list(self):
        Single_Model01.t_list.append(self.t)

    def print_list(self):
        print(Single_Model01.t_list)
        for i in Single_Model01.t_list:
            print(i)

# 方法二：使用实例成员变量
class Single_Model02:
    instance = None
    t_list = []
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(Single_Model02)
        return cls.instance

    def __init__(self, t):
        self.t = t

    def merge_list(self):
        self.t_list.append(self.t)

    def print_list(self):
        print(self.t_list)
        for i in self.t_list:
            print(i)

if __name__ == '__main__':
    obj01 = Single_Model01("张三")
    obj01.merge_list()
    # Single_Model.instance = True       #读取类变量，类变量重新赋值
    obj02 = Single_Model01("xt四")
    obj02.merge_list()
    obj01.print_list()
    # obj02.print_list()
    # print(id(obj01))
    # print(id(obj02))

# # 封装私有化变量
# class Single_Model:
#
#     __instance = None
#     __t_list = []
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = object.__new__(Single_Model)
#         return cls.__instance
#
#
#     def __init__(self, t):
#         self.t = t
#         self.merge_list()
#
#     def merge_list(self):
#         self.__t_list.append(self.t)
#
#     def print_list(self):
#         for i in self.__t_list:
#             print(i)
#             # print(self.__t_list)
#
# if __name__ == '__main__':
#     obj01 = Single_Model("张三")
#     obj02 = Single_Model("xt四")
#     obj01.print_list()
#     # obj02.print_list()
#     print(id(obj01))
#     print(id(obj02))