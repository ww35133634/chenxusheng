"""
演示自定义异常
"""
"""
异常是可以避免的,
不可避免的异常,用户输入的信息,,网络原因,,
"""
# 原生的异常: NameError,ZeroDivisionError
# 自定义异常:


# name = '波小明同学'
# age = 22

"""
1.仅仅做了一个简单的打印,,
2.最关键的,你把这个处理逻辑写死在函数里面是不合理,,
企业级的开发思维,,抛出异常,,然后呢在外拦截,,证明符合条件,,,就可以进行处理
"""
# def check_name(name):  # 检查名字
#     if name.find('明') >= 0:  # find() >= 0    找不到的情况 -1
#         print("这个人的名字里面有'明'字")
#
# def check_age(age):  # 检查年龄
#     if age >= 20:
#         print('这个人的年纪超过了20岁')
#
# check_name(name)
# check_age(age)
       # 01



# name = '小同学'
# age = 22
#
# def check_name(name):  # 检查名字
#     if name.find('明') >= 0:  # find() >= 0    找不到的情况 -1
#         raise NameError('这个人的名字里面有"明"字,')
#
# def check_age(age):  # 检查年龄
#     if age >= 20:
#         raise ValueError('这个人的年纪超过了20岁,')
#
# # 原生的异常:
# # 自定义异常:
# try:
#     check_name(name)
#     check_age(age)
# except NameError:  # 就证明你的名字里面有"明"字,因为我就可以进行相关处理
#     print('名字里面带"明"的已经处理完毕.......')
# # 只要是ValueError, 那么就能够证明是年纪超过了20岁
# except ValueError:
#     print('年纪超过了20岁的已经处理完毕.......')





# 类的东西 面向对象
"""
自定义异常类的条件
1.必须是一个类,
2,要被Exception所包含, Exception必须要我们自定义异常类的父类
"""
# 函数  def 函数名
# 类  class 类名
#        子类     (父类)   自定义异常类
class NameIsError(Exception):  # Exception是NameIsError的父类
    pass  # 1.可以让类或者函数内部什么都没有, 2.让其不会报错  >>> 占位符

class AgeIsError(Exception):
    pass  # 只要有父类,,pass就代表你所有的东西都是父类给你的




name = '小同学'
age = 22

def check_name(name):  # 检查名字
    if name.find('明') >= 0:  # find() >= 0    找不到的情况 -1
        raise NameIsError('这个人的名字里面有"明"字,')

def check_age(age):  # 检查年龄
    if age >= 20:
        raise AgeIsError('这个人的年纪超过了20岁,')

# 原生的异常:
# 自定义异常:
try:
    check_name(name)
    check_age(age)
except NameIsError:  # 就证明你的名字里面有"明"字,因为我就可以进行相关处理
    print('名字里面带"明"的已经处理完毕.......')
# 只要是ValueError, 那么就能够证明是年纪超过了20岁
except AgeIsError:
    print('年纪超过了20岁的已经处理完毕.......')












































