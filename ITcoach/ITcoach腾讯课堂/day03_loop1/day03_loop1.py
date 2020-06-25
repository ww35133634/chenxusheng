"""
计算从1-100之和
1+2+3+4...... 100
"""
# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

# sum = 0
# i = 1
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)

"""
输入某年的某月，判断这个月有多少天
分析：
1，3，5，7，8，10，12 ： 31天
4 6 9 11: 30天
2：闰年：29天  平年：28天
核心：判断输入的年份是闰年还是平年
情况1: 年份%400 == 0 闰年   2000年
情况2：年份%4 ==0 And 年份%100 ！= 0  1900年不是闰年 1900%4==0 1900%100 == 0
"""

# day = [31,28,31,30,31,30,31,31,30,31,30,31]
# year_num = int(input("请输入查询年份："))
# month_num = int(input("请输入查询月份："))
# if year_num % 400 == 0 or (year_num % 4 == 0 and year_num % 100 != 0):
#     if month_num == 2:
#         day = day[month_num-1] + 1
# else:
#     day = day[month_num-1]
# print(day)

"""
课后习题：简单的计算器
执行过程 
请输入第一个数字: 100
请选择运算符（+, - , * , /, %）: - 
请输入第二个数字: 30
结果： 100 - 30 = 70
"""

def get_num():
    while True:
        num_str = input("请输入一个数字：")
        try:
            num = float(num_str)
            return num
        except:
            print("输入不符要求，请重新输入！")

def get_action(action_list:list):
    while True:
        action = input("请选择要执行的操作（+，-，*，/，%）：")
        try:
            if action in action_list:
                return action.strip()
        except:
            print("输入不符要求，请重新输入！")

if __name__ == '__main__':

    str01 = "+，-，*，/，%"
    action_list = str01.split("，")
    num01 = get_num()
    action = get_action(action_list)
    num02 = get_num()
    result = 0
    flag = True
    if action == '+':
        result = num01 + num02
    elif action == '-':
        result = num01 - num02
    elif action == '*':
        result = num01 * num02
    elif action == '/':
        if num02 == 0:
            print("除数不能为0")
            flag = False
        else:
            result = num01 / num02
    elif action == '%':
        if num02 == 0:
            print("除数不能为0")
            flag = False
        else:
            result = num01 % num02
    if flag:
        print('{}{}{}={}'.format(num01,action,num02,result))
































