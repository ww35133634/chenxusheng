"""
迭代器的应用
"""
# print(range(0, 1000))
# range迭代器 可生成 1000 个数据，但它保存的是生成数据的代码，因此可以节省内存空间

# 例1：迭代器生产斐波那契数列


class Fei_Bo:
    # 斐波那契数列迭代器
    def __init__(self, n):
        self.n = n   # 返回斐波那契第n个的数值
        self.i = 0   # 存放循环自增变量
        self.a = 0   # 存放斐波那契第1个数，初始值赋为0
        self.b = 1   # 存放斐波那契第2个数，初始值赋为1

    def __iter__(self):
        # 迭代器的__iter__返回自身即可
        return self

    def __next__(self):
        if self.i < self.n:
            num = self.a
            self.a, self.b = self.b, self.a + self.b
            self.i += 1
            return num
        else:
            raise StopIteration


num = Fei_Bo(5)
for d in num:
    print(d, end="\t")
