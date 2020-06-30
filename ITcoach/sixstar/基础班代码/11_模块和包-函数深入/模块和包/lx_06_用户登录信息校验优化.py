"""
演示用户登录信息校验优化
"""
# 导入自定义异常类
from exception_666.exception_6 import *
# 导入业务函数,判断
from business_666.business_66 import *

name = input('请输入您的用户名:')
pwd = input('请输入您的密码:')

# 主程序文件当中
try:
    check(name, pwd)
except NameIsError as e:
    print(e)
except PwdIsError as e:
    print(e)













































































