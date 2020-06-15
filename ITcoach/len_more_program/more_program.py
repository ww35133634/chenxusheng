# import threading
#
# num = 1
#
#
# def demo1():
#     global num  # 把num提升为全局变量
#     num += 1
#     print("demo1的num是%s" % num)
#
#
# def demo2():
#     print("demo2的num是%s" % num)
#
#
# def main():
#     t1 = threading.Thread(target=demo1)
#     t2 = threading.Thread(target=demo2)
#     t1.start()
#     t2.start()
#
#
# if __name__ == "__main__":
#     main()


import threading

list1 = [1,2,3,4]


def demo1(i):
    # global list1    #因为是list1 是列表元素可以变的，可以不用global
    list1.append(i)
    print("demo1的list1是%s" % list1)


def demo2():
    print("demo2的list1是%s" % list1)


def main():
    t1 = threading.Thread(target=demo1,args=(5,))   #args是传入实参，参数为元组
    t2 = threading.Thread(target=demo2)
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
