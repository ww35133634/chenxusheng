"""
演示循环的嵌套
"""
# j = 1
# while j <= 3:
#     i = 1
#     while i <= 3:  # 打印123
#         print(i)
#         i += 1  # i = i + 1
#     j += 1  # j = j + 1



# 循环嵌套的应用理解使用
"""
*     1 第一轮
**    2 第二轮
***   3 第三轮
****  4
***** 5
"""

# 1.点的打印print('*')
# print('*')print('*')print('*')print('*')print('*')

# 2.一行五个,反复去print('*'),,循环 while

# 3.多行的打印:循环的嵌套
j = 1
while j <= 5:  # 外部循环控制着打印多少行
    i = 1
    while i <= j:  # 内部循环就是外部循环的一轮循环,,控制一行打印多少个
        # 每执行一次print,他的结尾是默认换行的  >>>>连接
        print('*',end = '')  # end = ''
        i += 1  # 内存循环变量的自增

    j += 1  # 外部循环变量的自增 # shift + ctrl  上下箭头
    print()  # 他的结尾是默认换行的 手动换行的操作








































































