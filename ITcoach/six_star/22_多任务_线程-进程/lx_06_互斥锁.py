"""
演示互斥锁
"""
# 默认是没有上锁 acquire()
# 开锁 release()
import threading
import time
num1 = 0


def demo1(a):
    # lock_1.acquire()  # 上锁
    global num1
    for i in range(a):
        lock_1.acquire() # 上锁
        num1 += 1 # 锁住 保持原子性
        lock_1.release() # 开锁
    print("在demo1中,num1的值为:",num1)
    # lock_1.release()  # 放锁


def demo2(a):
    # lock_1.acquire()  # 上锁
    global num1
    for i in range(a):
        lock_1.acquire() # 上锁
        num1 += 1 # 锁住 保持原子性
        lock_1.release() # 开锁
    print("在demo2中,num1的值为:",num1)
    # lock_1.release()  # 开锁

# 创建一个互斥锁,,默认是不上锁的状态
lock_1 = threading.Lock()


def main():
    nums = 1000000
    t1 = threading.Thread(target = demo1, args=(nums,))
    t2 = threading.Thread(target = demo2, args=(nums,))
    t1.start()
    t2.start()
    # 主线程等待两个子线程执行完毕
    time.sleep(2)
    print("在main中,num1的值为:",num1)


if __name__ == '__main__':
    main()


# 锁住的代码越少越好,,







































