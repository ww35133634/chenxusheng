"""
演示捕获具体的异常
"""

"""
用在用户登录上面
QQ:123456
密码:abc
验证码:qwer
1.账号输入有误  nameerror  
2.密码输入有误  passworderror
3.验证码输入有误 iderror
"""





# try:
#     demo = 'hello,python'
#     print(demo)  # 打印他的数据
#     print(demo.index('a'))  # 查看具体字符的索引值
# except:
#     print('demo没有被定义')  # 很精确的知道了是因为demo没有被定义



"""
	捕获具体的异常:
		except 异常类名:
		____出现异常现象的处理代码
"""
# NameError
# print(a)


# try:
#     demo = 'hello,python'
#     print(demo)  # 打印他的数据  出错
#     print(demo.index('a'))  # 查看具体字符的索引值
# except NameError:  # 指明了这部分只用来处理NameError引发的异常  虽然精确了, 捕获范围变小了
#     print('demo没有被定义')  # 很精确的知道了是因为demo没有被定义
# except ValueError:  # 成功捕获到ValueError的错误
#     print('该字符并不处于字符串当中')
# 同一个异常就不要重复设置了


# 你有可以写一个程序把所有的异常都给他精确捕获到嘛
# 有可能会有遗漏,,程序就会崩溃
# 在所有的精确捕获之后 来一个大的包围圈,格杀勿论





"""
一支军队被包围了,,,
三个包围圈:
1,只杀步兵
2,只杀骑兵
3,只杀炮兵
他们的将军跑了
4,大包围圈 不管你是什么,,格杀勿论

"""




try:
    demo = 'hello,python'
    print(demo)  # 打印他的数据  出错
    print(demo.index('p'))  # 查看具体字符的索引值
    d = 1 // 0  # 零不能被当做被除数来执行  Z

except NameError:  # 指明了这部分只用来处理NameError引发的异常  虽然精确了, 捕获范围变小了
    print('demo没有被定义')  # 很精确的知道了是因为demo没有被定义
except ValueError:  # 成功捕获到ValueError的错误
    print('该字符并不处于字符串当中')
# 大的包围圈,格杀勿论,无差别干掉
except Exception:  # Exception里面包含所有的精确异常  放在最后
    print('未知的错误')

# 类  父类 包含了
# d = 1 // 0
























