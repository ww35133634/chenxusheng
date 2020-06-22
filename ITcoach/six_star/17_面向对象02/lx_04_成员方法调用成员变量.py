"""
演示成员方法调用成员变量
"""
# 调用公有变量
# class Man:
#     def __init__(self):
#         self.gender = "男"
#         self.name   = None
#
#     def myself(self): # 来一个自我介绍
#         print("我叫%s,性别%s" %(self.name,self.gender))
#
#
#
# man1 = Man()
#
# man1.name = "吕子乔"
# man1.myself()


# 调用独有变量
class Man:
    def __init__(self):
        self.gender = "男"
        self.name   = None

    # def myself(self): # 来一个自我介绍
    #     print("我叫%s,性别%s" %(self.name,self.gender))
    def myself(self):
        print("我叫%s,性别%s,我很%s" % (self.name,self.gender,self.looks))


man1 = Man()
man1.name = "吕子乔"
# 给他一个独有变量
man1.looks = "帅"
man1.myself()

man2 = Man()
man2.name = "曾小贤"
man2.myself()
















