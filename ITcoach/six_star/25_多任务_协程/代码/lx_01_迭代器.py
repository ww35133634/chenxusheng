# """
# 演示迭代器
# """
# from collections import Iterable, Iterator
#
# # for i in [1,2,3]:
# #     print(i)
#
# # for循环后面 是一个可迭代对象 列表 元组 字符串,
# # for i in 100:
# #     print(i)
#
# # 是一个可迭代对象
# # print(isinstance([1,2,3],Iterable))
# # print(isinstance('武汉加油',Iterable))
# # # 不是一个可迭代对象
# # print(isinstance(10000,Iterable))
# import time
#
#
# # class DiyName: # 类A
# #     def __init__(self):
# #         self.name = []
# #
# #     def add_name(self,name):
# #         self.name.append(name)
# #
# #     def __iter__(self):
# #         return DiyIter(self) # 返回迭代器对象 讲类A的实例对象当作参数传给类B
# #
# #
# # class DiyIter(object): # 类B
# #     def __init__(self,obj): # 得到类A里面的数据
# #         self.obj = obj # 保存着就是类A的实例对象,
# #         self.start_num = 0 # 1 2 3 4
# #     def __iter__(self):
# #         pass
# #
# #     def __next__(self): # for循环其实就是根据这个方法去取值
# #         if self.start_num < len(self.obj.name): # 索引值不能大于列表的长度
# #             a = self.obj.name[self.start_num]
# #             self.start_num += 1
# #             return  a # 取出类A登记名单
# #         else:
# #             raise StopIteration
# #
# #
# # man1 = DiyName()
# # # man2 = DiyIter()
# # man1.add_name("王一")
# # man1.add_name("陈二")
# # man1.add_name("张三")
# # # print(man1.name)
# # # 可迭代对象 iter()  迭代器 iteror
# # # print(isinstance(man1,Iterable)) # 表面上是一个可迭代对象了
# # # # 可迭代对象 >>>  __iter__
# # # print(isinstance(man2,Iterator)) # 表面上是一个迭代器 __iter__,__next__
# #
# #
# # for i in man1:
# #     time.sleep(1)
# #     print(i)
# # 第一步 判断是否是一个可迭代对象,__iter__
# # 第二步 iter(man1) >>> 得到该实例对象的__iter__的返回值
# # 第三步 返回的这个东西 是否是一个 迭代器 >>> __iter__,__next__
#
#
#
#
#
# class DiyName: # 类A
#     def __init__(self):
#         self.name = []
#         # self.obj = obj # 保存着就是类A的实例对象,
#         self.start_num = 0 # 1 2 3 4
#
#     def add_name(self,name):
#         self.name.append(name)
#
#     def __iter__(self):
#         return self # 返回迭代器对象 讲类A的实例对象当作参数传给类B
#
#     def __next__(self): # for循环其实就是根据这个方法去取值
#         if self.start_num < len(self.name): # 索引值不能大于列表的长度
#             a = self.name[self.start_num]
#             self.start_num += 1
#             return  a # 取出类A登记名单
#         else: # 停止for循环无脑取值的方式
#             raise StopIteration
#
# man1 = DiyName()
# # man2 = DiyIter()
# man1.add_name("王一")
# man1.add_name("陈二")
# man1.add_name("张三")
#
# for i in man1:
#     time.sleep(1)
#     print(i)
# # 第一步 判断是否是一个可迭代对象,__iter__
# # 第二步 iter(man1) >>> 得到该实例对象的__iter__的返回值
# # 第三步 返回的这个东西 是否是一个 迭代器 >>> __iter__,__next__
# # 取值的时候 next()
# list()
# str()
#
# # 可迭代对象拥有__iter__方法,
# # 迭代器__iter__ __next__
# # 迭代器一定是可迭代对象(__iter)  可迭代对象就不一定是迭代器
#



# 保存1 到 10000
# list1 = [1,2,3,4,5,6,7,8,9......10000]

# 列表推导式
# list1 = [i for i in range(1,10001)]














