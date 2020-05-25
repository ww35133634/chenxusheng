"""
练习1：输入一个不大于5位数的数字，然后输入每个位置的数字：
"""
# def check_num():

#
# def get_num(num):
#     i = len(num)-1
#     sr = ""
#     for n in num:
#         sr = sr + "%s位是：%s \t" %(tuple01[i],n)
#         i -= 1
#     return sr
# if __name__ == '__main__':
#     tuple01 = ('个', '十', '百', '千', '万')
#     num = input("请输不大于5位数的数字或输入Q退出程序：")
#     while num != 'Q':
#         if len(num) <= len(tuple01):
#             st = get_num(num)
#             print(st)
#         else:
#             print("\n输入数字不符要求，请重新输入！")
#         num = input("请输不大于5位数的数字或输入Q退出程序：")


"""
- 输入三个互不相等的整数、按照从小到大输出
"""

# num01 = int(input("请输入一个整数："))
# num02 = int(input("请输入一个整数："))
# num03 = int(input("请输入一个整数："))
# num = []
# if num01 != num02 and num02 != num03:
#     num.append(num01)
#     num.append(num02)
#     num.append(num03)
#     num.sort()
#     for n in num:
#         print(n)

"""
- 用户输入一个年份，判断是否是闰年
"""
# year_num = int(input("请输入年份："))
# if year_num % 4 == 0 and year_num % 100 != 0 or year_num % 400 == 0: # and 优先 or 运算
#     print("%s是闰年" % year_num)
# else:
#     print("%s是平年" % year_num)

"""
- 编程实现145893秒是几天几小时几分钟几秒
- 提醒用户输入语文、数学、英语分数，输出总分和平均分
- 让用户输入陈鹏的语文和数学成绩，输入一下判断是否正确，正确（True）错误（False）
  - 陈鹏的语文和数学成绩都大于90分
  - 陈鹏的语文和数学成绩有一门大于90分
"""