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
# def demo(num:int):
#     if num == 1:
#         return 1
#     else:
#         total = demo(num-1) + num
#         return total
#
# if __name__ == '__main__':
#     result = demo(100)
#     print(result)

# def fib_get_num(num:int):
#     assert num >= 0
#     if num <= 1:
#         return num
#     else:
#         return fib_get_num(num - 2) + fib_get_num(num - 1)
#
# if __name__ == '__main__':
#     nums = []
#     for i in range(10):
#         num = fib_get_num(i)
#         nums.append(num)
#     print(nums)

"""
随机生成两个1000以内的不同的整数，计算两个数之间的质数之和
比如生成 312 和 980 
计算从312到980之间的所有素数之和并输出
"""
# import random
# import math
# def get_num():
#     """生成2个1000以内的不同的整数"""
#     num_set = set()
#     while len(num_set) != 2:
#         num = random.randint(1,1000)
#         num_set.add(num)
#     num_list = list(num_set)
#     num_list.sort()
#     return num_list
#
# def prime_range(start:int,end:int):
#     prime_nums = []
#     for i in range(start,end + 1):
#         if is_prime(i):
#             # print(i)
#             prime_nums.append(i)
#     return prime_nums
#
# def is_prime(num:int):
#     if num <= 1:
#         return False
#     elif num == 2:
#         return num
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return num
#
#
# if __name__ == '__main__':
#     nums = get_num()
#     print(nums)
#     prime_list = prime_range(nums[0], nums[1] + 1)
#     result = 0
#     for i in prime_list:
#         result += i
#     print(result)
#     print(prime_list)
#     print(math.fsum(prime_list))

import random
import numpy as np

def get_num():
    """获取2个不重复的数"""
    nums = set()
    while len(nums) < 2:
        num = random.randint(0,1000)
        nums.add(num)
    return nums


def is_prime(num:int):
    if num <= 1:
        return False
    elif num == 2:            
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def prime_nums(start:int,end:int):
    prime_list = []
    for i in range(start,end + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

if __name__ == '__main__':
    nums = get_num()
    print("最大值是：{}\t 最小值是：{}".format(min(nums),max(nums)))
    prime_list = prime_nums(min(nums),max(nums))
    print(prime_list)






# def myprime(x):
#     """判断一个数x是否为素数,如果为素数，
#     返回True,否则返回False
#     """
#     if x <= 1:
#         return False
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True
#
# def myprimes(start, end):
#
#     for i in range(start,end):
#         if myprime(i):
#             yield i
# print([x for x in myprimes(1, 10)])
#
# for x in myprimes(1,10):
#     print(x)




