"""
演示init方法
"""
# 函数/方法必须是先定义,再调用(才会去执行里面的代码)

class Man:
    # 成员变量/成员属性
    def __init__(self):  # 也是一个方法/函数
        self.gender = '男性'  # 已经被执行,
        self.name = None

    # 成员方法  定义部分
    def sing(self,num1):  # 形参
        print('唱了%s首歌...' % num1)

    def dance(self,num2):
        print('跳了%s支舞***' % num2)


# 只要对象一被创建, 那么init方法就自动被调用,里面的代码自动被执行
man1 = Man()   #__init__() 方法在创建对象时被运行, 无需手工调用即可执行
# 对象名.方法名 ()
print(man1.gender)  # init方法已经被调用了,>>> init方法已经在不知不觉中被























































































