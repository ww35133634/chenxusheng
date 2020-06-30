"""
演示静态方法
"""

"""
实例方法: 跟对象息息相关,随着对象的改变而发生改变
类方法: 跟类直接相关的,不会随着对象的改变而发生改变

静态方法: 跟类没有关系的方法
存在的意义:
"""


# 类方法: 不会随着对象的改变而发生改变
class Man:  # 中国人的模板
    # 类变量 > 不会随着对象的改变而发生改变
    country = '中华人民共和国'
    # 实例变量 > 会随着对象的改变而发生改成
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    # 实例方法 > 随着对象的改变而发生改变的方法
    def myself(self):
        print('我是:%s,我是一个:%s,我为中国加油' %(self.name,self.gender))

    # 类方法的定义 >不会随着对象的改变而发生改变
    @classmethod  # 固定的语法格式
    def fighting(cls):  # class 类本身
        print('我是中国人,我骄傲')

    # 静态方法 >>> 就是一个被打包在类模板里面的函数
    @staticmethod # 固定的语法格式, 把下面的函数(方法) 变成静态方法
    def say():
        print('bobo老师真帅气')

man1 = Man('简自豪','男性')  # init方法被自动调用
# 1.类名.方法名 直观性更强 2.对象名.方法名 不推荐,不常用
# Man.fighting()

# 调用静态方法, 类名.方法名
Man.say()
# 对象名.方法名
man1.say()













































































