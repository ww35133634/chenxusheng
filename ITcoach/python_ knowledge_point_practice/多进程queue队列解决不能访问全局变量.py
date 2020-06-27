"""
多进程间的通信 >>>Queue队列     队列特点：先进先出   CBA >>>CBA
栈  >>>  先进后出
"""
# 队列 >>> 先进先出
# import multiprocessing
# q = multiprocessing.Queue(3)    # 创建 Q队列 对象，参数表示：容器大小,无参数可以无限放。
# # 如何放数据
# q.put()    # 调用Q队列对象的 put方法
# q.full()   # 查看队列是否满了，True 为满
# q.get()    # 取出数据
# q.empty()  # 判断队列为空，True 为空
# q.get_nowait()   #不等待

# import multiprocessing
# # 创建空的容器为3的Q队列
# q = multiprocessing.Queue(3)
# # 存放3个数据
# q.put(123)
# q.put("bobo")
# q.put([4, 5, 6])
# # 取数据  >>> 先进先出
# i = 1
# while not q.empty():
#     print("取出第%d个数据是：%s "%(i,q.get()))
#     i += 1

"""Queue队列应用演示"""

import multiprocessing


def demo1(q):
    # 把获取数据，传入Q队列
    data = [c for c in range(1, 10)]
    for i in data:
        q.put(i)


def demo2(q):
    # 清洗接收队列中的数据，提取数据中的偶数
    even = []
    while not q.empty():
        d = q.get()
        if d % 2 == 0:
            q.put(d)
    #         even.append(d)
    # print(even)


def demo3(q):
    result = []
    while not q.empty():
        result.append(q.get())
    print(result)


def main():
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=demo1, args=(q,))
    p2 = multiprocessing.Process(target=demo2, args=(q,))
    p3 = multiprocessing.Process(target=demo3, args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    p3.start()
    p3.join()


if __name__ == '__main__':
    main()






































