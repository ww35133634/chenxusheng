"""
演示进程间的通信--利用Queue队列(传送带)
"""
# import multiprocessing
# q = multiprocessing.Queue(3) # 表示的是设置可以存放多少个数据,,
# q.put() # 往队列里面存放数据
# q.full() # 判断队列是否放满
# q.empty()# 判断队列是否为空
# q.get() # 往队列里面拿数据
# q.get_nowait()

# import multiprocessing
#
# # 创建一个队列对象,, 确定范围为3
# q = multiprocessing.Queue(3)
# # 往队列里面放数据
# q.put("hello")
# q.put(123)
# q.put([1,2,3])
#
# # 往队列里面拿数据
# print("队列数据提取1:",q.get())
# print("队列数据提取2:",q.get())
# print("队列数据提取3:",q.get())
# print(q.get())
# q.get()
# q.get_nowait() # 不等待


# 耦合度

# 演示案例
import multiprocessing
def demo1(q): # 见名知意
    """模拟下载数据"""
    data_code = [i for i in range(1,11)]
    # 把下载下来的数据单独放进队列之中
    print(data_code)
    for i in data_code:
        q.put(i)
    print("数据已经全部放进队列之中")

def demo2(q):
    """模拟清洗数据"""
    # 只留下偶数,放进一个列表
    list1 = []
    while True:
        i = q.get()
        if i % 2 == 0: # 清洗过程
            list1.append(i)
    # 如果队列为空,跳出循环
        if q.empty():
            break

    print(list1)

def main():
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=demo1,args=(q,))
    p2 = multiprocessing.Process(target=demo2,args=(q,))
    p1.start()
    p2.start()

if __name__ == '__main__':
    main()





























