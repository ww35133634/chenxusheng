# # import random
# #
# # list1 =[1,2,3,4,5,6,7]
# # print(random.randint(2, 5)) # 两个 数之间 随机产生一个值
# # print(random.choices(list1)) # 随机选择一个数据模型里面的单独元素
# #
# #
# # # 用户胡登录
# #
# # # 26字母 随机产生
# #
# #
# # 自定义异常类
# import random  # 用来生成随机方法
# import string  # 用来生成26个字母
#
#
# class NameIsError(Exception):  # 用户名异常类
#     pass
#
#
# class PwdIsError(Exception):  # 密码异常类
#     pass
#
#
# class CodeIsError(Exception):  # 验证码异常类
#     pass
#
#
# # 检测是否符合规范
# def check(n):
#     """检查用户名和密码是否符合规范"""
#     j = 1  # 循环变量初始值
#     while True:
#         try:
#             # 输入得到用户名(str), 密码(str), 验证码(str)
#             name = input('请输入您的用户名(第%s次):' % j)
#             pwd = input('请输入您的密码(第%s次):' % j)
#
#             str4 = string.ascii_uppercase  # 生成一个26个大写字母
#             code_id = ''  # 创建一个空的字符串
#             for i in range(4):  # 循环四此
#                 code = random.choices(str4)  # 从26个大写字母中随机一个放进列表
#                 code = code[0]  # 取列表的第一项得到一个随机的字符,类型为str
#                 code_id = code_id + code  # 字符串拼接,最终得到四个随机大写字母的字符串
#
#             code = input('请输入您的验证码(%s):' % code_id)
#             code = code.upper()  # 验证码不区分大小写
#
#             # 输入次数记录
#             j += 1
#             if j > n:  # 失败次数
#                 print('%s机会已经用完,程序失败,请明年再试!' % n)
#                 break
#
#             # 判断逻辑
#             if len(name) < 3 or len(name) > 8:
#                 raise NameIsError('用户名的长度必须在3-8个字符之间')
#
#             if not name.isalnum():
#                 raise NameIsError('用户名中只能出现英文字母和数字')
#
#             if len(pwd) != 6:
#                 raise PwdIsError('密码长度必须是6位')
#
#             if not pwd.isnumeric():
#                 raise PwdIsError('密码必须由纯数字组成')
#
#             if code != code_id:
#                 raise CodeIsError('验证码输入错误')
#
#             print('登录成功')
#             break
#
#         except NameIsError as e:
#             print(e)
#         except PwdIsError as e:
#             print(e)
#         except CodeIsError as e:
#             print(e)
#
#
# check(5)  # 调用函数,传参决定可以输入几次机会












import random


class Games:
    def __init__(self):
        self.tires = 0
        self.guess = 0
        self.secret = random.randint(1, 99)
        self.guess_int = input('请输入1-99的整数')

    @classmethod
    def guess_nums(cls):
        if (man1.guess != man1.secret) and man1.tires < 5:
            man1.guess = str(man1.guess_int)
            if man1.guess.isdigit():
                man1.guess = int(man1.guess_int)
            if man1.guess < man1.secret:
                print('太小咯!')
            else:
                print('大大大了!')
            man1.tires += 1
        if man1.guess == man1.secret:
            print('猜对了!!')
        else:
            print('机会没了!')

    @classmethod
    def main(cls):
        man1.guess_nums()

man1 =Games()
man1.main()


















