"""
演示继承
"""

# class Father:
#     # 实例变量
#     def __init__(self):
#         self.name = None
#         self.place = None
#
#     # 实例方法
#     def myself(self):
#         print('我叫%s,我来自%s' % (self.name,self.place))
#
#
# class Son(Father):  # 产生继承关系  产生父子关系
#     pass
#
# son1 = Son()  # 创建对象 >>> init方法被自动调用
# # 子类里面的东西如果没有的话 >>> 他会去找父类要
# son1.name = '王小明'
# son1.place = '湖北'
# son1.myself()  # 调用还是父类的方法








class Father:
    # 实例变量
    def __init__(self):
        self.name = None
        self.place = None
        # 私有属性
        self.__id_card = 123456

    # 实例方法
    def myself(self):
        print('我叫%s,我来自%s' % (self.name,self.place))


class Son(Father):  # 产生继承关系  产生父子关系
    def sing(self):
        print('我很会唱歌')

son1 = Son()  # 创建对象 >>> init方法被自动调用
# 子类里面的东西如果没有的话 >>> 他会去找父类要
print(son1.__id_card)




















































