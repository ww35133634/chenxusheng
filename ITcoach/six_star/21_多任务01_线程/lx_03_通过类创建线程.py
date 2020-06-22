"""
演示通过类创建线程
"""
import time
import threading


class DiyThread(threading.Thread):
    def run(self):# 名称固定为run
        for i in range(3):
            time.sleep(1)
            print(threading.enumerate())


if __name__ == "__main__":
    t1 = DiyThread()
    t1.start() # 创建子线程
    time.sleep(5)
    print(threading.enumerate())




















































