"""
随机生成一定数量不重复的数值
"""
import random

def random_oprator(begin_num,end_num,total_num):
    nums = []
    num = random.randint(begin_num,end_num)
    if num not in nums:
        nums.append(num)
        if len(nums) == total_num:
            print(nums)
            return nums


if __name__ == '__main__':
    nums = random_oprator(50,100,10)
