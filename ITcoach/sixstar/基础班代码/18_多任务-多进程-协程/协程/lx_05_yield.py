"""
演示yield的作用和原理
"""

# 函数里面yield >>> 生成器模板
# def fei_bo(c):
#     a, b = 1, 1
#     # 循环变量
#     i = 0
#     while i < c:  # 2 < 6
#         # 他一旦触发 就会进行一次暂停挂起,,,
#         yield a  # 2 跟return 把数据返回出去  不会结束这个语法部分,,
#         a, b = b, a + b   # a = 2
#         i += 1  # 循环变量自增 2
#
#
# data = fei_bo(6)  # 生成器对象的创建  >>> 类比 类创建对象
# print(data)  # 特殊的迭代器
# demo1 = next(data)  # 1.第一次调用next()取值,,启动生成器模板里面的代码, 让代码执行
# print(demo1)  # 2.demo1得到1, 此时他已经暂停挂起了,,,
# demo2 = next(data)  # 3.第二次调用next()取值,, 代码在哪里暂停,,就在哪里开始... 1
# print(demo2)  # 4.demo2得到1,, 此时他已经暂停挂起了,,,
# demo3 = next(data)  # 5.第三次调用next()取值,,
# print(demo3)  # 6.demo3得到yield返回出来的2,,, 进行一次暂停挂起

#  由于接下来并没有再次使用next()去启动代码,,因此 112

# for i in data:  # 可以使用for循环来迭代取值
#     print(i, end=',')
import time

"""
生成器对象既没有 __iter__ __nxet__  却可以使用for循环迭代取值>>> 特殊的迭代器
取值利用的是  for 里面调用next()函数
"""

"""
yield的特点
1.可以讲数据返回出来
2.返回出来之后,,,回暂停挂起
3.下一次使用next()启动,,从哪里暂停,,代码从哪里开始
"""




# a = next(data)
# print(a)
# b = next(data)
# print(b)
# c = next(data)
# print(c)


"""
演示yield 的暂停挂起机制
"""
#
# def fei_bo(c):
#     print('---111---')
#     a, b = 1, 1
#     i = 0
#     while i < c:
#         print('---222---')
#         yield a  # 暂停
#         print('---333---')
#         a, b = b, a + b
#         i += 1
#         print('---444---')
#
# data = fei_bo(6)
# print(data)
# demo1 = next(data)  # 1.111 > 222
# print(demo1)   # 1
# demo2 = next(data)  # 2.333 >>> 444 >>> 222
# print(demo2)   # 1
# demo3 = next(data)   # 3. 333 >>> 444 >>> 222
# print(demo3)   # 2



"""
使用yield 去完成多任务 
"""
# 这是一个单进程  单线程 的 单任务

# def sing():
#     while True:
#         print('bobo老师在唱歌......')
#         time.sleep(0.3)
#
# def dance():
#     while True:
#         print('bobo老师在跳舞******')
#         time.sleep(0.3)
#
# def main():
#     sing()
#     dance()
#
# if __name__ == '__main__':
#     main()



"""
最终目的 使用gevent协程来完成多任务
"""
"""
yield 完成多任务
"""
def sing():  # 从普通的函数 >>> 生成器模板
    while True:
        print('bobo老师在唱歌......')
        time.sleep(0.3)
        yield

def dance():  # 从普通的函数 >>> 生成器模板
    while True:
        print('bobo老师在跳舞******')
        time.sleep(0.3)
        yield
def main():
    t1 = sing()  # 函数的调用 >>> 生成器对象的创建
    t2 = dance()
    #  既然是生成器 那么就是特殊的迭代器  for >>> next()函数去取值
    while True:

        next(t1)  # 启动生成器模板 执行里面的代码
        next(t2)  # 如果想要不停的启动,,,放到循环里面


if __name__ == '__main__':
    main()

# 为什么能起到一个多任务的效果
"""
next(t1)    
next(t2)

next(t1)    
next(t2)
next(t1)    
next(t2)
next(t1)    
next(t2)
next(t1)    
next(t2)

# 多任务的效果
# 既没有利用到多进程  也没有利用到多线程
# 代码的运行 + 资源的占用        运行代码的东西
# yield 完成多任务  占用到的资源是最少
# 完成多任务  协程是占用资源最少的方式........
"""





















