"""
演示多进程是否能够共享全局变量
"""
import multiprocessing
# 全局变量
import time

list1 = [1,2,3]

def demo1():
    # 添加一个元素4
    list1.append(4)
    print('在demo1函数中,list1的值是:,',list1)

def demo2():
    # 添加一个元素5
    list1.append(5)
    print('在demo2函数中,list1的值是:,',list1)

def main():
    p1 = multiprocessing.Process(target=demo1)  # 子进程A准备就绪
    p2 = multiprocessing.Process(target=demo2)  # 子进程B准备就绪
    p1.start()  # [1,2,3,4]
    # time.sleep(1)  # 为了让上面的进程先执行完毕  时间的浪费
    p1.join()  # 就能够确保p1进程执行完毕
    p2.start()  # [1,2,3,4,5]
    p2.join(5)  # 堵塞的效果,, 确保改进程执行完毕  超时等待 >>>  5s过后 继续往下走
    # time.sleep(1)

    list1.append(6)  # [1,2,3,4,5,6]
    print('在main函数中,list1的值是:,',list1)
if __name__ == '__main__':
    main()


#  选中 time alt + 回车
"""
多进程是并不能去共享全局变量

就安全性来言,,,
互不干扰的多进程,,,是最安全的,,,
多线程相对来说就没有那么安全,,,


进程是系统进行资源(CPU 网络 运行内存空间 摄像头)分配和调度的一个独立单位. 基本单位

线程是进程的一个部分,,是CPU调度的基本单元  CPU去执行 线程


理想状态下,,, 多进程是可以完成真正的多任务的  并行

100核CPU    100进程  并行 真正的多任务  
线程         并发  假的多任务



"""



























































