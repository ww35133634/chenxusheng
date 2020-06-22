"""
文件读写模式的演示
"""
# w模式 write
# with open("demo2.txt","w") as file1:
#     file1.write("hello world")

# a模式, append追加 紧接着追加
# with open("demo3.txt","a") as file1:
#     file1.write("python, pyhton, python")

# r模式 阅读 read
# with open("demo3.txt","r") as file1:
#     file2 = file1.read()
#     print("file1里面读取到的内容是:",file2)


# 从一个文件中读取数据,,然后写入另一个文件,,复制
# file1 = open("demo3.txt","r")
# file2 = file1.read()
# file1.close()
#
# # 写操作 新建文件 保存内容
# file3 = open("demo4.txt","w")
# file3.write(file2)
# file3.close()



# 字符, 二进制>图片,  字节
# 从一个文件中读取数据,,然后写入另一个文件,,复制
# file1 = open("女友1号.jpg","rb")
# file2 = file1.read()
# file1.close()
#
# # 写操作 新建文件 保存内容 一个字节八个二进制单位
# file3 = open("女友2号.jpg","wb")
# file3.write(file2)
# file3.close()


# plus 加强版 c++ 侧重于哪个
file1 = open("demo5.txt","w+")
file1.write("hello")
read_file1 = file1.read()
# print(read_file1)
file1.close()
























