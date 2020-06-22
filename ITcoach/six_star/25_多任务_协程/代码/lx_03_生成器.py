"""
演示生成器
"""


# list1 = [i for i in range(1,11)]
# print(list1)
#
# list2 = [i*2 for i in range(1,11)]
# print(list2)


# 生成器的表现形式之一: 列表推导式 [] >>> ()
# list2 = (i*2 for i in range(1,11)) # 生成器
# print(list2)
# for i in list2:
#     print(i,end= ',')



# 函数 保存生成数据的方法,  yield
# 条件1:保存着生成数据的方法代码
#条件2: 有关键字: yield
# 特殊的迭代器






#方法, 函数,  生成器
# 函数里面有yield  函数 >>> 生成器
# def fei_bo(c):
#     a, b = 0 ,1
#     # 来一个循环变量
#     # list1 = []
#     start_num = 0
#     while start_num < c: # c的值就是我们取值斐波那契的范围
#         # print(a,end=',')
#         yield a
#         a, b = b , a + b
#         start_num += 1
#         # return a
#
# fei_bo1 = fei_bo(10)
# for i in fei_bo1:
#     print(i,end=',')




# 函数 >>> 生成器模板  创建对象
# def fei_bo(c):
#     a, b = 0 ,1
#     # 来一个循环变量
#     # list1 = []
#     start_num = 0
#     while start_num < c: # c的值就是我们取值斐波那契的范围
#         # print(a,end=',')
#         yield a # 0  1 1 不会停止整个代码块的运行  暂停挂起的机制  被调用两次两次取值,
#         a, b = b , a + b  #     a , b   =1 ,2
#         start_num += 1
#         # return a
#
# fei_bo1 = fei_bo(10) # 创建生成器对象
# # for i in fei_bo1:
# #     print(i,end=',')
# f1 = next(fei_bo1)
# print(f1)
#
# f2 = next(fei_bo1)
# print(f2)




# 怎么去 证明 yield 暂停
# def fei_bo(c):
#     print('---1---')
#     a, b = 0 ,1
#     start_num = 0
#     while start_num < c:
#         print('---2---')
#         yield a # 0  1 1 # 暂停
#         print('---3---')
#         a, b = b , a + b
#         start_num += 1
#         print('---4---')
#
# fei_bo1 = fei_bo(10) # 创建生成器对象
# # for i in fei_bo1:
# #     print(i,end=',')
# f1 = next(fei_bo1) # 一次取值
# print(f1)
#
# f2 = next(fei_bo1)
# print(f2)



# 生成器模板
# def fei_bo(c):
#     a, b = 0 ,1
#     start_num = 0
#     while start_num < c:
#         yield a # 0  1 1 # 暂停
#         a, b = b , a + b
#         start_num += 1
#
# fei_bo1 = fei_bo(10)
# fei_bo2 = fei_bo(5)
# for i in fei_bo1:
#     print(i,end=',')
# print()
# for i in fei_bo2:
#     print(i,end=',')



# def fei_bo(c):
#     a, b = 0 ,1
#     start_num = 0
#     while start_num < c:
#         yield a # 0  1 1 # 暂停
#         a, b = b , a + b
#         start_num += 1
#
# fei_bo1 = fei_bo(2)
# # for i in fei_bo1:
# #     print(i)
# # f1 = next(fei_bo1) # 一次取值
# # print(f1)
# # f2 = next(fei_bo1) # 一次取值
# # print(f2)
# # f3 = next(fei_bo1) # 一次取值
# # print(f3)
# while True:
#     try:
#         f1 = next(fei_bo1) # 一次取值
#         print(f1)
#     except Exception:
#         break




# def fei_bo(c):
#     a, b = 0 ,1
#     start_num = 0
#     while start_num < c:
#         yield a # 0  1 1 # 暂停
#         a, b = b , a + b
#         start_num += 1
#     return 'hello, 武汉加油' # 一般放到最后
#
# fei_bo1 = fei_bo(2)
# while True:
#     try:
#         f1 = next(fei_bo1) # 一次取值
#         print(f1)
#     except Exception as e:
#         print(e.value)
#         break


# send() 启动生成器模板
def fei_bo(c):
    a, b = 0 ,1
    start_num = 0
    while start_num < c:
        d = yield a # 0  1 1 # 暂停
        # print(d)
        a, b = b , a + b
        start_num += 1

fei_bo1 = fei_bo(10)

# f1 = next(fei_bo1) # 一次取值
# print(f1)

f2 = fei_bo1.send('武汉加油') # 通过一个类似传参的方式往模块内部传递数据
print(f2)



"""
迭代器: __iter__(返回一个迭代器self)  __next__(保存着生成数据的代码) next()

生成器: 特殊的迭代器, yield 内部代码只执行一部分 next() send('')
"""




















