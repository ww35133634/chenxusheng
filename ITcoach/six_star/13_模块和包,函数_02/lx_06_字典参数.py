"""
字典参数
"""

# 可以有,  但是有且只有一个,
# def demo(a,b,*args,c=1,d=2,):
#     print(a)
#     print(b)
#     print(args)
#     print(c)
#     print(d)
#
# demo(1,2,3,4,5,c=10,d=20,e=30,f=40)

# 位置参数, 可变参数, 关键字参数, 字典参数
def demo(**kwargs):
    print(kwargs)

demo(a=1,b=2,c=3)




















