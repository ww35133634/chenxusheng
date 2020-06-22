"""
演示多线程的资源竞争问题
"""
import threading
import time
num1 = 0
def demo1(a):
    global num1
    for i in range(a):
        num1 += 1 # 锁住
    print("在demo1中,num1的值为:",num1)
def demo2(a):
    global num1
    for i in range(a):
        num1 += 1 # 锁住
    print("在demo2中,num1的值为:",num1)
def main():
    nums = 1000000
    t1 = threading.Thread(target = demo1, args=(nums,))
    t2 = threading.Thread(target = demo2, args=(nums,))
    t1.start()
    t2.start()
    # 主线程等待两个子线程执行完毕
    time.sleep(5)
    print("在main中,num1的值为:",num1)
if __name__ == '__main__':
    main()



# 多线程的多任务, 是假的多任务 并发 高速切换任务
"""
demo1
num += 1: 原子性
1.程序获取到num1 的值
2.程序会将num1的值跟1相加, 得到一个 新的结果
3.程序将会把新的结果赋值给 num1
"""

"""
demo2
num += 1:
1.程序获取到num1 的值
2.程序会将num1的值跟1相加, 得到一个 新的结果
3.程序将会把新的结果赋值给 num1
"""


# 原子性 >>> 转账
"""
A: 100  

B: 0 
"""













































