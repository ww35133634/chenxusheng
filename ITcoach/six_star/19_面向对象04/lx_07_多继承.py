"""
演示多继承
"""


class Father1:

    def sing(self):
        print("唱歌唱得好听")

    def play(self):
        print("钓钓鱼")


class Father2:

    def dance(self):
        print("跳舞跳得好")

    def play(self):
        print("打打球")



# 多个父类成员冲突的情况
class Son(Father2,Father1):
    # def play(self):
    #     Father1.play(self)
    pass

# son1 = Son()
# son1.sing()
# # son1.dance()
# son1.play()
# print(Son.__mro__)


# 陌生的男人
# 孩子 爸爸  父母 儿子  老婆 丈夫的角色



















