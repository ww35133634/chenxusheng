"""
演示查看进程号
"""

import time
import multiprocessing
import os

# 证明多进程  就去查看他的进程号
def sing():  # 子进程A 来执行
    for i in range(3):
        print('bobo老师在唱歌......,执行他的进程号是:',os.getpid())  # 得到此时的进程的进程号
        time.sleep(1)

def dance():  # 子进程B 来执行的
    for i in range(3):
        print('bobo老师在跳舞******,执行他的进程号pid是:',os.getpid())
        time.sleep(1)

def main():  # 主进程来执行
    # 利用多进程去完成多任务
    p1 = multiprocessing.Process(target=sing)  # 创建子进程A对象  等待
    p2 = multiprocessing.Process(target=dance)  # 创建子进程B对象 等待
    p1.start()  # 启动子进程A去指定的部分执行代码
    p2.start()  # 启动子进程A去指定的部分执行代码
    time.sleep(1)
    print('主进程的pid,进程号是:',os.getpid())
    print('父进程的进程号pid是:',os.getppid())
if __name__ == '__main__':
    main()