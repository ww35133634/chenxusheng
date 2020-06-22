"""
演示文件基本操作
"""

# # 1.打开文件 ctrl + 鼠标左键点击
# file1 = open("demo.txt","w") # read > r  write > w
# # 2.操作文件(读或写)
# file1.write("hello ptyhon lalala")
# # 3.关闭文件
# file1.close() # 关闭


# 第二种格式, 免关闭格式
with open("demo1.txt","w") as file1:
    file1.write("hello,武汉加油")














