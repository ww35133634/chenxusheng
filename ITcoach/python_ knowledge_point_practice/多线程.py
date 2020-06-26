"""
多线程
"""

import threading  # 多线程模块
import time


def sing():
    for i in range(3):
        print("bobo老师在唱歌。。。。。。")
        time.sleep(1)


def dance():
    for i in range(3):
        print("bobo老师在跳舞。。。。。。")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)  # 创建线程，target参数指定一个任务sing,指向sing代码内存空间，sing后不能加(),加()代表调用函数
    t2 = threading.Thread(target=dance)
    t1.start()   # 调用Thread类内start方法，启动target指向任务的内存空间
    t2.start()

    while True:
        data = threading.enumerate()   # 调用threading类内enumerate函数查看线程
        print(data)
        time.sleep(1.2)
        if len(data) <= 1:
            break


if __name__ == '__main__':
    main()

"""
多线程看似执行多任务，同时进行，其实质是假的多任务，任务间切换执行。称为 >>>并发
并行：真正的多任务，任务同时进行。
"""