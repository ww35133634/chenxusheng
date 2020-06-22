"""
演示异常处理方案二
"""

try:
    print("读文件")
    f = open('123.txt','r') # 读取一个名为123.txt .py 的文件,,
    # f.read() # 阅读
    f.write("hello, 武汉加油!")  # 书写 出现问题
    # f.close() # 关闭该文件, 释放内存 文件未关闭,严重的内存泄漏的现象,
    print('读文件结束')
except:
    print("读取文件失败")
finally: #最后 作用 一定会强制执行里面的代码在最后
    print("我是一定要执行的!!!")
    # f.close() # 关闭该文件, 释放内存 文件未关闭,严重的内存泄漏的现象,























# try:
#     print(111)
#     print(a)
# except:
#     print(222)








































































