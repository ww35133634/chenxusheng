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
import numpy as np

def is_prime_number(num:int):
    for r in range(2,int(np.sqrt(num))+1):
        if num % r == 0:
            return False
        else:
            return True

if __name__ == '__main__':
    num = int(input("请输入一个数："))
    is_prime = is_prime_number(num)
    print(is_prime)

