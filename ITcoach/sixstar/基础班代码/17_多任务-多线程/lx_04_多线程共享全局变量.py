"""
演示多线程共享全局变量
"""

# a = 1  # 全局变量
#
# def demo():
#     b = 1  # 局部变量

# 单线程 -- 全局变量
# num1 = 1
#
# def demo1():
#     # 升级成全局变量
#     global num1  # 局部变量 >>> 全局变量
#     num1 += 1
#     print('在demo1当中,,num1的值为:',num1)
#
# def demo2():
#     print('在demo2当中,,num1的值为:',num1)
#     # 拿到的就是demo1中修改过后的全局变量的结果
# def main():
#     demo1()  # 先修改 再打印      2
#     demo2()  # 打印修改过后的值   2
#
# if __name__ == '__main__':
#     main()

# 单线程 只有一个主线程去执行代码,,,毫无疑问,,两个函数可以共享全局变量
import time

"""
多线程  -- 全局变量
"""

# import threading
# num1 = 1
#
# def demo1():
#     global num1  # 局部变量 >>> 全局变量
#     num1 += 1
#     print('在demo1当中,,num1的值为:',num1)
#
# def demo2():
#     print('在demo2当中,,num1的值为:',num1)
#
# def main():
#     # 创建两个子线程,,分别去执行demo1函数 和 demo2函数
#     t1 = threading.Thread(target=demo1)  # 子线程A去修改全局变量
#     t2 = threading.Thread(target=demo2)  # 子线程B去打印全局变量  是否是修改过后的值
#     t1.start()
#     time.sleep(0.1)  # 手动加上一个延迟,,避免子线程B demo2 里面的代码先被执行
#     t2.start()
# if __name__ == '__main__':
#     main()

# 子线程B当中打印的是被子线程A修改过后的全局变量,,
# 证明了多线程之间是共享全局变量
"""
demo2,子线程B先去执行,,,  1
demo1 子线程A去修改       2
"""



"""
多线程传参的问题
"""
import threading

list1 = [1,2,3]  # 全局变量 可变类型  不需要通过global去指定为全局变量进行操作

def demo1(i):
    list1.append(i)
    print('在demo1当中,,list1的值为:',list1)

def demo2():
    print('在demo2当中,,list1的值为:',list1)

def main():
    # 创建两个子线程,,分别去执行demo1函数 和 demo2函数
    # target是用来指定将来子线程去哪里执行代码
    # args是传参的
    t1 = threading.Thread(target=demo1,args=(4,))  # 子线程A去修改全局变量
    t2 = threading.Thread(target=demo2)  # 子线程B去打印全局变量  是否是修改过后的值
    t1.start()  # list1追加数据  4  >>> [1,2,3,4]
    time.sleep(0.1)  # 手动加上一个延迟,,避免子线程B demo2 里面的代码先被执行
    t2.start()  # [1,2,3,4]
if __name__ == '__main__':
    main()

# 多线程共享全局变量
"""
爬虫
1. 爬取数据  100     100   10  A
2. 清洗数据  100           10  B
3. 保存      100           10  C
提高效率 >>> 多线程共享全局变量的情况下  
"""
"""
小明一家三口,,
一个电视机  >>> 全局变量 资源  资源竞争的额问题
小明爸 
小明妈 
小明
"""























































