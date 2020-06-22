"""
演示成员方法
"""

# class Man:
#     def __init__(self):
#         self.gender = "男"
#         self.name = None
#
#     def run(self): # 成员方法
#         print("跑了一千米")
#
#     def sing(self):
#         print("唱了一首歌")
#
#
# man1 = Man()
# man1.run()
# man1.sing()





class Man:
    def __init__(self):
        self.gender = "男"
        self.name = None

    def run(self,num1): # 成员方法
        print("跑了%s千米" % num1)

    def sing(self,num2):
        print("唱了%s首歌" % num2)


man1 = Man()
man1.run(2)
man1.sing(2)

print("-"*100)
man2 = Man()
man2.run(3)
man2.sing(3)



































