"""
异常处理的机制
"""

# 层层嵌套的情况  甩锅的过程
try:
    def demo1():
        d =  1 // 0
        print(a)  # 异常
    def demo2():
        try:
            demo1()
        except NameError:
            print('思思老师帮助你 ....')
    def demo3():
        demo2()

    try:
        demo3()
    except NameError:
        print('波波老师帮助你...')
except ZeroDivisionError:
    print('乔木老师帮助你...')

















































































































