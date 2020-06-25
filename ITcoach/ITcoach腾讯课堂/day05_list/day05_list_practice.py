"""
案例01：生成10个50-100的数字
案例02：生成10个不同的50-100的数字
案例03：班级有50个同学，每个同学有5门课，随机生成50个同学的成绩(成绩介于50-100之间)
   list = [
        [66,77,56,90,87],
        [58,78,91,67,100],
        .....
   ]
案例04:
随机生成五名学生 每个学生有五门科目【语文、数学、英语、物理、化学】，
为这5位同学随机生成5门考试的成绩【成绩介于50-100间】
需求：按照平均分的倒序打印出成绩的明细
"""
from day05_list.class_random import class_random

# 案例01：生成10个50-100的数字
# if __name__ == '__main__':
#     result = class_random.Random_result(50,100,10)
#     one_result = result.one_repetition_result
#     print(one_result)

# 案例02：生成10个不同的50-100的数字

# if __name__ == '__main__':
#     result = class_random.Random_result(50,100,10)
#     one_result = result.one_distinc_result
#     print(one_result)

"""案例03：班级有50个同学，每个同学有5门课，随机生成50个同学的成绩(成绩介于50-100之间)
   list = [
        [66,77,56,90,87],
        [58,78,91,67,100],
        .....
   ]
"""
# if __name__ == '__main__':
#     all_results = []
#     for i in range(1,51):
#         result = class_random.Random_result(50,100,5)
#         one_result = list(result.one_distinc_result)
#         all_results.append(one_result)
#     print(len(all_results))
#     print(all_results)

"""
案例04:
随机生成五名学生 每个学生有五门科目【语文、数学、英语、物理、化学】，
为这5位同学随机生成5门考试的成绩【成绩介于50-100间】
需求：按照平均分的倒序打印出成绩的明细
"""
import numpy as np

if __name__ == '__main__':
    result_average_list = []
    name = class_random.Random_name(5)
    name_list = list(name.name)
    results = []
    for i in range(len(name_list)):
        one_result = []
        result = class_random.Random_result(50, 100, 5)
        one_result_list = list(result.one_distinc_result)
        one_result_average = round(np.average(one_result_list),2)
        print(one_result_average)
        one_result.append(name_list[i])
        one_result.extend(one_result_list)
        one_result.append(one_result_average)
        results.append(one_result)
    print(results)

    # results01 = sorted(results,key=itemgetter(7))
    results01 = sorted(results,key=lambda x:x[7])
    print(results01)


"""
list01 = [['北京', 22312], ['南京', 18909], ['上海', 20134], ['深圳', 31221],['武汉',16045],
          ['成都', 12908], ['西安', 13009]]
# 写一个程序，实现list01按照数字排序
"""

# from operator import itemgetter,attrgetter
#
# list01 = [['北京', 22312], ['南京', 18909], ['上海', 20134], ['深圳', 31221],['武汉',16045],
#           ['成都', 12908], ['西安', 13009]]
#
# # list02 = sorted(list01,key=lambda x:x[1])
# list02 = sorted(list01,key=itemgetter(1),reverse=True)
# print(list02)
#
# student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10)]
# # list03 = sorted(student_tuples, key=lambda student: student[2])   # sort by age
# list03 = sorted(student_tuples,key=itemgetter(2),reverse=False)
# print(list03)









