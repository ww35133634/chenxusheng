# # 格式化字符串常见用法
# print("i am {0},age {1}".format("tom", 18))
# # i am tom,age 18
# print("{:.2f}".format(3.1415926))  # 保留小数点后两位
# # 3.14
# print("{:+.2f}".format(-1))  # 带符号保留小数点后两位
# # -1.00
# print("{:.0f}".format(2.718))  # 不带小数位
# # 3
# print("{:0>3d}".format(5))  # 整数补零，填充左边, 宽度为3
# # 005
# print("{:,}".format(10241024))  # 以逗号分隔的数字格式
# # 10,241,024
# print("{:.2%}".format(0.718))  # 百分比格式
# # 71.80%
# print("{:.2e}".format(10241024))  # 指数记法
# # 1.02e+07

# lst = [1, 2, 3, 5]
# print(f'lst: {lst}')
# print(f'lst:', lst)

# # 判断是否为闰年
# import calendar
# from datetime import date
# mydate = date.today()
# is_leap = calendar.isleap(mydate.year)
# print(("{}是闰年" if is_leap else "{}不是闰年\n").format(mydate.year))

import os

# os.chdir(r'F:\python\ITcoach\python_ knowledge_point_practice')
# t = os.listdir()  # 返回 文件夹下的文件名的列表，如下
# # 返回 ['practice_point.py', '多线程.py', '多线程内的子线程执行类内的代码.py', '演示gevent完成多任务.py', '演示greenlet完成多任务.py', '生成器.py', '类模块的装饰器和修饰器区别.py', '迭代器.py', '迭代器的应用.py']

# t = os.path.splitext('D:/source/dataset/new_file.txt')  # 提取文件后缀
# 返回 ('D:/source/dataset/new_file', '.txt')
# t = os.path.split('D:/source/dataset/new_file.txt')  # 提取文件名
# 返回 ('D:/source/dataset', 'new_file.txt')
# print(t)

# x = [1, 3, 5]
#
# for i, e in enumerate(x, 10): # 枚举
#     print(i, e)

data = [1, 2, 3, 5, 8]
result = [i * 2 for i in data if i & 1] # 奇数则乘以2
print(result)  # [2, 6, 10]













