"""
演示协程gevent
"""

# 1.第三方  pip install gevent

# 导入
# import gevent
# import time  # 为什么需要导入
#
# # 目的 一边唱歌  一边跳舞 达到多任务的目的
# def sing():
#     for i in range(1,6):
#         print('bobo老师在唱第%s首歌......' % i)
#
# def dance():
#     for i in range(1,6):
#         print('bobo老师在跳第%s只舞******' % i)
#
# g1 = gevent.spawn(sing)  # 任务作为参数传进入
# g2 = gevent.spawn(dance)  # 跟子线程  子进程的创建十分的想象 对greenlet
# # gevent 对greenlet 进行封装 实际上呢 就是想利用 切换 多任务的 目的
# # 优点是 并不像greenlet一样 需要手动调用swtich() 去进行切换 >>> 自动切换的目的
# # 自动切换的目的 并没有触发到自动切换任务的条件,,,
# # 在碰到延时操作的时候 就会自动切换任务  达到多任务的效果
# def main():
#     g1.join()  # 用来启动
#     g2.join()
#     # sing()  start()
#     # dance()
# if __name__ == '__main__':
#     main()



"""
延时操作 导致 自动切换任务 达到多任务的效果
"""
import gevent
import time  # 为什么需要导入


# 目的 一边唱歌  一边跳舞 达到多任务的目的
# def sing():
#     for i in range(1, 6):
#         print('bobo老师在唱第%s首歌......' % i)
#         # time.sleep(0.5)  # 具备了延时操作
#         gevent.sleep(0.5)  # gevent 自带的延时操作, 切换任务
#
# def dance():
#     for i in range(1, 6):
#         print('bobo老师在跳第%s只舞******' % i)
#         # time.sleep(0.5)
#         gevent.sleep(0.5)
# g1 = gevent.spawn(sing)  # 任务作为参数传进入
# g2 = gevent.spawn(dance)  # 跟子线程  子进程的创建十分的想象 对greenlet
#
#
# # gevent 对greenlet 进行封装 实际上呢 就是想利用 切换 多任务的 目的
# # 优点是 并不像greenlet一样 需要手动调用swtich() 去进行切换 >>> 自动切换的目的
# # 自动切换的目的 并没有触发到自动切换任务的条件,,,
# # 在碰到延时操作的时候 就会自动切换任务  达到多任务的效果
# # gevent 只承认自己的延时操作
# def main():
#     g1.join()
#     g2.join()
#
# if __name__ == '__main__':
#     main()

















# import gevent
# import time  # 为什么需要导入
#
#
# # 目的 一边唱歌  一边跳舞 达到多任务的目的
# def sing():
#     for i in range(1, 6):
#         print('bobo老师在唱第%s首歌......' % i)
#         gevent.sleep(0.5)  # gevent 自带的延时操作, 切换任务
#
# def dance():
#     for i in range(1, 6):
#         print('bobo老师在跳第%s只舞******' % i)
#
#         gevent.sleep(0.5)
# g1 = gevent.spawn(sing)
# g2 = gevent.spawn(dance)
#
# def main():
#     g1.join()
#     g2.join()
#
# if __name__ == '__main__':
#     main()

# 单进程 单线程 的情况 下 利用 切换 就达到了多任务的效果
"""
gevent协程 也可以完成多任务
"""

"""
cmd pip 下载 
pycharm 指定的 解释器又不是同一个 
"""

"""
IO密集型
计算密集型

协程 依赖 线程 , 线程 依赖 进程
进程耗费资源最大
线程次之
协程是最少, 方法的调用 达到切换的目的

多任务
多进程  子进程  代码  资源 
多线程  子线程  资源的产生
协程  利用 是延时操作 自己的gevent里面的延时操作,, 十分不方便
"""

# IO  input  ouput 读写的 时间的浪费,,,
# 是否可以让原来的延时操作 来 触发 gevent的切换呢,,,
# 网络接收的堵塞

# 利用打补丁 来  触发 原生的延时操作



import gevent
import time  # 为什么需要导入
from gevent import monkey
# 打补丁
monkey.patch_all()  # 将程序当中的原生延时操作,,通通自动转化为gevent自己的延时操作
# 目的 一边唱歌  一边跳舞 达到多任务的目的
def sing():
    for i in range(1, 6):
        print('bobo老师在唱第%s首歌......' % i)
        time.sleep(0.5)  # >>> gevent.sleep()

def dance():
    for i in range(1, 6):
        print('bobo老师在跳第%s只舞******' % i)
        time.sleep(0.5)
# g1 = gevent.spawn(sing)
# g2 = gevent.spawn(dance)

def main():
    # g1.join()
    # g2.join()
    gevent.joinall([
        gevent.spawn(sing),
        gevent.spawn(dance),
    ])
if __name__ == '__main__':
    main()


# 协程完成多任务,, 利用延时操作切换任务 达到所任务的效果

