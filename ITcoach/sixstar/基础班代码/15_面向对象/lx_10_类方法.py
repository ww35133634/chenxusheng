"""
演示类方法
"""
"""
类模板,代表的是一个群体,,通过类来创建对象.....
类:成员
成员:1.类成员 2.实例成员(对象)
1.类成员: (1).类变量 (2).类方法
2.实例成员(对象): (1).实例变量__init__ (2).实例方法
"""
# class Man:  # 中国人的模板
#     # 类变量 > 不会随着对象的改变而发生改变
#     country = '中华人民共和国'
#     # 实例变量 > 会随着对象的改变而发生改成
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender
#
#     # 实例方法 > 随着对象的改变而发生改变的发生
#     def myself(self):
#         print('我是:%s,我是一个:%s,我为中国加油' %(self.name,self.gender))
#
#
# man1 = Man('简自豪','男性')  # init方法被自动调用
# Man.country = '中国'
#
# man1.country = '中华人民共和国家'  # >>> 添加该对象私有变量,,,
#
# man2 = Man('史森明','男性')
# print(Man.country)








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

man1 = Man('简自豪','男性')  # init方法被自动调用
# 1.类名.方法名 直观性更强 2.对象名.方法名 不推荐,不常用
Man.fighting()










"""
	1.类方法中不允许使用实例变量和实例方法。
	
	2.实例方法中允许使用类变量和类方法。


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
        # 实例方法当中使用类变量 >>> 类名.类变量名
        print(Man.country)
        # 实例方法当中去调动类方法>>> 类名.类方法名
        Man.fighting()

    # 类方法的定义 >不会随着对象的改变而发生改变
    @classmethod  # 固定的语法格式
    def fighting(cls):  # class 类本身
        print('我是中国人,我骄傲')
        # 类方法中去调用实例变量
        # print(self.name)  # 本实例,,,
        # print(man1.name)  # 实际的对象,,,

        # 实例方法
        # self.myself()
        # 对象名
        # man1.myself()
man1 = Man('简自豪','男性')  # init方法被自动调用

# 演示实例方法当中去调用类的成员  类变量和类方法
# man1.myself()

# 调用类方法
Man.fighting()

"""
调用自身
"""
































































