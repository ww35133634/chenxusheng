# # 求三位数中最大的57的倍数
#
# if __name__ == '__main__':
#     for i in range(999,100,-1):
#         if i % 57 == 0:
#             print(i)
#             break

#  计算任何100，500个数间所有5的倍数之和

# sum = 0
# if __name__ == '__main__':
#     for i in range(100,500):
#         if i % 5 == 0:
#             sum += i
#     print(sum)


# if __name__ == '__main__':
# #     total = 0
# #     for i in range(100,500,5):
# #         total += i
# #     print(total)


# 演示：输入一个正整数，求出从1开始到这个数中所有包含3数字的数和3的倍数的和。


"""
输入一个数字，判断是不是质数
质数 又叫素数
比如 7 ，只能被1 或者 自己整除
比如 21 不是素数，1，21， 3，7
"""
# import numpy as np
#
# def is_prime_number(num:int):
#     for r in range(2,int(np.sqrt(num))+1):
#         if num % r == 0:
#             return False
#         else:
#             return True
#
# if __name__ == '__main__':
#     num = int(input("请输入一个数："))
#     is_prime = is_prime_number(num)
#     print(is_prime)

"""
生成斐波那契序列,返回指定位置的数字
0，1，1，2，3，5，8，13，21，34......
从第3个数开始，后面的数是前面两个数之和
"""
# 普通方法：
# def get_list(number:int=5):
#     try:
#         num01_str = input("请输入第1个数：")
#         num02_str = input("请输入第2个数：")
#         num01 = int(num01_str)
#         num02 = int(num02_str)
#         list01 = []
#         list01.append(num01)
#         list01.append(num02)
#         i = len(list01)
#         while i <= number - 1:
#             num = list01[i - 1] + list01[i - 2]
#             list01.append(num)
#             i += 1
#         return (list01,list01[-1])
#     except:
#         print("请输入一个整数！")
# if __name__ == '__main__':
#     num_list,num = get_list(20)
#     print("生成的斐波那契序列是：%s " % num_list)
#     print("指定位置的数字是：%d " % num)

#递归法

# def demo(a:int):
#     if a == 1:
#         return 0
#     elif a == 2:
#         return 1
#     else:
#         return demo(a - 2) + demo(a - 1)
# if __name__ == '__main__':
#     num= demo(10)
#     print(num)

# def fib_recursion(n):
#   assert n >= 0, "n > 0"
#   if n <= 1:
#     return n
#   return fib_recursion(n-1) + fib_recursion(n-2)
#
# for i in range(1, 20):
#     print(fib_recursion(i), end=' ')

# f = []
# def fib_recur(x = 1,y = 1):
#     global f
#     while len(str(y))!= 5:
#         f.append(x)
#         y += x
#         x = y - x
#     return
# fib_recur()
# print(f)

"""
计算从1-100之和
1+2+3+4...... 100
"""

# 递归法



