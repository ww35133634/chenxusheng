"""
继承关系
"""
class Father(object):
    pass

class Son(Father):
    pass

class Sun(Son):
    pass

print(Sun.__mro__)
sun1 = Sun()


















