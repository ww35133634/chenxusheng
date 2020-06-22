"""
演示异常处理机制
"""

#
# def demo1():
#     print(i)
#
#
# def demo2():
#     demo1()
#
#
# def demo3():
#     demo2()
#
# try:
#     demo3()
# except:
#     print("出现了问题")


# def demo1():
#     print(i)
#
#
# def demo2(): #
#     try:
#         demo1()
#     except:
#         print("已经处理了")
#
# def demo3():
#     demo2()
#
#
# demo3()




try: # try 的嵌套
    def demo1():
        print(1/0)
        print(i)

    def demo2(): #
        demo1()


    def demo3():
        demo2()

    try:
        demo3()
    except NameError:
        print("因为变量名没有被定义")
except ZeroDivisionError:
    print("不能做除法")


































