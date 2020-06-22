"""
装饰器的深入
"""
# 没有参数,,没有返回值的函数进行装饰..
# def a(c):
#     def b():
#         print("这里是中华人民共和国的:",end="")
#         c() # 原demo1()
#         print("hello,武汉加油")
#     return b # c()
#
# @a # demo1 = a(demo1)
# def demo1(): # 要被装饰的函数
#     print("湖南省")
#
# # demo1 = a(demo1) # 函数a被调用,,demo1作为实参传过去
# demo1() # → 内部函数a的返回值 → 内部函数b


# 有参数, 无返回值的函数进行装饰
# def a(c):
#     def b(name):
#         print("这里是中华人民共和国的:",end="")
#         c(name) # 原demo1()
#         print("hello,武汉加油")
#     return b # c()
#
# @a # demo1 = a(demo1)
# def demo1(name): # 要被装饰的函数
#     print("湖南省的%s" % name)
#
# # demo1 = a(demo1) # 函数a被调用,,demo1作为实参传过去
# demo1("岳阳市") # → 内部函数a的返回值 → 内部函数b


# 如何对有用不定长参数的函数进行装饰
# def a(c):
#     def b(*args,**kwargs):
#         print("这里是中华人民共和国的:",end="")
#         c(*args,**kwargs) # 原demo1()
#         print("hello,武汉加油")
#     return b # c()


# 对带有返回值的参数进行装饰
def a(c):
    def b(*args,**kwargs):
        # print("这里是中华人民共和国的:",end="")
        return c(*args,**kwargs) # 原demo1()
        # print("hello,武汉加油")
    return b # c()

@a
def demo1(name):
    print("湖南省的%s" % name)
    return "hello,热干面加油"

test1 = demo1("岳阳市")
print(test1)












































































