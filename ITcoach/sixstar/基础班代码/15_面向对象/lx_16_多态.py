"""
演示多态  抽象
"""
#              H2o
# 冰 固态    水 液态    水蒸气 气态

"""
son1, Son(1,2,3,4)
开车  >>> 司机  
唱歌  >>> 歌手
做饭  >>> 厨师
打球  >>> 教练
son1有多态的特征 
"""
"""
旁观者---陌生人 
孩子  ---父亲  
老婆  ---老公   
父母  ----儿子 
男人 多态的特征 多种形态
"""


class Player:  # 球员类模板
    def play(self):
        print('会打篮球***')

class Singer:  # 歌手类模板
    def sing(self):
        print('会唱歌...')

class Man(Player,Singer):
    def play(self):
        print('我会打篮球...')

    def sing(self):
        print('我会唱歌***')

class Son:
    # 想学习唱歌和打篮球,,找专业的人,需要一个对象来教他,,歌手的对象
    def son_play(self,singer):
        singer.sing()

# singer1 = Singer()
# son1 = Son()
# son1.son_play(singer1)  # 传入一个歌手的对象,,来教孩子唱歌

# 多态
man1 = Man()  # 多态的特征
son1 = Son()
son1.son_play(man1)  # 传入一个歌手的对象,,来教孩子唱歌 ,, 实际上传入的对象是父亲


# man1 = Man()  # 多态的特征


""""
封装
继承                                                   歌手      父亲
多态: 鸭子类型 >>>  一个人在湖面上看到一种禽类在游泳,, 鸭子     实际上他是天鹅

"""











































