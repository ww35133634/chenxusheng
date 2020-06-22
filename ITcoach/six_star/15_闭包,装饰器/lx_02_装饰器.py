"""
演示装饰器
"""
"""
装饰器就是可以在不修改原函数代码的情况下,去对其进行功能的增加
"""
# def a(c):
#     def b():
#         print("这里是中华人民共和国的:",end="")
#         c() # 原demo1()
#     return b # c()
#
# @a # demo1 = a(demo1)
# def demo1():
#     print("湖南省")
#
# @a
# def demo2():
#     print("广东省")
#
# @a
# def demo3():
#     print("四川省")
#
# @a
# def demo4():
#     print("台湾省")
#
# demo1() # → 内部函数a的返回值 → 内部函数b
# demo2()
# demo3()
# demo4()



def a(c):
    def b():
        print("这里是中华人民共和国的:",end="")
        c() # 原demo1()
        print("hello,武汉加油")
    return b # c()
# @a # demo1 = a(demo1)
def demo1(): # 要被装饰的函数
    print("湖南省")
demo1 = a(demo1) # 函数a被调用,,demo1作为实参传过去
demo1() # → 内部函数a的返回值 → 内部函数b
"""
45,函数a被调用,变量名demo1得到了函数a的返回值,函数a的返回值是什么呢,就是return b,
函数a的返回值就是函数b,,意味着demo1变量名里面保存着的就是函数b......
代表着demo1的调用,,,函数b被调用,里面的调用被执行.......
print("这里是中华人民共和国的:",end=""),,
demo1函数作为一个实参传给了形参c,,c在函数里面被调用,,c()
print("湖南省")
"""









