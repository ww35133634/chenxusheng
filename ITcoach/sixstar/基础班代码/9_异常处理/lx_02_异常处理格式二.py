"""
演示异常处理格式二
"""


# 读写文件
# 1.打开一个文件 假设存在一个1.txt的文件 w write r read
# file1 = open('1.txt','r')  # r
# # 2.操作这个文件 读这个read 写文件write 操作必须入打开的模式相对应
# file1.write('hello,武汉加油')
# # 3.关闭这个文件
# file1.close()




# 如果出现异常,会跳到except里面去关闭文件
# 但是如果没有引发的异常,就不会被关闭
try:
    file1 = open('1.txt','w')  # 打开文件

    file1.write('hello,武汉加油')  # 这里报错
    # 文件没有被关闭,,导致无限期占用内存,
    # file1.close()  # 这句话不会被执行  这句话必须被执行
except:
    # file1.close()
    print('文件打开失败')
# 需要一个无论是否出现异常,,都会被执行的地方
finally: #
    file1.close()
    print('因为我必须要执行')
















































































