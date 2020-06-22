"""
演示多任务
"""
# 程序睡眠等待
import time
import threading

# 多任务

def sing():
    for i in range(3):
        print("我在唱歌......")
        time.sleep(2)

def dance():
    for i in range(3):
        print("我在跳舞......")
        time.sleep(2)

def main(): # threading → 线程 看似多任务
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start() # 开始 创建出了一个线程>> 执行代码
    t2.start()
    # sing()
    # dance()

# 运行代码的管理
if __name__ == "__main__": # 是否是在本环境在执行
    main()

# 并发 qq 微信  CPU  单核CPU 双核CPU 四核
"""
一个CPU  0.01 0.02 并发 假的多任务       CPU A qq   CPU b 微信  并行 真正的多任务
线程 看似多任务 Cpython>>> GIL 全局解释器锁  肉眼不可见的切换任务的现象 


"""





































# 单任务
# def sing():
#     for i in range(3):
#         print("我在唱歌......")
#         time.sleep(1)
#
# def dance():
#     for i in range(3):
#         print("我在跳舞......")
#         time.sleep(1)
#
# def main():
#     sing()
#     dance()
#
# if __name__ == "__main__":
#     main()


# 多任务





























