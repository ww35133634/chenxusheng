"""
成员方法
"""

# class Man:
#     # 成员变量/成员属性
#     def __init__(self):
#         self.gender = '男性'
#         self.name = None
#
#     # 成员方法  定义部分
#     def sing(self):
#         print('唱了一首歌...')
#
#     def dance(self):
#         print('跳了一支舞***')
#
#
# man1 = Man()
# # 调用方法 对象名.方法名()
# man1.sing()
# man1.dance()
#
# print('*' * 50)
#
# man2 = Man()
# man2.sing()
# man2.dance()











class Man:
    # 成员变量/成员属性
    def __init__(self):
        self.gender = '男性'
        self.name = None

    # 成员方法  定义部分
    def sing(self,num1):  # 形参
        print('唱了%s首歌...' % num1)

    def dance(self,num2):
        print('跳了%s支舞***' % num2)


man1 = Man()
# 调用方法 对象名.方法名()
man1.sing(1)  # 实参传递
man1.dance(1)

print('*' * 50)

man2 = Man()
man2.sing(2)
man2.dance(2)








































































