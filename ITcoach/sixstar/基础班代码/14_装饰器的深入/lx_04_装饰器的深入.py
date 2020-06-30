"""
演示装饰器的深入
"""

"""
函数功能的添加
1.无参数 无返回值的
2.有参数 无返回值的
3.有参数 又有返回值的

4.一个函数被多个装饰器装饰
5.装饰器带有参数的情况
"""

# 1.无参数 无返回值的

# 2 有参数 无返回值的  定义的东西 程序员 更复杂都 没有关系  调用的话 越简单越好
# def a(c):
#     def b(name):  # 2 name = '长沙市'
#         print('中华人民共和国的:',end='')
#         c(name)  # 原demo1 3  '长沙市'  函数的调用 实参
#     return b
#
# @a  # demo1 = a(demo1)
# def demo1(name):  # 4 形参接收
#     print('湖南省的%s' % name)
#
# demo1('长沙市')  # b() 1


# 不管你传过来多少的参数,,我都能够接住  可变参数  字典参数
# def a(c):
#     def b(*args, **kwargs):  # 2 name = '长沙市'
#         print('中华人民共和国的:',end='')
#         c(*args, **kwargs)  # 原demo1 3  '长沙市'  函数的调用 实参
#     return b
#
# @a  # demo1 = a(demo1)
# def demo1(name):  # 4 形参接收
#     print('湖南省的%s' % name)
#
# demo1('长沙市')  # b() 1




#
# 3.有参数 又有返回值的
# def a(c):
#     def b(*args, **kwargs):  # 2 name = '长沙市'
#         print('中华人民共和国的:',end='')
#         # return c() # 原来的 demo1  c() = 'bobo老师真帅气'
#         # print('湖南省的长沙市')
#         # return 'bobo老师真帅气'
#         return c(*args, **kwargs)  # 原demo1 3  '长沙市'  函数的调用 实参
#     return b
#
# @a  # demo1 = a(demo1)
# def demo1(name):  # 4 形参接收
#     print('湖南省的%s' % name)
#     return 'bobo老师真帅气'  # 返回值
#
# i = demo1('长沙市')  # b() 1  'bobo老师真帅气'
# print(i)
"""
1.a = xxxx 先执行右边 
demo1('长沙市') >>>函数的调用

"""


# 建议反复观看函数定义与调用格式三
# 函数的调用: a() 1.去执行里面的代码,  执行完代码之后a() = 返回值
"""
demo1(),
1.print('中华人民共和国的:',end='') print('湖南省的%s' % name)
2.return 'bobo老师真帅气'  c() 去执行里面的代码  print('湖南省的%s' % name)  'bobo老师真帅气'
(1) 
"""




# 4.一个函数被多个装饰器装饰 两个
# 两个闭包
# 第一个闭包
# def A1(c):
#     print('这是第一个装饰器......') # 2
#     def B1(*args,**kwargs):
#         print('添加了第一种功能.......') # 3
#         return c(*args,**kwargs)  # 要被装饰的函数print('添加了第二种功能******')
#     return B1             # return c(*args,**kwargs)  # 要被装饰的函数 print('周周老师真帅气~~~~~~')
# # 第二个闭包
# def A2(c):
#     print('这是第二个装饰器******')  # 1
#     def B2(*args,**kwargs):
#         print('添加了第二种功能******')  # 4
#         return c(*args,**kwargs)  # 要被装饰的函数 print('周周老师真帅气~~~~~~')
#     return B2
# # 要被装饰的函数  满足他下面紧挨着的必须是函数   装饰器只能对函数进行装饰
# @A1  # (1) 不会发生改变 >>>
# # (3)当下面紧挨着变成了一个函数,,马上就开始进行装饰  B2 = A1(B2) >>>  B2 = B1
# @A2  # (2) demo = A2(demo)  >>> demo = B2
# def demo():
#     print('周周老师真帅气~~~~~~')
#
# demo()  # >> B2 ()  >>> B1()

"""
1.装饰器只有遇到函数才会进行装饰,,
2.第二个装饰器 装饰的 是print('周周老师真帅气~~~~~~') 
3.第一个装饰器 装饰的 是第二个闭包里面的B2
"""

#
# def A1(c):
#     print('这是第一个装饰器......')
#     def B1(*args,**kwargs):
#         print('添加了第一种功能.......')
#         return c(*args,**kwargs)
#     return B1
# # 第二个闭包
# def A2(c):
#     print('这是第二个装饰器******')
#     def B2(*args,**kwargs):
#         print('添加了第二种功能******')
#         return c(*args,**kwargs)
#     return B2
#
# @A1
# @A2    # >>>> demo = A1(A2(demo))
# def demo():
#     print('周周老师真帅气~~~~~~')
#
# # demo = A1(A2(demo))
# demo()






# 5 装饰器带有参数的情况  闭包的理念 内部函数用到外部函数的数据,,,,
# def d(name):  # name = '这是装饰器的参数.....'
#     def a(c):  # 用来接收要被装饰的函数的引用
#         def b(*args,**kwargs):
#             print(name)
#             print('我增加了一个功能......')
#             return c(*args,**kwargs)  # 要被装饰的函数
#         return b
#     return a
#
# @d(name = '这是装饰器的参数.....')  # demo = d('这是装饰器的参数.....')(demo)
# def demo():
#     print('我是要被装饰的函数******')

# demo = d('这是装饰器的参数.....')(demo) 拆分按照顺序去执行
"""
1.右边 函数的调用  d('这是装饰器的参数.....')  >>> 返回值 a
demo = a(demo)
2. 函数的调用   a(demo) >>> b
3. demo = b 
"""
# demo()


"""
1.引用
2.闭包:1.函数嵌套函数 2.内部函数用到了外部函数的数据 3.外部函数return 内部函数引用
3.装饰器:
闭包的情况下,,配合@a 的使用
只能对函数进行装饰,,,b = a(b)
作用: 在不修改原函数内部代码的情况下,,对其进行功能的添加,,,

1.无参数 无返回值的
2.有参数 无返回值的
3.有参数 又有返回值的

4.一个函数被多个装饰器装饰
5.装饰器带有参数的情况
"""

"""
作业
复习装饰器
预习面向对象

"""

"""
一个小时:
学过的内容做一个解答

"""
#  (18)







from time import sleep
from gevent import *
def sing():
    print('111...')
    sleep(0.5)

def dance():
    print('222...')
    sleep(0.5)

def main():
    joinall([spawn(sing),spawn(dance())])

if __name__ == '__main__':
    main()
































