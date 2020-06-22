"""
静态方法
"""

class Chinese:
    # 类变量
    country = "中国"
    def __init__(self,name,id_card):
        self.name = name
        self.id_card = id_card

    # 静态方法定义
    # @staticmethod
    # def say():
    #     print("今天是个好日子")
    @staticmethod
    def say():
        print("今天是个好日子")

man1 = Chinese("小明","654321")
# # 类名
# Chinese.say()
# # 对象名
# man1.say()
# say()

# 继承





























