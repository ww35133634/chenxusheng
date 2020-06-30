"""
演示匹配分组
"""
# 要求匹配qq邮箱 5 - 12位的 qq @  qq 不区分大小
# import re
# while True:
#     email_ = input('请输入一个QQ邮箱:')
#     data = re.match(r'^\d{5,12}@[qQ]{2}\.com$',email_)  # \转义 让.真的是. 不是匹配任意字符
#     if data:  # 如果匹配成功,那么data为True
#         print('%s是一个符合规范的QQ邮箱地址......' % email_)
#     else:
#         print('%s不是一个符合规范的QQ邮箱地址******' % email_)


"""
163 和qq 邮箱都想拿到
"""

# import re
# while True:
#     email_ = input('请输入一个邮箱地址:')    # 分组内部 二选一 你或者是我
#     data = re.match(r'^[a-zA-Z0-9_]{4,13}@([qQ]{2}|163)\.com$',email_)  # \转义 让.真的是. 不是匹配任意字符
#     # data = re.match(r'^[a-zA-Z0-9_]{4,13}@[qQ]{2}|163\.com$',email_)  # \转义 让.真的是. 不是匹配任意字符
#
#     if data:  # 如果匹配成功,那么data为True
#         print('%s是一个符合规范的邮箱地址......' % email_)
#     else:
#         print('%s不是一个符合规范的邮箱地址******' % email_)



# import re
# # () 分组
# email_ = input('请输入一个邮箱地址:')    # 分组内部 二选一 你或者是我
# data = re.match(r'^[a-zA-Z0-9_]{4,13}@([qQ]{2}|163)\.com$',email_)
# print(data.group())
#
# print(data.group(1))  # 用来提取分组里面的单独的数据






























































