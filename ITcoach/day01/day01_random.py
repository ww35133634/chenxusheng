"""
随机生成一定数量不重复的数值
"""
import random

# def random_oprator(begin_num,end_num,total_num):
#     nums = []
#     num = random.randint(begin_num,end_num)
#     if num not in nums:
#         nums.append(num)
#         if len(nums) == total_num:
#             print(nums)
#             return nums
#
#
# if __name__ == '__main__':
#     nums = random_oprator(50,100,10)


class RandomItem:
    def __init__(self,begin_num,end_num,num):
        self.begin_num = begin_num
        self.end_num = end_num
        self.num = num
        self.nums = []   #定义存放随机数的集合

    def get_num(self):
        temp = random.randint(self.begin_num,self.end_num)
        if temp not in self.nums:
            self.nums.append(temp)
            if len(self.nums) == self.num:
                break
if __name__ == '__main__':
    obj01 = RandomItem(50,100,10)
    obj01.get_num()
    print(obj01.nums)





