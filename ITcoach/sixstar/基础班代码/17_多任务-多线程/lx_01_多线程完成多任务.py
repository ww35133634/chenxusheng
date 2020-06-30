"""
解释性的编程语言
"""

# def demo1():
#     pass
#
# def demo2():
#     pass
#
#
# demo1()  # 先去执行完demo1里面所有的代码  任务
# demo2()  # 再去执行demo2里面所有的代码    任务
# #  单任务

# import time
# # 演示单任务   固有的观念
# def sing():
#     for i in range(3):
#         print('bobo老师在唱歌......')
#         # 设置一个睡眠等待
#         time.sleep(1)  # 1秒钟的程序挂起状态  睡眠
# def dance():
#     for i in range(3):
#         print('bobo老师在跳舞******')
#         time.sleep(1)
#
# def main():  # 单任务 >>> 解释性的编程语言
#     sing()
#     dance()

# 只想调用一个函数 就可以达到让两个函数执行的效果
# 管理一下运行代码  让别人导入咱们这个模块的时候 下面的代码不执行  程序的入口
# if __name__ == '__main__':
#     main()
"""
多任务的效果目的:  唱歌跳舞一起执行 >>> 唱跳歌手
"""

# 想要完成多任务
# 1. 导入一个模块
import threading  # 线程

import time
# 演示单任务   固有的观念
# def sing():
#     for i in range(3):
#         print('bobo老师在唱歌......')
#         # 设置一个睡眠等待
#         time.sleep(1)  # 1秒钟的程序挂起状态  睡眠
# def dance():
#     for i in range(3):
#         print('bobo老师在跳舞******')
#         time.sleep(1)
#
# def main():  # 多线程 >>> 假的多任务 大部分的语言多线程是并行真的多任务
#     # python的解释器 Cpython >>> GIL 全局解释器锁, 保护了线程的安全,,,
#     # 吉多 快速切换  python中的多线程是并发 是假的多任务......
#     t1 = threading.Thread(target=sing)  # 参数 指定一个任务
#     t2 = threading.Thread(target=dance)
#     t1.start()  # 调用此方法可以 启动指定的函数去执行代码
#     t2.start()
#     # sing()
#     # dance()
#
# # 只想调用一个函数 就可以达到让两个函数执行的效果
# # 管理一下运行代码  让别人导入咱们这个模块的时候 下面的代码不执行  程序的入口
# if __name__ == '__main__':
#     main()  # 多任务的表现形式


"""
看似多任务: 同时进行
并发: 假的多任务   两个任务  切换执行,, 看起来是多任务
并行: 真正的多任务 两个任务 真的同时在进行

4个CPU  同时只能执行一个任务
A1  B 3 C5 D7     
2    4    6  8 
0.01S过后 切换
A2 B 4 C6 D8
1   3   5  7  肉眼看上去  切换速度过后,, 

8个任务  每时每刻其实只有四个再执行  但是因为切换速度过快 因为看起来是8个任务同时进行 其实不是 假的多任务


并行: 真的多任务
A  1   B  2   C 3    D 4   真正的同时在执行,,,




"""

"""
解析多线程多任务
"""
# 把程序运行起来之后,,一定会有一个东西去执行代码,,,主线程
# 一个程序可以没有去完成多任务的子线程  >>> 单任务
# 一定不能没有主线程,,
# import threading
# def sing():
#     for i in range(3):
#         print('bobo老师在唱歌......')
#         # 设置一个睡眠等待
#         time.sleep(1)  # 1秒钟的程序挂起状态  睡眠
# def dance():
#     for i in range(3):
#         print('bobo老师在跳舞******')
#         time.sleep(1)
#
# def main():
#     t1 = threading.Thread(target=sing)  # 子线程A 参数 指定一个任务
#     t2 = threading.Thread(target=dance) # 子线程B
#     t1.start()  # 线程启动    调用此方法可以 启动指定的函数去执行代码
#     t2.start()
#     # 子线程的执行先后顺序 由操作系统决定
#
#
# # main TAB自动补全
# if __name__ == '__main__':
#     main()  # 多任务的表现形式
# # 当主线程没有代码执行了,,他会进入一个等待状态,,所有的子线程全部执行完毕死掉之后,, 主线程才会消失,,



"""
当python程序被执行起来,,,就一定有一个东西去执行代码,,,主线程,,,,,
解释性的编程语言
"""
import threading
def sing():
    for i in range(3):  # 子线程A
        print('bobo老师在唱歌......')
        time.sleep(1)
def dance():
    for i in range(3):  # 子线程B
        print('bobo老师在跳舞******')
        time.sleep(1)

def main():
    # 1个线程
    t1 = threading.Thread(target=sing)  # 子线程A  函数的调用 代码的执行 返回值
    t2 = threading.Thread(target=dance)  # 子线程B
    t1.start()  # 子线程B启动  可以去执行代码
    t2.start()  # 子线程B启动  此时此刻 三个线程


if __name__ == '__main__':
    main()  # 主线程   最后进行一个等待,,, 一起结束


