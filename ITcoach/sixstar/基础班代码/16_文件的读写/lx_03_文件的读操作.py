"""
演示文件的读操作
"""


# file1 = open('hello.txt','r')
# data = file1.read()
# print(data)
# file1.close()

# 如果说一个文件里面的内容太多了 read() 会讲里面的内容一次性读取出来, 负荷太大,,,

# 第一种方式 read(参数)  # 每次读取参数大小的内容
# file1 = open('hello.txt','r')
# while True:  # 循环取值, 把里面的内容都读取出来,, 每次都多少由参数决定
#     data = file1.read(5)  # 字符来作为单位 一次读取出来的大小  5 hello 10 hello hell 空格也属于一个字符
#     print(data)
#     if len(data) == 0:  # 没有内容了
#         break
# file1.close()
# file1 = open('hello.txt','r')
# while True:  # 循环取值, 把里面的内容都读取出来,, 每次都多少由参数决定
#     data = file1.read(5)  # 字符来作为单位 一次读取出来的大小  5 hello 10 hello hell 空格也属于一个字符
#     print(data,end = '')
#     if len(data) == 0:  # 没有内容了
#         break
# file1.close()


# 第二种方式 readline>>> 每次读取一行
# file1 = open('hello.txt','r')
# while True:
#     data = file1.readline()
#     print(data)
#     if len(data) == 0:
#         break
# file1.close()


# 第三种 redalines 文件中所有字符数据成为一个列表,每一行字符数据都是一个元素
# file1 = open('hello.txt','r')
# data = file1.readlines()
# print(data)
# file1.close()









































