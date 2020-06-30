"""
迭代器的应用场景
"""

# range是一个迭代器
# 他可以生成1000W个数据
# 但是他保存的不是具体的1000w个数据,,
# 他保存的是生成这些数据的方法........
# 他并没有使用到需要保存1000W数据的内存空间,,,,代码,,,,
print(range(10000000))


"""
迭代器的应用场景:
迭代器里面保存着的就是生成数据的代码,,
可以达到节约内存的作用......
"""

class FibIterator(object):
    """斐波那契数列迭代器"""

    def __init__(self, n):
        """
        :param n: int, 指明生成数列的前n个数
        """
        self.n = n
        # current用来保存当前生成到数列中的第几个数了
        self.current = 0
        # num1用来保存前前一个数，初始值为数列中的第一个数0
        self.num1 = 0
        # num2用来保存前一个数，初始值为数列中的第二个数1
        self.num2 = 1



    def __next__(self):
        """被next()函数调用来获取下一个数"""
        if self.current < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__返回自身即可"""
        return self



if __name__ == '__main__':
    fib = FibIterator(10)
    for num in fib:
        print(num, end=" ")
















































































