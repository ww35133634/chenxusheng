"""
演示可迭代对象和迭代器
"""

"""
for循环的原理
"""
list1 = [4, 5, 6]
# 迭代取值  在原有的情况下增加东西,,,
# 迭代版本
# QQ 1.1 >>> 1.2  原有的东西上去增加东西
# for i in list1:  # list1可以让for循环去迭代取值 列表
#     print(i)

# 换成一个整型
# for i in 100:  # 整型对象不是一个可迭代对象  >>>
#     print(i)


# 只有可迭代对象iterable才能够被for循环去进行迭代

# 列表, 元组, 集合
from collections import Iterable

#      判断      数据        身份
# print(isinstance(range(10), Iterable))
# print(isinstance('武汉加油', Iterable))

# 只有可迭代对象才能够被for循环操作
# 可迭代对象,,,

# 想要被for循环成功的迭代
# 1.该对象必须是一个可迭代对象


"""
自定义可迭代对象
"""

# for i in xxx:
#          Iterable
#          列表 字典 字符串 元组  ..... python自带

# 想自己创建一个对象,,, 可迭代对象,,,,

# 怎么样才能够称为一个可迭代对象,,,,
# 在类里面写一些方法,,  可以把里面的数据,,迭代取出
# class Diy:
#     def __init__(self):
#         self.names = []
#
#     # 定义一个实例方法,,,
#     def add_name(self, name):
#         # 调用实例方法,,添加姓名进列表
#         self.names.append(name)
#
#     # 只要拥有了__iter__方法,那么就能够成为一个可迭代对象
#     def __iter__(self):
#         pass
#
#
#
# # from collections import Iterable  # 是否是可迭代对象
#
# man1 = Diy()  # 一个自定义对象  此时的man1已经是一个可迭代对象了,,,
# man1.add_name('bobo')
# man1.add_name('sisi')
# man1.add_name('python')
#
# # print(isinstance(man1, Iterable))
# # 使用for循环迭代自定义对象,,就能把里面的数据取出来
# for i in man1:  # 里面没有可迭代的数据
#     print(i)
"""
在没有__iter__方法之前,TypeError: 'Diy' object is not iterable
在拥有了__iter__方法之后,TypeError: iter() returned non-iterator of type 'NoneType'
# 怎么样才能够称为一个可迭代对象,,,,
为什么自定义对象已经成为了可迭代对象,,但是还不能够使用for循环迭代取值了,,

"""

# class Diy:
#     def __init__(self):
#         self.names = []
#
#     # 定义一个实例方法,,,
#     def add_name(self, name):
#         # 调用实例方法,,添加姓名进列表
#         self.names.append(name)
#
#     # 只要拥有了__iter__方法,那么就能够成为一个可迭代对象
#     def __iter__(self):
#         pass  # 需要一个返回值
#
# man1 = Diy()
# man1.add_name('bobo')
# man1.add_name('sisi')
# man1.add_name('python')
# for i in man1:
#     print(i)


"""
for循环的原理
列表已经是一个可迭代对象了,,,
1,判断是否是一个可迭代对象,,,  __iter__ 方法           √
2,自动调用iter()函数,, 得到__iter__方法的返回值,,
3,这个返回值,, 需要是一个迭代器对象
"""

# for i in [1, 2, 3]:
#     print(i)

"""
迭代器,,,,
可迭代对象  >>>  __iter__
迭代器      >>>  __iter__  +  __next__
"""

# class Diy:  # 可迭代对象
#     def __init__(self):
#         self.names = []
#
#     # 定义一个实例方法,,,
#     def add_name(self, name):
#         # 调用实例方法,,添加姓名进列表
#         self.names.append(name)
#
#     # 只要拥有了__iter__方法,那么就能够成为一个可迭代对象
#     def __iter__(self):
#         return DiyIter() # 需要一个返回值  __iter__  +  __next__
#
# class DiyIter:  # 迭代器
#     def  __iter__(self):
#         pass
#
#     def __next__(self):  # 是否真的是__next__方法里面的代码控制着数据的迭代
#         return '武汉加油'
#
# man1 = Diy()
# man1.add_name('bobo')
# man1.add_name('sisi')
# man1.add_name('python')
# for i in man1:
#     print(i)

