"""
演示greenlet 完成多任务，greenlet 对 yield 进行了简单的封装。

1、yield 是利用 暂停 机制，完成多任务
2、greetlet  是利用 切换 机制，完成多任务

"""
from greenlet import greenlet
import time


def sing():
    for i in range(3):
        print("bobo老师在唱歌。。。。。。")
        time.sleep(1)
        g2.switch()


def dance():
    for i in range(3):
        print("bobo老师在跳舞。。。。。。")
        time.sleep(1)
        g1.switch()


g1 = greenlet(sing)  # 创建greenlet类对象，需指定要执行的代码块
g2 = greenlet(dance)


def main():
    g1.switch()  # 调用类的 switch 切换方法，切换到指向执行代码块


if __name__ == '__main__':
    main()









