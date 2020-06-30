"""
演示多进程完成多任务
"""
import time
import multiprocessing

def sing():
    for i in range(3):
        print('bobo老师在唱歌......')
        time.sleep(1)

def dance():
    for i in range(3):
        print('bobo老师在跳舞******')
        time.sleep(1)

def main():
    # 利用多进程去完成多任务
    p1 = multiprocessing.Process(target=sing)  # 创建子进程A对象  等待
    p2 = multiprocessing.Process(target=dance)  # 创建子进程B对象 等待
    p1.start()  # 启动子进程A去指定的部分执行代码
    p2.start()  # 启动子进程A去指定的部分执行代码

if __name__ == '__main__':
    main()
















