"""
for循环的原理
列表已经是一个可迭代对象了,,,
1,判断是否是一个可迭代对象,,,  __iter__ 方法           √
2,自动调用iter()函数,, 得到__iter__方法的返回值,,
3,这个返回值,, 需要是一个迭代器对象  __iter__ 加 __next__方法

4.取值的时候,,会怎样去做,,,,取值就跟迭代器相关了,,,
for 循环取值的最终原理,
自动死循环调用next()函数,,,来触发__next__方法,,,取到里面的值,,,,
"""

"""
1.for循环去迭代取值咱们的自定义对象的时候,,,已经没有报错了,,,
问题 : 如何去正确的取值,,,,
2.已经知道了for循环迭代取值是跟迭代器里面的__next__方法相关的,,,,
3.成功的取到了我们想要的自定义对象里面的数据
4.想要迭代得到的是里面所有的数据,,,并不是一味的死循环一个....
5.死循环的调用next()函数 来取值.. 所以导致列表的索引超出了范围

"""
#
# class Diy:  # 可迭代对象  A类
#     def __init__(self):
#         self.names = []
#     def add_name(self, name):  # 定义一个实例方法,,,
#         # 调用实例方法,,添加姓名进列表
#         self.names.append(name)
#     def __iter__(self):  # 只要拥有了__iter__方法,那么就能够成为一个可迭代对象
#         return DiyIter(self) # A类实例 init方法被调用
# class DiyIter:  # 迭代器  B类 里面的 __next__ 方法 去拿到 A类里面的数据
#     def __init__(self,obj):  # 利用传参来得到数据...A类的实例 取到A类里面的数据
#         self.obj = obj  # 保存着A类的实例对象,,里面的数据都在
#         self.start_num = 0          # 定义一个初始的索引值
#     def  __iter__(self):
#         pass
#     def __next__(self):  # 是否真的是__next__方法里面的代码控制着数据的迭代
#         # 索引自增,,才能够往后取值.....
#         #     索引3  第四个数据                      3
#         if self.start_num < len(self.obj.names):
#             a = self.obj.names[self.start_num]  # 取到索引为0的数据
#             self.start_num += 1  # 索引的自增
#             return a  # return过后的代码,,,
#         else:  # 当超出了取值范围 那么就停止迭代
#             raise StopIteration  # 停止你的迭代
#
# man1 = Diy()
# man1.add_name('bobo')
# man1.add_name('sisi')
# man1.add_name('python')
# # 自定义了一个对象,,  然后可以使用for 循环 对其迭代取值......
# for i in man1:
#     print(i)


"""
优化
"""


# 如果本身就是一个迭代器对象,,那么__iter__里面返回自身是不是就可以了啊,,
class DiyIter:  # 迭代器  B类 里面的 __next__ 方法 去拿到 A类里面的数据
    def __init__(self):  # 利用传参来得到数据...A类的实例 取到A类里面的数据
        self.names = []
        self.start_num = 0  # 定义一个初始的索引值

    def add_name(self, name):  # 定义一个实例方法,,,
        self.names.append(name)  # 调用实例方法,,添加姓名进列表

    def __iter__(self):
        return self  # 代表返回自身

    def __next__(self):  # 是否真的是__next__方法里面的代码控制着数据的迭代
        # 索引自增,,才能够往后取值.....
        #     索引3  第四个数据                      3
        if self.start_num < len(self.names):
            a = self.names[self.start_num]  # 取到索引为0的数据
            self.start_num += 1  # 索引的自增
            return a  # return过后的代码,,,
        else:  # 当超出了取值范围 那么就停止迭代
            raise StopIteration  # 停止你的迭代


man1 = DiyIter()
man1.add_name('bobo')
man1.add_name('sisi')
man1.add_name('python')
# 自定义了一个对象,,  然后可以使用for 循环 对其迭代取值......
# for i in man1:
#     print(i)
a = next(man1)
print(a)
b = next(man1)
print(b)
c = next(man1)
print(c)
# d = next(man1)
# print(d)  # None
"""
可迭代对象 :  __iter__
迭代器对象(可迭代对象) : __iter__  + __next__

for循环的原理:
1.判断对象是否是可迭代对象
2.iter()函数得到返回值,返回值需要是迭代器对象
3.自动调用next()去得到__next__里面的返回值
"""
