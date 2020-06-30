"""
演示类的定义
"""

# 定义了一个类,, 定义了一个类模板
# class Man: # 如果有继承关系,()  没有的话可以不加
#     pass
#
# # 对象名
# man1 = Man()  # 创建对象
# man2 = Man()

# name = 'bobo老师'
# age = 18
"""
第二种
"""
"""
	class 类名:
		def __init__(self):
			self.变量名1 = 值1
			self.变量名2 = None

"""


class Man:  # 定义类模板
    """成员"""
    # 成员变量 >>> 静态化的状态 年纪 国籍 身高 体重  成员属性 / 静态化
    # 所有通过类模板创建出来的对象都拥有的属性/变量 就定义在init方法里面
    def __init__(self):  # 双下划线__init__(self)
        # 定义成员变量 固定的语法格式
        self.gender = '男'  # 成员变量
        self.name = None  # 并不确定该属性具体的值,,
    # 成员方法 >>> 动态化的行为 函数

"""
调用格式:	取值: 对象名.变量名
			赋值: 对象名.变量名 = 值
"""
# 创建对象  >>>  通过类模板来创建对象  群体>个体
man1 = Man()  # 对象名
print(man1.gender)
# print(man1.name)
man1.name = '卓定'  # 给他取了一个名字
print(man1.name)

# 创建对象出来之后,,独有的属性/变量
man1.looks = '帅气'  # 属于该对象特有的属性
print(man1.looks)

print('*' * 50)

man2 = Man()
print(man2.gender)
# print(man2.name)
man2.name = '高天亮'
print(man2.name)
# print(man2.looks)  # 并不具备属于第一个对象的独有的属性












































































