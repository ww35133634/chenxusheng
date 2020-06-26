"""
一个子线程执行多个函数，多个函数存于类中，让子线程执行指定的类
如果想让子线程执行类里面的代码，
1、需要继承threading模块里面的Thread类
2、类内必须拥有run方法
"""
import threading
import time


class DiyThread(threading.Thread):   # 继承Thread类

    def run(self):     # 固定的语法格式，必须拥有run方法
        for i in range(3):
            self.sing()  # 调用类内的sing()方法
            time.sleep(1)
            print("当前线程数量为", len(threading.enumerate()))

    def sing(self):
        print("bobo老师在唱歌。。。。。。")


t1 = DiyThread()    # 因为继承了threading.Thread类，所以用DiyThread创建子线程
t1.start()

















