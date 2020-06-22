"""
演示gevent完成多任务
"""

# import gevent
# import time
#
# def sing():
#     for i in range(1,6):
#         print('***我在唱第%s首歌***' % i)
#         time.sleep(0.5)
#         # gevent.sleep(0.5)
#
# def dance():
#     for i in range(1,6):
#         print('---我在跳第%s只舞---' % i)
#         # time.sleep(0.5)
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


# 打补丁
import gevent
import time
from gevent import monkey

monkey.patch_all()
def sing():
    for i in range(1, 6):
        print('***我在唱第%s首歌***' % i)
        time.sleep(0.5) # >>> gevent.sleep()
        # gevent.sleep(0.5)


def dance():
    for i in range(1, 6):
        print('---我在跳第%s只舞---' % i)
        time.sleep(0.5)
        # gevent.sleep(0.5)


# g1 = gevent.spawn(sing)
# g2 = gevent.spawn(dance)
#
#
# def main():
#     g1.join()
#     g2.join()
def main():
    gevent.joinall([
        gevent.spawn(sing),
        gevent.spawn(dance)
    ])


if __name__ == '__main__':
    main()



























































































