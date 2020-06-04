"""
需求：1. 生成10个不同的三位数
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
# from day05_list.class_random import class_random
# from operator import itemgetter,attrgetter
# if __name__ == '__main__':
#     obj_name = class_random.Random_name(10)
#     names = obj_name.name
#     # print(names)
#     all_results = []
#     name_totals = []
#     appear_numbers = []
#     for name in names:
#         results = []
#         total = []
#         obj_result = class_random.Random_result(50, 100, 3)
#         one_result = obj_result.one_distinc_result
#         # print(one_result)
#         # 需求1格式：[姓名，语文成绩，数学成绩，英语成绩]
#         results.append(name)
#         results.extend(one_result)
#         # 需求2格式：[姓名，成绩总分]
#         total.append(name)
#         total.append(sum(one_result))
#         # 需求3
#         appear_numbers.extend(one_result)
#
#         all_results.append(results)
#         name_totals.append(total)
#     # print(all_results)
#     # print(name_totals)
# # 【1】统计出每门学生的前三名和后三名【包含姓名和具体的分数】
#     course = ["chinese","math","english"]
#     i = 1
#     for i in range(1,len(course)+1):
#         # all_results_sort = sorted(all_results,key=lambda x:x[i],reverse=True)
#         all_results_sort = sorted(all_results,key=itemgetter(i),reverse=True)
#         top3_all_results = all_results_sort[:3]
#         last3_all_results = all_results_sort[-3:]
#         print("%s 前3名成绩:%s,%s 后3名成绩:%s \n" %(course[i-1],top3_all_results,course[i-1],last3_all_results))
# # 【2】统计出总分的前三名和后三名学生姓名
#     name_totals_sort = sorted(name_totals,key=itemgetter(1),reverse=True)
#     top3_name_totals = name_totals_sort[:3]
#     last3_name_totals = name_totals_sort[-3:]
#     top3_names = []
#     for t_name in top3_name_totals:
#         top3_names.append(t_name[0])
#     last3_names = []
#     for l_name in last3_name_totals:
#         last3_names.append(l_name[0])
#     print("成绩总分前3名：%s ,成绩总分后3名：%s \n" %(top3_names,last3_names))
# # 【3】在(50-100)的数字中，哪些数字没有在在三门的分数中出现过
#     print("分数中出现的数字：%s" % appear_numbers)
#     numbers = []
#     for num in range(50,101):
#         if num not in set(appear_numbers):
#             numbers.append(num)
#     print("分数中未出现的数字：%s" %numbers)





