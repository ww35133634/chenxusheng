"""
演示互斥锁
"""

import threading
import time

num1 = 0  # 全局变量 不可变类型

def demo1(a):  # 子线程A 对全局变量进行操作
    global num1
    for i in range(a):
        # 上锁,上完锁之后,,就可以安全的不被CPU强行切换任务
        lock1.acquire()
        num1 += 1  # 锁住他,不让他在执行的时候被强行切换任务
        lock1.release()
        # 开锁,执行完了关键的部分之后,就允许CPU切换任务了
    print('在demo1当中,,num1的值为:',num1)
# 就相当于是单任务,,因为一旦上了锁 整个部分就不会被切换,,其实呢就变成了单任务,,
# 因此 上锁的部分,,代码越少越好
def demo2(a):  # 子线程B 也要对 全局变量进行操作
    global num1
    for i in range(a):
        lock1.acquire()  # 上锁  锁住的部分越少越好  shift + ctrl 上下键移动
        num1 += 1  # 锁住他,不让他在执行的时候被强行切换任务
        # 一个互斥锁,,,两个线程进行抢夺,,谁先抢到,,谁先上锁,,,,
        lock1.release()  # 开锁

    print('在demo2当中,,num1的值为:',num1)

lock1 = threading.Lock()  # 创建一个互斥锁的对象 默认是开锁的
def main():
    num2 = 1000000
    t1 = threading.Thread(target=demo1,args=(num2,))
    t2 = threading.Thread(target=demo2,args=(num2,))
    t1.start()
    t2.start()
    time.sleep(1)
    print('在主线程main当中,,,num1的值为:',num1)

if __name__ == '__main__':
    main()














