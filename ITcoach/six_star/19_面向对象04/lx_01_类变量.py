"""
演示类变量
"""
class Man:
    def __init__(self):
        self.name = None
        self.gender = None
        self.place = None

    def myself(self):
        print("我叫%s,性别%s,我来自%s,我为武汉加油" %(self.name,self.gender,self.place))

# man1 = Man()
# man1.name = "吕子乔"
# man1.gender = "男"
# man1.place = "四川"
# man1.myself()
#
# man2 = Man()
# man2.name = "曾小贤"
# man2.gender = "男"
# man2.place = "湖南"
# man2.myself()


# 传参
# class Man:
#     gender = "男" # 类变量
#     def __init__(self,name,gender,place):
#         self.name = name # 实例变量
#         self.gender = gender
#         self.place = place
#
#     def myself(self):
#         print("我叫%s,性别%s,我来自%s,我为武汉加油" %(self.name,self.gender,self.place))
#
# man1 = Man("吕子乔","男","四川")
# man1.myself()
#
# man2 = Man("曾小贤","男","湖南")
# man2.myself()


# 类变量
class Man:
    country = "中国"
    def __init__(self,name,place):
        self.name = name
        self.place = place

    def myself(self):
        print("我来自%s,我叫%s,我为武汉加油" % (self.place,self.name))

man1 = Man("吕子乔","四川省")
# man1.myself()
# # 第一种方式 类名.类变量名
# print(Man.country)
#
# # 第二种方式 对象名.类变量名 (不常用)
# print(man1.country)

# 修改值
# 对象名
# man1.country = "中华人民共和国"  # 对象的独有变量
# man1.looks = "帅"

# 类名
Man.country = "中华人民共和国"
print(Man.country)


























