"""
演示多线程共享全局变量
"""
# import threading
# import time
#
# num1 = 0
# def demo1():
#     global num1
#     num1 += 1
#     print("在demo1中,num1的值是:",num1)
#
#
# def demo2():
#     print("在demo2中,num1的值是:",num1)
#
#
# def main(): #主程序函数
#     t1 = threading.Thread(target=demo1)
#     t2 = threading.Thread(target=demo2)
#     t1.start()
#     time.sleep(1)
#     t2.start()
#     time.sleep(1)
#     print("在main中,num1的值是:",num1)
#
# # 运行代码管理
# if __name__ == "__main__":
#     main()


# 参数和多线程的关系

import threading
import time

num1 = 0
def demo1(a):
    global num1
    num1 += 1
    a.append(4)
    print("在demo1中,list1是:",str(a))

    print("在demo1中,num1的值是:",num1)


def demo2(a):
    print("在demo2中,list1是:",str(a))
    print("在demo2中,num1的值是:",num1)


def main(): #主程序函数
    list1 = [1,2,3]
    # 在target执行将来执行这个子线程创建之后去哪里执行代码
    # args指定将来调用函数的时候, 将什么数据传递过去
    t1 = threading.Thread(target=demo1,args=(list1,)) # 元组
    t2 = threading.Thread(target=demo2,args=(list1,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("在main中,num1的值是:",num1)

# 运行代码管理
if __name__ == "__main__":
    main()

# 四口人  一个电视机  资源竞争的问题































# 不可变类型
# num1 = 10
#
# def demo1():
#     global num1
#     num1 = 20
#
# demo1()
# print(num1)

# 可变类型
# list1 = [1,2,3]
#
# def demo1():
#     list1.append(4) # 内存地址
#
# demo1()
# print(list1)

























































