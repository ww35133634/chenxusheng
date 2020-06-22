"""
查看线程数量
"""
import threading
import time

def sing():
    for i in range(1,4):
        print("我在唱第%s首歌......" % i)
        time.sleep(1.5)

def dance():
    for i in range(1,4):
        print("我在跳第%s只舞......" % i)
        time.sleep(1.5)

def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    # list1 = threading.enumerate()
    # print(list1)
    while True:
        length = len(threading.enumerate())
        list1 = threading.enumerate()
        print(list1)
        time.sleep(1)
        if length <= 1:
            break
if __name__ == "__main__":
    print("___开始____:%s" % time.ctime())
    main()
    time.sleep(1)


















































