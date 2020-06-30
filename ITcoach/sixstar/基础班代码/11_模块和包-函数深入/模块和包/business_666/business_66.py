"""
保存业务逻辑函数
"""

# 业务逻辑
def check(name,pwd):
    """检查用户名和密码是否符合规范"""
    if len(name) < 3 or len(name) > 8:
        raise NameIsError('用户名的长度不在3-8个字符之间')
    if not name.isalnum():
        raise NameIsError('用户名中只能出现英文字母和数字')
    if len(pwd) != 6:
        raise PwdIsError('密码长度必须是6位')
    if not pwd.isnumeric():
        raise PwdIsError('密码必须由纯数字组成')
    print('登录成功')



























