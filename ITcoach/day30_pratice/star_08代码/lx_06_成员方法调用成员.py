"""
演示成员方法调用成员
"""

# 时候定义在类模板里面的方法,self
# 成员:1.成员变量 2.成员方法(类似函数调用函数)


"""
成员方法调用成员变量: 1.类模板里面的init方法当中定义的公有变量.
                     2.在创建对象出来之后定义的独有变量
"""
# class Man:
#     # 成员变量的定义
#     def __init__(self):  # 对象本身
#         self.gender = '男性'
#         self.name = None
#
#     # 成员方法
#     def myself(self):  # 成员方法去调用成员变量(公有变量)
#         print('我是:%s,性别是:%s' %(self.name,self.gender))
#
# man1 = Man()
# man1.name = '简自豪'
# man1.myself()  # 默认传过去对象名给self



# class Man:
#     # 成员变量的定义
#     def __init__(self):  # 对象本身
#         self.gender = '男性'
#         self.name = None
#
#     # 成员方法
#     def myself(self):  # 成员方法去调用成员变量(公有变量)
#         print('我是:%s,性别是:%s,我很:%s' %(self.name,self.gender,self.looks))
#
# man1 = Man()
# man1.name = '简自豪'  # (成员变量)私有变量
# man1.looks = '帅'
# man1.myself()  # 默认传过去对象名给self
#
# man2 = Man()  # 该对象没有man1的私有变量,,因此他的成员方法不可以调用
# man2.name = '史森明'
# man2.myself()



"""
成员方法调用成员方法
"""
class Man:
    # 成员方法
    def sing(self):
        print('唱了一首歌')

    def dance(self):
        print('跳了一支舞')

    def run(self):
        # 调用成员方法
        self.sing()
        self.dance()

man1 = Man()
man1.run()  # 调用简单

man2 = Man()
man2.run()












































































