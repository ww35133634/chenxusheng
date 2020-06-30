"""
演示类变量
"""


# 类变量  类方法
# class Man:
#     # 成员(实例)变量的定义  self代表的是对象本身 创建对象之后去执行
#     def __init__(self,name,gender,place):  # 对象本身
#         self.gender = gender
#         self.name = name
#         self.place = place
#     # 成员(实例)方法
#     def myself(self):  # 成员方法去调用成员变量(公有变量)
#         print('我是:%s,性别是:%s,我来自:%s,我为中国加油!' %(self.name,self.gender,self.place))
#
# man1 = Man('简自豪','男性','湖北')  # 传参 init方法的调用
# man1.myself()
#
# man2 = Man('史森明','男性','湖南')
# man2.myself()

"""
我是:简自豪,性别是:男性,我来自:湖北,我为中国加油!
我是:史森明,性别是:男性,我来自:湖南,我为中国加油!
"""






# 类变量  类方法 成员变量:1.类变量(类),2.实例对象(对象)
# class Man: # 男人的类模板  跟类直接相关,不随着对象的改变而发生的变量
#     # 类变量
#     gender = '男性'
#     # 成员(实例)变量的定义  self代表的是对象本身 创建对象之后去执行
#     def __init__(self,name,gender,place):  # 对象本身
#         self.gender = gender
#         self.name = name
#         self.place = place
#     # 成员(实例)方法
#     def myself(self):  # 成员方法去调用成员变量(公有变量)
#         print('我是:%s,性别是:%s,我来自:%s,我为中国加油!' %(self.name,self.gender,self.place))
#
# man1 = Man('简自豪','男性','湖北')  # 传参 init方法的调用
# man1.myself()
#
# man2 = Man('史森明','男性','湖南')
# man2.myself()



class Man:  # 中国人的模板
    # 类变量 > 不会随着对象的改变而发生改变
    country = '中华人民共和国'
    # 实例变量 > 会随着对象的改变而发生改成
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    # 实例方法 > 随着对象的改变而发生改变的发生
    def myself(self):
        print('我是:%s,我是一个:%s,我为中国加油' %(self.name,self.gender))


man1 = Man('简自豪','男性')  # init方法被自动调用
# 调用类变量  1.类名.变量名  2.对象名.变量名(不推荐)
# print(Man.country)
# 修改类变量 1.类名.变量名 = 值 成功的进行的修改
Man.country = '中国'

# 对象名.变量名 = 值
man1.country = '中华人民共和国家'  # >>> 添加该对象私有变量,,,

man2 = Man('史森明','男性')
print(Man.country)


















