"""
演示类的多线程执行
"""

# import threading
# import time
#
# class A:
#     pass
#
# def sing():
#     for i in range(3):  # 子线程A
#         print('bobo老师在唱歌......')
#         time.sleep(1)
# def dance():
#     for i in range(3):  # 子线程B
#         print('bobo老师在跳舞******')
#         time.sleep(1)
#
# def main():
#     # 1个线程
#     t1 = threading.Thread(target=sing)  # 子线程A  函数的调用 代码的执行 返回值
#     t2 = threading.Thread(target=dance)  # 子线程B  三个线程 多线程
#     t1.start()  # 子线程B启动  可以去执行代码
#     t2.start()  # 子线程B启动  此时此刻 三个线程
#
# if __name__ == '__main__':
#     main()  # 主线程   最后进行一个等待,,, 一起结束

"""
多任务的三个形式:  多线程.  多进程  协程
协程 概念 方式
可迭代对象 >>> 迭代器 >>> 生成器 >>> yiled  >>> yiled多任务  >>> grennlet  >>> gevent 协程 多任务
装饰器有点像,,, 使用十分简单 利用gevent协程完成多任务
分析比较难
"""
"""
想让一个子线程执行多个函数,,
多个函数存在于类当中,,  让子线程去指定类
"""

import threading
import time

# 如果想让子线程可以去一个类里面执行代码,,
class DiyThread(threading.Thread):  # 继承threading模块里面的Thread类
    # 固定的语法格式,,必须拥有
    def run(self):
        for i in range(3):
            print('我是在类里面')
            time.sleep(1)
            # 去打印当前的线程数量,以此来证明子线程可以执行到类里面
            print('当前的线程数量为:',len(threading.enumerate()))

if __name__ == '__main__':
    # 创建子线程
    # threading.Thread()  # 指定执行函数代码的
    t1 = DiyThread()  # 创建出子线程对象
    # 启动子线程 让他去指定的地方执行代码
    t1.start()  # 去到DiyThread 的 run方法里面去执行代码,,,,
    time.sleep(4)
    print('当前的线程数量为:',len(threading.enumerate()))




























































