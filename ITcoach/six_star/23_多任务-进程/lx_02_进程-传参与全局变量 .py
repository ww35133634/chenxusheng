"""
演示传参与全局变量
"""

# 演示传参
# import multiprocessing
#
# def demo1(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# def main():
#     p1 = multiprocessing.Process(target=demo1,args=(1,2,3),kwargs={'a':1,"b":2})
#     p1.start()
#
# if __name__ == '__main__':
#     main()



# 演示是否共享全局变量  >>> 证实 不共享全局变量  join()
import multiprocessing
import time

list1 = [1,2,3]

def demo1():
    list1.append(4) # list1 = [1,2,3,4]
    print("在demo1中,list1的值是:",str(list1))

def demo2():
    list1.append(5) # list1 = [1,2,3,4,5]
    print("在demo2中,list1的值是:",str(list1))

def main():
    p1 = multiprocessing.Process(target=demo1)
    p2 = multiprocessing.Process(target=demo2)
    p1.start()
    # 进程等待阻塞的效果
    p1.join() # 可以传参(5) 超时等待
    # time.sleep(1)
    p2.start()

if __name__ == '__main__':
    main()
    time.sleep(3)
    list1.append(6) # list1 = [1,2,3,4,5,6]
    print("在主进程中,list1的值是:",str(list1))

# 队列: 水管, 先进先出,  后进后出....

# 栈  : 先进后出,  后进先出...



















