"""
解决 多线程  对同一个全局变量操作，造成资源竞争。
"""
import threading
import time



num = 0  #全局变量


def demo1(x):
    global num   # 用global升级成全局变量
    for i in range(x):
        lock1.acquire()   # 上锁
        num += 1
        lock1.release()   # 开锁
    print("在demo1内num的值是：", num)

def demo2(x):
    global num   # 用global升级成全局变量
    for i in range(x):
        lock1.acquire()   # 上锁
        num += 1
        lock1.release()   # 开锁
    print("在demo2内num的值是：", num)


lock1 = threading.Lock()     # 创建锁  上锁后，代码就不会被强制切换
def main():
    times = 1000000
    t1 = threading.Thread(target=demo1, args=(times,))
    t2 = threading.Thread(target=demo2, args=(times,))
    t1.start()
    time.sleep(0.1)
    t2.start()
    time.sleep(3)
    print("在主线程内num的值是：", num)


if __name__ == '__main__':
    main()


















