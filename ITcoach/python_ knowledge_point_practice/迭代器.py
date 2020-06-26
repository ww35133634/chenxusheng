"""
功能 ：自定义迭代器对象，并用for循环取出存储的值。

可迭代对象包含：__iter__ 方法
迭代器对器包含：__iter__ +  __next__  方法
因此 迭代器对象 就是一个 特殊的 可迭代对象
"""

from collections import Iterable
class DiyIter:

    def __init__(self):
        self.names = []
        self.start_num = 0

    def add_name(self, name):
        self.names.append(name)

    def __iter__(self):
        return self    # self 代表返回自身，供__next__方法调用自身

    def __next__(self):
        if self.start_num < len(self.names):
            a = self.names[self.start_num]
            self.start_num += 1
            return a
        else:
            raise StopIteration  # 当超出取值范围，就停止迭代


name = DiyIter()  # 实例对象
print(isinstance(name, Iterable))  # 判断实例对象是不是可迭代对象，True为真
name.add_name("bobo")  # 调类方法添加元素
name.add_name("sisi")
name.add_name("python")
for n in name:
    print(n)

"""
for循环的原理
1,判断是否是一个可迭代对象,,,  __iter__ 方法           √
2,自动调用iter()函数,, 得到__iter__方法的返回值,,
3,这个返回值,, 需要是一个迭代器对象  __iter__ 加 __next__方法
4.取值的时候,,会怎样去做,,,,取值就跟迭代器相关了,,,
for 循环取值的最终原理,
自动死循环调用next()函数,,,来触发__next__方法,,,取到里面的值,,,,
"""