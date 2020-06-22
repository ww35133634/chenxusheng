"""
演示多进程完成多任务
"""
import multiprocessing
import time
# 通过一个进程号去判断
import os
# 多进程完成多任务
def sing():
    for i in range(1,4):
        print("我正在唱第%s首歌" % i)
        print("进程在sing中运行, 进程号pid为:",os.getpid()) # 获取当前进程号
        time.sleep(1.5)

def dance():
    for i in range(1,4):
        print("我正在跳第%s只舞" % i)
        print("进程在dance中运行, 进程号pid为:",os.getpid()) # 获取当前进程号

        time.sleep(1.5)

def main():
    print("进程在main中运行, 进程号pid为:", os.getpid()) # 获取当前进程号

    p1 = multiprocessing.Process(target = sing)
    p2 = multiprocessing.Process(target = dance)
    p1.start()
    p2.start()
    time.sleep(5)
    print("进程在main中运行, 进程号pid为:", os.getpid()) # 获取当前进程号

    # sing()
    # dance()

if __name__ == '__main__':
    main()





























































