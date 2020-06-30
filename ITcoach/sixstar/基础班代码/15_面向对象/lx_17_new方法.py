"""
演示new方法
"""


# 类模板
# class Man:  # 默认是继承了基类 object
#     # 重写object的new方法
#     # 创建对象利用的是object里面的new方法,,利用new方法里面的代码的执行创建对象
#     def __new__(cls, *args, **kwargs):  # 创建对象
#         # 调用object类里面的new方法,,那么就可以真正的创建对象,,,,
#         print('new方法被执行******')  # 并不能真正的创建对象
#         instance = object.__new__(Man)  # 创建对象 把它return出去
#         return instance  # 真正的创建对象的效果
#         # 对象创建出来,放在类模板里面有用嘛
#
#
#     def __init__(self,name,age):  # 创建对象的时候被自动调用
#         print('init方法被调用了.......')
#         self.name = name
#         self.age = age
#
# # new方法被执行了吗???  执行了的,,默认执行的继承了object类的new方法,里面的代码被执行 >>> 才会创建出来对象
# man1 = Man('李寻欢',28)  # 利用__new__方法创建对象,,,创建对象的时候自动调用init方法,,



"""
为什么要干预new方法,,,,
"""
# 自己没有的东西,,就去找父类要,,,
class Man:  # 没有指明父类的情况下,,那么直系父类就是object
    # 创建对象对象依赖是什么呢,,是new方法的执行(new方法里面的代码的执行>>>创建对象)
    # 如果没有自己定义new方法的话,,那么是自动调用了object类里面的new方法
    # (执行object类new方法里面的代码)去成功的创建对象,,

    def __new__(cls, *args, **kwargs):
        # 这里面没有可以成功(真正)创建对象的代码
        # 如果我们想真正的创建对象,,是不是让object类里面的__new__方法去真正的创建对象
        print('new方法被调用了******')
        instance = object.__new__(Man)  # 对象被成功的创建
        return instance  # 让外界真正的接受到对象,,

    def __init__(self):
        print('init方法被执行了......')

man1 = Man()
# 现在自己有了__new__方法,,那么创建对象的时候,,就会使用自己的__new__方法了,,,
# 对象无法真正的被创建,,,,就导致init方法无法被成功的调用

# 要利用new方法去创建对象,,没有的话就找自己的父类调用
# 创建对象, 创建对象成功之后init方法被调用(里面的代码被执行)












































