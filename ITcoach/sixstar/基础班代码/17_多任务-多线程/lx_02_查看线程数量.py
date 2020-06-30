"""
演示查看线程数量
"""

import threading
import time


def sing():
    for i in range(3):  # 子线程A
        print('bobo老师在唱歌......')
        time.sleep(1)
def dance():
    for i in range(3):  # 子线程B
        print('bobo老师在跳舞******')
        time.sleep(1)

def main():
    # 1个线程
    t1 = threading.Thread(target=sing)  # 子线程A  函数的调用 代码的执行 返回值
    t2 = threading.Thread(target=dance)  # 子线程B
    t1.start()  # 子线程B启动  可以去执行代码
    t2.start()  # 子线程B启动  此时此刻 三个线程
    while True:  # python文件
        data = threading.enumerate()  # 是一个函数
        data1 = len(data)  # 根据列表的长度来判断此时此刻有多少个线程存在
        print('此时此刻线程的数量为:', data1)
        print(data)
        time.sleep(1.2)
        if data1 <= 1:  # 证明子线程执行完毕 死掉了, 只剩了一个主线程
            break
if __name__ == '__main__':
    main()  # 主线程   最后进行一个等待,,, 一起结束









