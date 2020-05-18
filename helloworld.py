"""
使用异常处理机制完成 用户登录信息校验 案例
要求:
用户输入用户名, 密码后对信息进行校验
1. 用户名长度在3-8个字符
2. 用户名中只能出现英文字母和数字
3. 密码长度必须是6位
4. 密码必须由纯数字组成
5. 验证码的判断  ABCD  ABCD
输入错误之后,,自动重新输入
总共输入错了五次,,那么就返回一个'登录失败'
"""
from random import randint

class NameisError(Exception):
    pass
class PwdisError(Exception):
    pass
class AuthcodeisError(Exception):
    pass
def check_infos(name,password,authcode):
    if len(name) < 3 and len(name) > 8:
        raise NameisError("用户名长度不符要求，请重新输入！")
    if not name.isalnum():
        raise NameisError("输入用户名不是字母或数字，请重新输入！")
    if len(password) != 6:
        raise PwdisError("密码长度不符6位，请重新输入！")
    if not password.isnumeric():
        raise PwdisError("密码不是6位数字，请重新输入！")
    if authcode





if __name__ == '__main__':
    name = input("请输入用户名：")
    password = input("请输入密码：")
    authcode = randint()
    check_infos(name,password,authcode)


