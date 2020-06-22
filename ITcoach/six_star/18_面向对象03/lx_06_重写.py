"""
演示重写
"""

# class Father:
#     def play(self):
#         print("钓鱼")
#
# class Son(Father):
#     def play(self): # 重写  (覆盖)
#         print("打游戏")
#
#
#
# son1 = Son()
# son1.play()
# print(son1)




class Father:

    def play(self):
        print("钓鱼")

class Son(Father):

    def play(self): # 重写  (覆盖)
        print("打游戏")


    # 调用格式一:
    # 	父类名.方法名(对象)
        Father.play(self)

    # 调用格式二:
    # 	super(子类名,对象).方法名()
        super(Son,self).play()

    # 调用格式三: 使用这个哟
    # 	super().方法名()
        super().play()
son1 = Son()
son1.play()








































