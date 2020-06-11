"""
继承关系
"""
# 如果没有指明具体的父类,, 都默认继承自 object  炎帝黄帝 所有类的共同的父类 >>> 基类
class Father:
    pass

class Son(Father):
    pass

class Sun(Son):
    pass

# 查看继承关系 >>> 家谱
print(Sun.__mro__)

"""
(<class '__main__.Sun'>, <class '__main__.Son'>, <class '__main__.Father'>, <class 'object'>)
"""
"""
hello()方法      sun     >    son       >     Father  >   object  报错 
"""
sun1 = Sun()




















































































































