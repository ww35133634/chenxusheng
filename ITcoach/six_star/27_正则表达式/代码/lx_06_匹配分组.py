"""
演示匹配分组
"""

# 好比我们要去匹配一个 QQ邮箱 321651161@qq.com
# import re
# while True:
#     email = input("请输入一个QQ邮箱:")
#     email_data = re.match(r"\d{5,12}@[qQ]{2}\.com$",email)  # 转义 \. >>> .
#     if email_data:
#         print("%s是一个符合规范的qq邮箱地址......" % email)
#     else:
#         print("%s不是一个符合规范的qq邮箱地址*******" % email)


# 163 qq 分组
# import re
# while True:
#     email = input("请输入一个邮箱地址:") # or 或 shift +\ > |
#     email_data = re.match(r"[a-zA-Z0-9_]{4,16}@(qq|163)\.com$",email)
#     print(email_data.group())
#
#     if email_data:
#         print("%s是一个符合规范的邮箱地址......" % email)
#     else:
#         print("%s不是一个符合规范的邮箱地址*******" % email)



# 163 .qq
# import re
# while True:
#     email = input("请输入一个邮箱地址:") # or 或 shift +\ > |
#     email_data = re.match(r"[a-zA-Z0-9_]{4,16}@(qq|163)\.com$",email)  #分组
#     print(email_data.group(1))

    # if email_data:
    #     print("%s是一个符合规范的邮箱地址......" % email)
    # else:
    #     print("%s不是一个符合规范的邮箱地址*******" % email)


# <h1>hello,武汉加油</h1> 双标签
# import re
#
# # demo_data = "<h1>hello,武汉加油</h1>" # 前后必须一致 产生联系
# # print(re.match(r"<(\w*)>.*</\1>",demo_data).group())  # \1 代表第一个分组匹配到的数据必须和他一样
#
# # 分组太多
# demo_data = "<h1>hello,武汉加油</h1>" # 前后必须一致 产生联系
# print(re.match(r"<(?P<p1>\w*)>.*</(?P=p1)>",demo_data).group())  # \1 代表第一个分组匹配到的数据必须和他一样
#









































































