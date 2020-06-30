import multiprocessing


def demo1(q1):  # 提取(创造数据)
    """模拟下载数据"""
    download_data = [i for i in range(1, 11)]
    # 把下载好的数据分别放进队列A当中
    print('放进队列的数据是:', end='')
    for i in download_data:  # 单独的放进了队列
        q1.put(i)
        print(i, end=',')
    print()
    print('数据已经全部放进了队列之中......')


def demo2(q1, q2):  # 清洗数据
    """模拟清洗数据"""
    print('被清洗出来的数据:', end='')
    while True:  # 清洗出来偶数放进队列B
        i = q1.get()  # 只拿一个数据,, 先进先得
        if i % 2 == 0:  # 只要是偶数
            q2.put(i)
            print(i, end=',')
        if q1.empty():  # 如果队列为空, 那么就跳出循环
            break
    print()


def demo3(q2):  # 保存数据
    print('保存进去的数据是:', end='')
    while True:
        j = str(q2.get()) + ','
        print(j, end='')
        with open('bobo.txt', 'a') as file1:
            file1.write(j)
        if q2.empty():
            break


def main():
    # 创建出两个队列
    q1 = multiprocessing.Queue()  # 队列A用来下载好数据后清洗
    q2 = multiprocessing.Queue()  # 队列B用来清洗好数据后保存

    # 创建三个子进程, 进程A提取(创造数据), 子进程B清洗数据,子进程C用来保存数据
    p1 = multiprocessing.Process(target=demo1, args=(q1,))
    p2 = multiprocessing.Process(target=demo2, args=(q1, q2))
    p3 = multiprocessing.Process(target=demo3, args=(q2,))
    p1.start()
    p2.start()
    p3.start()


if __name__ == '__main__':
    main()


# list1 = []
# for i in range(100,200):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#         else:
#             list1.append(i)
# list1 = list(set(list1))
# list1.sort()
# print(len(list1),list1)