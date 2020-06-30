"""
文件的写操作
"""
# # 1.打开文件
# file1 = open('demo6.txt','w')
# # 2.操作文件
# file1.write('hello python')
# # 3.关闭文件
# file1.close()

# writelines  >>> readlines
# 1.先读取
file1 = open('demo6.txt','r')
data = file1.readlines()
print(data)
file1.close()

# 复制到一个新的文件当中
file2 = open('demo7.txt','w')
file2.writelines(data)  # write >>> 字符串
file2.close()


















































