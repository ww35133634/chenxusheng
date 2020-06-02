"""
需求：
1. 生成10个不同的三位数
"""
# from day05_list.class_random import class_random
# if __name__ == '__main__':
#     obj01 = class_random.Random_result(100,1000,10)
#     print(obj01.one_distinc_result)

"""
2. 有10个学生，姓名自行添加。有三门考试：语文、数学和英语，随机为这10个学生生成分数【50-100】，
   要求每一门科目中所有学生分数不能重复
需求：【1】统计出每门学生的前三名和后三名【包含姓名和具体的分数】
      【2】统计出总分的前三名和后三名学生姓名
      【3】在(50-100)的数字中，哪些数字没有在在三门的分数中出现过
"""
from day05_list.class_random import class_random
from operator import itemgetter,attrgetter
if __name__ == '__main__':
    obj_name = class_random.Random_name(10)
    names = obj_name.name
    print(names)
    all_results = []
    name_totals = []
    for name in names:
        results = []
        total = []
        obj_result = class_random.Random_result(50, 100, 3)
        one_result = obj_result.one_distinc_result
        print(one_result)
        # 格式：[姓名，语文成绩，数学成绩，英语成绩]
        results.append(name)
        results.extend(one_result)
        # 格式：[姓名，成绩总分]
        total.append(name)
        total.append(sum(one_result))
        all_results.append(results)
        name_totals.append(total)
    print(all_results)
    print(name_totals)
# 【1】统计出每门学生的前三名和后三名【包含姓名和具体的分数】
#     course = ["chinese","math","english"]
#     i = 1
#     for i in range(1,len(course)+1):
#         # all_results_sort = sorted(all_results,key=lambda x:x[i],reverse=True)
#         all_results_sort = sorted(all_results,key=itemgetter(i),reverse=True)
#         top3_all_results = all_results_sort[:3]
#         last3_all_results = all_results_sort[-3:]
#         print("%s 前3名成绩:%s,%s 后3名成绩:%s \n" %(course[i-1],top3_all_results,course[i-1],last3_all_results))
# 【2】统计出总分的前三名和后三名学生姓名





"""
一副扑克牌52张（除了大小王）, 4个玩家在玩，模拟系统发牌、洗牌和整理牌，具体需求如下：
【1】先按照顺序打印出一副扑克牌
【2】在没有洗牌的情况下，输出发到四个玩家的扑克牌
【3】实现对扑克牌的洗牌，然后输出发到四个玩家的扑克牌
【4】对于洗牌后的四个玩家的扑克牌进行整理
​    整理规则1：数字从小到大
​    从小到大(3、4、5、6、7、8、9、10、J、Q、K、A、2)
​    整理规则2：在数字相同的情况下，按照花色（黑、红、梅、方）的顺序
"""