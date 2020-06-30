"""
演示greenlet 完成多任务
"""
# 1.第三方模块  pip install greenlet -i http//..........

# 2.使用局部导入  为了引导出最终的 gevent
from greenlet import greenlet
import time

def sing():  # 任务A
    while True:
        print('bobo老师在唱歌......')
        time.sleep(0.3)
        g2.switch()  # 切换到对象创建的时候指定的代码部分 执行

def dance():  # 任务B
    while True:
        print('bobo老师在跳舞******')
        time.sleep(0.3)
        g1.switch()  # 切换

g1 = greenlet(sing)  #  创建对象  需要指定执行的代码的部分
g2 = greenlet(dance)
def main():
    # g1.switch()  # 切换到对象创建的时候指定的代码部分 执行
    g2.switch()  # 启动

if __name__ == '__main__':
    main()


"""
利用在各个任务里面进行来回切换,,,达到多任务的效果
greenlet 里面 的 switch方法
"""


# 虚拟环境  pip  第三方库
# 系统环境   并不共享的

# 在系统环境中 的python 解释器 下载了第三方库 在pycharm 不能共享第三方库


"""
为什么要演示yield 完成多任务
greenlet 多任务  对yield进行了简单的封装

"""

"""
利用yield 暂停挂机机制完成多任务
利用greenlet 里面的 切换 完成多任务

协程gevent 完成多任务

"""

