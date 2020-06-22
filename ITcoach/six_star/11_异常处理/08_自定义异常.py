"""
演示自定义异常
"""

# 清朝前期,,风云突起,清朝,少数民族,,明朝,,
# 朝廷,, 规定,, 取名字>>"明",, 反清复明的节奏

# name = "乔木"

# def check_name(name):
#     if name.find("明") >= 0: # 索引大于0,,就以为着有明这个字符
#         print("这个人暗示反清复明,抓起来") # 处理方案写死, 这个不好
#     else:
#         print("这个人是个大清良民")
#
# check_name("小明")

# 年龄,, 如果到达了20岁,,那么你要去当兵,,
# 有一天, 皇帝开明了,, 你的名字可以带有"明",,不把你当作反清复明,,
# 参军的人数够了,不再强制征兵


# def check_name(name):
#     if name.find("明") >= 0:
#         raise NameError("这个人名字里面有明")
#     else: # 可写可不写
#         print("名字里面没有明")
#
# def check_age(age):
#     if age >= 20:
#         raise ValueError("这个人年龄到了20岁")
#
# age = 20
# name = "小明"
# try:
#
#     check_name(name)
#     check_age(age)
# except NameError: # 具体的应对方案
#     # print("你这个人暗示反清复明,要抓起来")
#     print("你这个人名字有点问题,但是没事")
# except ValueError:# 具体的应对方案
#     print("你这个人到了参军的年龄,,但是不强求")



# 不能去占用原生的异常类 需要自定义异常类
# exception是所有异常类的爸爸 父类,
# class 代表定义一个类
# 类名使用大驼峰写法, 标识符,, idcard IdCard

# 自定义异常的定义
class NameIsError(Exception):#继承了这个类,就可以拥有这个类所有的东西
    pass # 占位符,不去起作用又不会报错

class AgeIsError(Exception):
    pass

def check_name(name):
    if name.find("明"):
        raise NameIsError("这个人名字里面有明")

def check_age(age):
    if  age >= 20:
        raise AgeIsError("这个人的年纪超过了20")

age = 20
name = "小明"
try:
    check_name(name)
    check_age(age)
except NameIsError:
    # print("你这个人暗示反清复明,要抓起来")
    print("你这个人名字有点问题,但是没事")
except AgeIsError:
    print("你这个人到了参军的年龄,,但是不强求")


















