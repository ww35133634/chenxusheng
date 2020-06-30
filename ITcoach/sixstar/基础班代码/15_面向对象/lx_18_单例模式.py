"""
演示单例模式
"""
""""
单个实例对象
类模板 >>> 创建无数个对像

单例模式
类模板 >>> 只能够创建出一个对象  >>>  __new__
同一个对象
"""
# class Man:
#     def __init__(self,name):
#         self.name = name
#
# man1 = Man('bobo')
# man2 = Man('思思')
# print(id(man1))
# print(id(man2))


# 创建一个单例类模板 >>> 只能创建出一个对象
class TheMan:
    # 创建对象相关的,, new方法,, 通过重写new方法来达到干预的目的
    __instance = None  # 类变量  101  私有化 不让外界去控制
    def __new__(cls, *args, **kwargs):
        # 创建对象要依赖object类里面的new方法
        # instance = None  # 每次创建对象instance的值都是从None开始的,,
        if cls.__instance is None:
            cls.__instance = object.__new__(TheMan)  # ,每被执行一次,,就会申请一片内存空间(房子),不会有新的对象产生
        return cls.___instance  # 每次的instance都是同一个对象

    def __init__(self,name):
        self.name = name

man1 = TheMan('bobo')  # 101
# TheMan.instance = None  # 不能够让外界去控制咱们的instance
man2 = TheMan('思思')  # 101
print(id(man1))
print(id(man2))


"""
对象没被创建之前,,instance是没有值的,,
当第一个对象创建出来之后,,instance是不是就有了值啊..
如果instance有了值之后,,以后创建对像就跳过创建对象部分,,,
那么是不是就意味着,,, 不管你创建出来多少个对象,,,都是同一个instance
101  101 101 101 101  
"""

""""
123  == 123
 is  >>> 判断两个的内存地址是否相同
==  is 
"""

# 可变类型
# list1 = [1,2,3]
# list2 = [1,2,3]
# print(list1 == list2)  # == 判断的是值相等
# print(id(list1))
# print(id(list2))
# print(list1 is list2)  # is 判断的是内存地址

""""
打印机案例
打印机的类模板
有一个列表,,是用来记录打印的内容是什么,,,
方法,,,列表里面的内容打印出来


man1 = xxx  
man2 = xxx
man3 = xxx
如果是三个对象,那么就意味着有三个列表,,,

如果单例模板,让他只有一个对象
看似三个对象控制着的是同一个列表,,,就可以按照顺序进行打印,,,,,

作业,,,,,,
利用单例完成打印机案例,,,,,,,,,
调用demo1方法,,把自己的打印内容添加到打印列表中,,,,
调用dmeo2方法,,把打印机里面要打印的内容打印出来

2004-简自豪-作业.py
思思
A 
B
C
"""


































