"""
演示重写 建立在继承关系之上
"""
"""
在子类中如果定义了和父类相同名称的方法, 那么此时的子类的方法就对父类的方法构成了 重写。

如果子类重写了父类的方法, 使用子类对象调用被重写的方法时, 执行子类中重写后的方法。
"""


# class Father:
#     def play(self):
#         print('去湖边钓鱼......')
#
#
# class Son(Father):
#     def play(self):
#         print('去球场打球******')
#
#
# son1 = Son()
# son1.play()




"""
调用格式一:
	父类名.方法名(对象)
    object.__new__
调用格式二:
	super(子类名,对象).方法名()

调用格式三:
	super().方法名()
    super().__new__   Father Mon
"""


class Father:
    def play(self):
        print('去湖边钓鱼......')


class Son(Father):
    def play(self):
        print('去球场打球******')
    # 格式一:  父类名.方法名(对象)
    #     Father.play(self)
    # 格式二: super(子类名,对象).方法名()
    #     super(Son,self).play()
    # 格式三: super().方法名()  >>> 一般只用第三种
        super().play()
son1 = Son()
son1.play()
































































































