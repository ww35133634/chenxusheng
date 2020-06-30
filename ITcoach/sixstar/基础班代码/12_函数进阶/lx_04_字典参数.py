"""
演示字典参数(形参相关)
"""

# 可变参数是用来接收没人要的任意数量的位置实参  args
# 字典参数是用来接收每人要的任意数量的关键字实参  kwargs  >>>key word

#  位置形参 可变参数 位置形参(关键字实参传值) 字典参数
def demo(a,b,*args,c,**kwargs):
    print(a)  # 1
    print(b)  # 2
    print(args)  # (3,4,5,6)
    print(c)  # 7
    print(kwargs)  # d = 8 , e = 9 关键字实参   字典

#    位置参数    关键字实参
demo(1,2,3,4,5,6,c = 7, d = 8 , e = 9)  # c =7 d = 8 , e = 9

# 字典参数应用场景很少
















































































