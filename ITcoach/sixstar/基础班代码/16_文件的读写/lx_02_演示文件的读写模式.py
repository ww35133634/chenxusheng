"""
演示文件的读写模式
"""
# 预习愉快的多任务

# W 模式 write
# 文件不存在的情况 新建文件 讲内容写入
# with open('demo3.txt','w') as file1:
#     file1.write('hello python')
# 文件存在的情况  里面的内容会进行一个覆盖
# with open('demo3.txt','w') as file1:
#     file1.write('bobo bobo bobo')


# a模式  append 追加
# 文件不存在的情况下 新建文件 将内容写入
# with open('demo4.txt','a') as file1:
#     file1.write('hello python')
# 文件存在的情况 在最后追加内容
# with open('demo4.txt','a') as file1:
#     file1.write('bobo bobo bobo')


# r 模式 read
# 文件存在的情况下
# with open('demo4.txt','r') as file1:
#     data = file1.read()  # data里面保存着的就是读取出来的数据/内容
#     print('读取出来的数据是:',data)
# 文件不存在的情况下
# with open('demo5.txt','r') as file1:
#     data = file1.read()  # data里面保存着的就是读取出来的数据/内容
#     print('读取出来的数据是:',data)


# 完成复制
# file1 = open('demo4.txt','r')
# data = file1.read()
# file1.close()
#
# # 新建一个文件
# file2 = open('demo5.txt','w')
# file2.write(data)  # 把demo4.txt文件里面读取出来的内容写进新的文件
# file2.close()
# c++ c plus plus C 强大
# 字节组成的图片
# file1 = open('女友1号.jpg','rb')
# data = file1.read()
# file1.close()
#
# # 新建一个文件
# file2 = open('女友2号.jpg','wb')
# file2.write(data)  # 把demo4.txt文件里面读取出来的内容写进新的文件
# file2.close()


file1 = open('90_多个装饰器分析.wmv','rb')
data = file1.read()
file1.close()

# 新建一个文件
file2 = open('bobo老师真帅气.mp4','wb')
file2.write(data)  # 把demo4.txt文件里面读取出来的内容写进新的文件
file2.close()



















































