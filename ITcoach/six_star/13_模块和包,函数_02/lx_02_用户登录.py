"""
用户登录
"""
from exception_666.exception_6 import *
from business_666.business_6 import *
# 读取缓存

name = input("请输入您的用户名:")
pwd = input("请输入您的密码")

# 自定义异常,拿走,,放到相对独立的包中去保存,当成模块文件




# 检测账号跟密码是否符合规范  可以拿走,,当做模块文件导入

# 拦截异常
try:
    check(name,pwd)
except NameIsError as e:
    print(e)
except PwdIsError as e:
    print(e)
