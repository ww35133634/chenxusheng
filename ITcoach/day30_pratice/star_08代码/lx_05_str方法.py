"""
演示str方法
"""

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

    def __str__(self):  # 也是一个魔术方法 特定的时机去进行调用
        # return一个返回值
        return '这个类是创建人类的模板'

man1 = Man()  # man1 是一个对象 引用 man1 → 内存空间

# 对象名被打印的时候 __str__
print(man1)  # 如果不仅仅想要他的一个内存空间地址值 而是想要一些说明性的文字 数据 信息
# <__main__.Man object at 0x0000025356BDD080>
# 这个类是创建人类的模板

































































































