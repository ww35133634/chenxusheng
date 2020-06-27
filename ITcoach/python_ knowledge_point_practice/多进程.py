"""
用多进程完成多任务
"""

import multiprocessing   # 多进程模块
import os
import time


def sing():
    for i in range(3):
        print("bobo老师在唱歌。。。。。。")
        print("sing子进程PID:", os.getpid())   # 查看子进程的ID
        time.sleep(1)


def dance():
    for i in range(3):
        print("bobo老师在跳舞。。。。。。")
        print("dance子进程PID:", os.getpid())
        time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=sing)
    p2 = multiprocessing.Process(target=dance)
    p1.start()
    p1.join(3)   # 确保p1进程执行完毕，参数3是超时等待，超过3秒，程序继续执行
    time.sleep(1)
    p2.start()
    time.sleep(3)
    print("主进程的PID:", os.getpid())
    print("父进程的PID:", os.getppid())  # 即当前程序(pycharm)的进程号


if __name__ == '__main__':
    main()
