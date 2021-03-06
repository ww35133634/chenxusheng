"""
演示进程池Pool
"""

# 特殊的容器, 容纳一定数量的进程  >>> 完成任务
# 重复利用进程池里面的进程,, 完成多个任务的目的
# 100任务
# 进程池 5 进程 节约大量的资源 重复利用进程来完成多个任务
# 减轻操作系统调度的压力

"""
100人去团建(任务)  骑马     1个小时 100  10分钟  6  
马棚(进程池)  马(进程)
100马 >>> 你们的老板不会这样做,,  极大的资源的浪费,,

租一个小的马棚(进程池)  10 匹 马 10进程
 1个进程   10任务  100人
 
极大的节约资源  10个进程
"""

# 创建一个进程池  >>> 准备一些进程
# 来了大量的任务 不停的去执行,,, 执行完毕 圆满了


import multiprocessing
import os, time, random


def demo(msg):
    t_start = time.time()  # 记录此时的时间
    print("%s开始执行,进程号为%d" % (msg, os.getpid()))  # 打印完成这个任务的此时的进程号是多少,
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random() * 2)  # 随机数字,,让程序休眠挂起
    t_stop = time.time()  # 记录一下此时的时间
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))  # 执行一个任务所用到的时间


if __name__ == '__main__':

    po = multiprocessing.Pool(3)  # 定义一个进程池，最大进程数3
    for i in range(1, 11):  # 一共十个任务
        # 实例对象.apply_async(要调用的目标,(传递给目标的参数元祖,))
        # 每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(demo, (i,))  # 启动进程池里的进程去执行任务
        # t1.start() p1.start


    print("----start----")
    po.close()  # 关闭进程池，关闭后po不再接收新的请求
    po.join()  # 等待po中所有子进程执行完成，必须放在close语句之后
    print("-----end-----")


"""
利用进程池里面的进程 重复完成任务,,,,
减少了大量的创建和释放进程资源的过程 大大的提高了效率,,,


5 个任务  进程池  


100000  进程池


"""




