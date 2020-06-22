"""
演示greenlet实现多任务
"""
# 第三方库 pip install 默认国外镜像源下载
# 导入的是greentlet模块里面的greenlet类

from greenlet import greenlet
import time

def sing():
    while True:
        print('***我在唱歌***')
        time.sleep(0.5)
        g2.switch()
def dance():
    while True:
        print('---我在跳舞---')
        time.sleep(0.5)
        g1.switch()
g1 = greenlet(sing)
g2 = greenlet(dance)

def main():
    g1.switch() # 切换的方法
if __name__ == '__main__':
    main()





















