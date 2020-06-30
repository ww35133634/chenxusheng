# """
# 演示Queue队列
# """
#
# # 容器, 存放数据 先进先出
# # 队列是让多进程之间彼此交互数据的
#
# # 队列的创建
# # import multiprocessing
# # q = multiprocessing.Queue(3)  # 划分空间 可以自己去设置队列容器的大小 只能存放三个数据
# #
# # # 如何往队列里面放数据
# # q.put()  # 函数1, 方法2
# #
# # # 如何查看队列里面满了
# # q.full()  # 满了 True  False
# #
# # # 貔貅 只进不出  取得队列里面的数据
# # q.get()
# #
# # # 是否可以判断队列为空
# # q.empty()  # True  False
#
# # get_nowait
#
#
# """
# 演示队列的方法效果
# """
# import multiprocessing
#
# q = multiprocessing.Queue(3)
# # 有了空队列, 容量为三
#
# # 往队列里面放数据
# q.put(123)  # 1
# q.put('bobo')  # 2
# q.put([4, 5, 6])  # 3
#
# # 往队列里面取数据出来  >>> 先进先出  后进后出
# print('队列里取出来的第一个数据是:', q.get())
# print('队列里取出来的第二个数据是:', q.get())
# print('队列里取出来的第三个数据是:', q.get())
#
# # 队列为空, 还去取数据
# # q.get()  # 程序在这个地方 卡住了 进行一个等待
# q.get_nowait()  # 不等待 如果我们截取到了异常, 那么是不是就意味着队列里面没有东西
#
#


"""
只是一个演示案例
"""
# 1.单独的容器, 作为一个通道, 交流的桥梁. 可以让进程之间完成通信
# 2.耦合度,  尽可能的降低耦合度 ,,
# 相互影响,,,        A    B没有问题,,,不影响
# 先进先出 后进后出  >>>  出去了就出去了不要再存在 避免重复数据的提取,,,,
# A进程 >> 队列  爬取 B清洗 从队列拿 , C保存
#    D进程 队列   B     灵活的作用 不让彼此之间依赖关系过重

"""
进程A, 提取数据 创造数据  >>> 队列
进程B, 清洗数据 
"""

import multiprocessing


def demo1(q):  # 提取(创造数据)
    """模拟下载数据"""
    download_data = [i for i in range(1, 11)]
    # 把下载好的数据分别放进队列当中
    for i in download_data:  # 12345678910 单独的放进了队列
        q.put(i)
        print('放进队列的数据是:',i)
    print('数据已经全部放进了队列之中......')


def demo2(q):  # 清洗数据
    """模拟清洗数据"""
    # 只想要偶数,把他放进一个列表,打印出来
    list1 = []
    while True:
        i = q.get()  # 只拿一个数据,, 先进先得
        if i % 2 == 0:  # 只要是偶数
            list1.append(i)  # 那么就放到列表里面去
            print('此时此刻的list1里面是:',list1)
        # 如果队列为空, 那么就跳出循环
        if q.empty():
            break
    print('清洗完的数据是:', list1)


def main():
    # 创建一个队列
    q = multiprocessing.Queue()
    # 创建两个子进程, 进程A提取(创造数据), 子进程B清洗数据
    p1 = multiprocessing.Process(target=demo1, args=(q,))
    p2 = multiprocessing.Process(target=demo2, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()

# ctrl + A 选中全部,  ctrl +alt + L 规范格式
