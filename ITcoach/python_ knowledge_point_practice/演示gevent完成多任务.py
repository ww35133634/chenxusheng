"""
演示协程 gevent

1、gevent 并不像 greenlet 需要手动调用 switch()切换任务。
2、要自动切换任务，前提是 gevent 碰到 延时操作。
3、gevent.sleep(1)  自带的延时操作
"""

# import gevent
# import time
# from gevent import monkey   # 打补丁，将time的延时操作，转化为gevent的延时操作。
#
# monkey.patch_all()   #自动将time的延时操作，转化为gevent的延时操作。
# def sing():
#     for i in range(1, 5):
#         print("bobo老师在唱第%s首歌" % i)
#         time.sleep(1)
#         # gevent.sleep(1)
#
# def dance():
#     for i in range(1, 5):
#         print("bobo老师在跳第%s支舞" % i)
#         time.sleep(1)
#         # gevent.sleep(1)
#
#
# g1 = gevent.spawn(sing)     # 任务做为参数传入
# g2 = gevent.spawn(dance)
#
#
# def main():
#     g1.join()  # 启动协程
#     g2.join()
#
#
# if __name__ == '__main__':
#     main()


"""最终代码优化"""
import gevent
import time
from gevent import monkey  # 打补丁，将time的延时操作，转化为gevent的延时操作。

monkey.patch_all()   # 自动将time的延时操作，转化为gevent的延时操作。


def sing():
    for i in range(1, 5):
        print("bobo老师在唱第%s首歌" % i)
        time.sleep(1)


def dance():
    for i in range(1, 5):
        print("bobo老师在跳第%s支舞" % i)
        time.sleep(1)


def main():
    gevent.joinall([
        gevent.spawn(sing),
        gevent.spawn(dance)
    ])


if __name__ == '__main__':
    main()





