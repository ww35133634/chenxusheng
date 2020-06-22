"""
文件写操作
"""
# file1 = open("demo6.txt","w")
# file1.write("hello python")
# file1.close()


# 先读取
file1 = open("demo6.txt","r")
read_file = file1.readlines()
print(read_file)
file1.close()

file2 = open("demo7.txt","w")
file2.writelines(read_file)
file2.close()









































