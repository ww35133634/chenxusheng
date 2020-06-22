"""
核心检测代码
"""



def check(name, pwd):
    """判断用户名和密码是否符合规范"""
    # 	1. 用户名长度在3-8个字符
    if len(name) < 3 or len(name) > 8:
        raise NameIsError("用户名的长度应该是在3-8个字符之间")

    # 2.用户名中只能出现英文字母或数字
    if not name.isalnum(): # 满足标识符 字母 数字 下划线
        raise NameIsError("用户名中只能出现英文字母和数字")

    # 3. 密码长度必须是6位
    if len(pwd) != 6:
        raise PwdIsError("密码长度必须是6位")

    # 	4. 密码必须由纯数字组成
    if not pwd.isdigit():
        raise PwdIsError("密码必须由纯数字组成")

















