"""
演示读操作
"""

# file1 = open("hello.txt","r")
# read_file = file1.read()
# print(read_file)
# file1.close()

# 希望不要一次性将其读取出来,,,
# 第一种方式
# file1 = open("hello.txt","r")
# while True: # 节约内存的空间
#     read_file = file1.read(1024) #1kb = 1024字符 1M =1024KB 1G = 1024M 1T = 1024G
#     if len(read_file) == 0:
#         break
#     print(read_file,end="")
# file1.close()


# 第二种方式
# file1 = open("hello.txt","r")
# while True:
#     read_file1 = file1.readline() # 一次读取一行
#     # print(read_file1)
#     if len(read_file1) == 0:
#         break
#     print(read_file1,end="")
# file1.close()


# 第三种方式
file1 = open("hello.txt","r")
read_file = file1.readlines()
print(read_file)
file1.close()


























