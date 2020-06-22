"""
演示单例模式
"""
# 控制一个类只能产生一个对象
# class Man():
#     pass
#
#
# man1 = Man()
# man2 = Man()
# print(id(man1))
# print(id(man2))

# 单例类 new方法
# class TheMan:
#     instance = None # 有了具体的值 None → 101
#     def __new__(cls, *args, **kwargs):
#         # 控制只开辟一次内存空间, 那么就会创建出一个对象
#         # instance = None # 只要创建对象, instance就会被初始化成None
#         if cls.instance == None:
#             cls.instance = object.__new__(TheMan) # 开辟一个内存空间,
#         return cls.instance
#
# man1 = TheMan() # man1 → 101  一个对象被创建
#
# man2 = TheMan() # man2 → 101  同一个对象
# print(id(man1))
# print(id(man2))



# shift + f6 统一修改
class TheMan:
    __instance = None # 有了具体的值 None → 101
    def __new__(cls, *args, **kwargs):
        # 控制只开辟一次内存空间, 那么就会创建出一个对象
        # instance = None # 只要创建对象, instance就会被初始化成None
        if cls.__instance is None:
            cls.__instance = object.__new__(TheMan) # 开辟一个内存空间,
        return cls.__instance

man1 = TheMan() # man1 → 101  一个对象被创建

man2 = TheMan() # man2 → 101  同一个对象
print(id(man1))
print(id(man2))

# is 和 == 的区别
# == 判断是两个值是否相同,, is 判断的是两个内存地址是否相同
# list1 = [1,2,3]
# list2 = [1,2,3]
# print(list1 == list2)
# print(list1 is list2)





























