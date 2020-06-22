"""
案例:
    用户登录信息校验
要求:
	用户输入用户名, 密码后对信息进行校验
	1. 用户名长度在3-8个字符
	2. 用户名中只能出现英文字母和数字
	3. 密码长度必须是6位
	4. 密码必须由纯数字组成

"""

# 拿到用户的信息
name = input("请输入您的用户名:")
pwd = input("请输入您的密码")

# 自定义异常


class NameIsError(Exception):
    pass


class PwdIsError(Exception):
    pass


# 检测账号跟密码是否符合规范
def check(name, pwd):
    """判断用户名和密码是否符合规范"""
    # 	1. 用户名长度在3-8个字符
    if len(name) < 3 or len(name) > 8:
        raise NameIsError("用户名的长度应该是在3-8个字符之间")

    #	2. 用户名中只能出现英文字母或数字
    if not name.isalnum(): # 满足标识符 字母 数字 下划线
        raise NameIsError("用户名中只能出现英文字母和数字")

    # 3. 密码长度必须是6位
    if len(pwd) != 6:
        raise PwdIsError("密码长度必须是6位")

    # 	4. 密码必须由纯数字组成
    if not pwd.isdigit():
        raise PwdIsError("密码必须由纯数字组成")

# 拦截异常
try:
    check(name,pwd)
except NameIsError as e:
    print(e)
except PwdIsError as e:
    print(e)




















# class NameIsError(Exception):
#     pass
#
# class PwdError(Exception):
#     pass
#
#
#
# def check(name,pwd): # 检测功能
#     """判断用户名和密码是否规范"""
#     if len(name) < 3 or len(name) > 8: #	1. 用户名长度在3-8个字符
#        raise NameIsError('用户名长度在3-8个字符')
#     if not name.isalnum():	# 2. 用户名中只能出现英文字母和数字 面向百度编程
#         raise NameIsError('用户名中只能出现英文字母和数字')
#     if len(pwd) != 6:# 密码长度必须是6位
#         raise PwdError('密码长度必须是6位')
#     if not pwd.isnumeric(): # 密码必须由纯数字组成
#         raise PwdError('密码必须由纯数字组成')
#
#
# name = input('请输入用户名:') # 字符串
# pwd = input('请输入密码') # 字符串转化成整数
#
# try:
#     check(name,pwd)
# except NameIsError as e:
#     print(str(e))
# except PwdError as e:
#     print(str(e))
# else:
#     print('登录成功')


















































































