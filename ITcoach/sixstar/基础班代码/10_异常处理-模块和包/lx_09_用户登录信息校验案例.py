"""
演示用户信息登录校验案例
"""
"""
	使用异常处理机制完成 用户登录信息校验 案例
	要求:
		用户输入用户名, 密码后对信息进行校验
v
	思考:
		1. 用户名, 密码如何得到?
		2. 各种规则如何使用异常处理机制实现?
"""
"""
1.input() 两样数据 用户名, 密码
"""

# 3.自定义异常,当不满足我们的规范时,,就抛出异常,让程序报错 raise
class NameIsError(Exception):
    pass

class PwdIsError(Exception):
    pass

# 1.输入得到 用户名和密码
name = input('请输入您的用户名:')  # str
pwd = input('请输入您的密码:')  #

# 2.检测 是否符合规范  复用性很强 >>> 函数
# 符合四个规范就没事,登录成功,,只要一个不满足条件,,那么就进行处理
def check(name,pwd):
    """检查用户名和密码是否符合规范"""
    if len(name) < 3 or len(name) > 8:  # 用户名长度在3-8个字符
        raise NameIsError('用户名的长度不在3-8个字符之间')
    if not name.isalnum():  # 用户名中只能出现英文字母和数字 汉字 正则表达式
        raise NameIsError('用户名中只能出现英文字母和数字')
    if len(pwd) != 6:  # 密码长度必须是6位
        raise PwdIsError('密码长度必须是6位')
    if not pwd.isnumeric():  # 密码必须由纯数字组成 T
        raise PwdIsError('密码必须由纯数字组成')
    print('登录成功')

try:
    check(name, pwd)
except NameIsError as e:  # 精确捕获异常处理的意义
    print(e)
except PwdIsError as e:
    print(e)




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


"""
1,只能由数字,字母,_组成
2.不能以数字开头
3.不能是关键字

"""















































