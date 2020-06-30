"""
演示文件的路径
"""

"""
文件所在的位置称为文件的路径

路径根据寻找的方式不同分为两种:
	❤绝对路径 从头开始算的,,就叫做绝对路径 中华人民共和国的湖南省的长沙市的岳麓区的麓谷街道的芯城科技园 
	❤相对路径 相对 优盛兴选公司的旁边
D:\乔木\2004期基础班\19_文件的读写\课件\代码
"""

# 绝对路径去写文件  当前的位置来作为相对
# file1 = open('D:/QQ/bobo.txt','w')
# file1.write('hello python 22:08')
# file1.close()

# 相对路径   当前路径 上一级的上一级
# file1 = open('./../../bobo.txt','w')
# file1.write('hello python 22:08')
# file1.close()

# 相对路径 往下去写
file1 = open('./demo1/demo2/demo3/bobo.txt','w')
file1.write('hello python 22:08')
file1.close()


"""
多任务 多线程 多进程 协程

"""


























































