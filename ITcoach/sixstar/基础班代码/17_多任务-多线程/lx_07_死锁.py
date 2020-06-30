"""
死锁的演示
"""

import threading
import time

class MyThread1(threading.Thread):  # A任务
    def run(self):  # 子线程A执行这个部分
        # 对mutexA上锁
        mutexA.acquire()

        # mutexA上锁后，延时1秒，等待另外那个线程 把mutexB上锁
        print(self.name+'----do1---up----')
        time.sleep(1)

        # 此时会堵塞，因为这个mutexB已经被另外的线程抢先上锁了
        mutexB.acquire()  # 需要拿到B锁  等待子线程B释放B锁  卡住,等待
        print(self.name+'----do1---down----')
        mutexB.release()

        # 对mutexA解锁
        mutexA.release()  # 必须执行完锁A的释放, 子线程B才可以拿到A锁去执行

class MyThread2(threading.Thread):  # B任务
    def run(self):  # 子线程B执行这个任务
        # 对mutexB上锁
        mutexB.acquire()

        # mutexB上锁后，延时1秒，等待另外那个线程 把mutexA上锁
        print(self.name+'----do2---up----')
        time.sleep(1)

        # 此时会堵塞，因为这个mutexA已经被另外的线程抢先上锁了
        mutexA.acquire()  # 这个部分想要拿到A锁 等待子线程A释放A锁,,卡住,等待
        print(self.name+'----do2---down----')
        mutexA.release()

        # 对mutexB解锁
        mutexB.release()  # 必须执行到这个部分锁B才会释放

mutexA = threading.Lock()  # A锁
mutexB = threading.Lock()  # B锁

if __name__ == '__main__':
    t1 = MyThread1()  # 线程A
    t2 = MyThread2()  # 线程B
    t1.start()
    t2.start()



    # 设置一个超时等待,,,,
    # 避免这种现象



