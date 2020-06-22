"""
演示使用生成器里的yield完成多任务
"""
# import time
import time


def sing(): # 生成器模板
    while True:
        print('***我在唱歌***')
        time.sleep(1) # alt
        yield #暂停挂起的机制
def dance():
    while True:
        print('---我在跳舞---')
        time.sleep(1)
        yield
# Thread Process 协程
def main():
    t1 = sing()
    t2 = dance()
    while True:
        try:
            next(t1) # 唤醒生成器
            next(t2)
        except Exception:
            break
if __name__ == '__main__':
    main()
#  并发 假的多任务




























































