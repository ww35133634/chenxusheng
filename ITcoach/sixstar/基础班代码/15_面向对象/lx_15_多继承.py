"""
演示多继承
"""


# class Father1:  # >>>object
#     def sing(self):
#         print('会唱歌......')
#     def play(self):
#         print('去湖边钓钓鱼......')
#
# class Father2:
#     def dance(self):
#         print('会跳舞******')
#     def play(self):
#         print('去球场打打篮球')
#
# class Son(Father1,Father2):
#     pass
#
#
# son1 = Son()
# son1.play()  # 继承了 >>> 继承关系
# print(Son.__mro__)
"""
(<class '__main__.Son'>, <class '__main__.Father1'>, <class '__main__.Father2'>, <class 'object'>)
"""




class Mon:
    pass

class Father1(Mon):  # >>>object
    def sing(self):
        print('会唱歌......')
    def play(self):
        print('去湖边钓钓鱼......')

class Father2:
    def dance(self):
        print('会跳舞******')
    def play(self):
        print('去球场打打篮球')

class Son(Father1,Father2):
    pass


son1 = Son()
son1.play()  # 继承了 >>> 继承关系
print(Son.__mro__)
# print(Father1.__mro__)  # 并没有多继承关系了,,,,,
"""
(<class '__main__.Son'>, <class '__main__.Father1'>, 
<class '__main__.Father2'>, <class '__main__.Mon'>, <class 'object'>)
"""








#              H2o
# 冰 固态    水 液态    水蒸气 气态



























































































