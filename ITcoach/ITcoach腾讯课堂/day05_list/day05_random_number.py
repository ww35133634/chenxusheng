"""
随机生成10个 50-100之间的整数 -- 随机数
random.randint(50,100)， 包含两头
"""
import random
#生成带有重复的数字
def get_random_repetition_numbers(begin:int,end:int,total:int):
    nums_list = list()  #存放生产成数的列表
    num = random.randint(begin,end)
    while len(nums_list) != total:
        nums_list.append(num)
        num = random.randint(begin,end)
    print(nums_list)
# 生成没有重复的数字
def get_random_distinct_numbers01(begin:int,end:int,total:int):
    nums_list = list()
    num = random.randint(begin, end)
    while len(nums_list) != total:
        if num not in nums_list:
            nums_list.append(num)
        num = random.randint(begin, end)
    print(nums_list)

def get_random_distinct_numbers02(begin:int,end:int,total:int):
    nums_set = set()
    num = random.randint(begin, end)
    while len(nums_set) != total:
        nums_set.add(num)
        num = random.randint(begin, end)
    print(nums_set)


if __name__ == '__main__':
    get_random_distinct_numbers02(50,100,10)


