"""
演示匹配单个字符
"""

import re

# 系列电影的名称  哈利波特1-7
#       正则表达式 , 要被匹配的字符串
# re.match(r'哈利波特1', '哈利波特1')
# re.match(r'哈利波特2', '哈利波特2')
# re.match(r'哈利波特3', '哈利波特3')
# re.match(r'哈利波特4', '哈利波特4')
# re.match(r'哈利波特5', '哈利波特5')
# re.match(r'哈利波特6', '哈利波特6')
# re.match(r'哈利波特7', '哈利波特7')

# 匹配单个字符, \d 用来单个一个数字字符 整数
#
# data = re.match(r'哈利波特\d', '哈利波特2')
#
# print(data.group())  # 利用对象的group方法拿到匹配成功的数据


# 不合理的情况
#                       # 匹配单个数字
# data = re.match(r'哈利波特\d', '哈利波特11')
#
# print(data.group())  # 利用对象的group方法拿到匹配成功的数据


# 1234567                    并不存在   也不合理
# data = re.match(r'哈利波特\d', '哈利波特8')
#
# print(data.group())  # 利用对象的group方法拿到匹配成功的数据




# \d 0-9   [] >>> 只会匹配其中列举出来的一个字符
# 哈利波特1234567    哈利波特8
# data = re.match(r'哈利波特[1234567]', '哈利波特8')
#
# print(data.group())  # 利用对象的group方法拿到匹配成功的数据

#  类似连续的数字,, [1234567] 简写成[1-7]
# data = re.match(r'哈利波特[1-7]', '哈利波特3')
#
# print(data.group())  # 利用对象的group方法拿到匹配成功的数据


# 哈利波特 1 -11  匹配多个字符再去讲
# data = re.match(r'哈利波特\d\d', '哈利波特11')
#
# print(data.group())  # 利用对象的group方法拿到匹配成功的数据



# 哈利波特a  哈利波特b 哈利波特c  哈利波特d
# data = re.match(r'哈利波特[abcd]', '哈利波特a')
# data = re.match(r'哈利波特[a-d]', '哈利波特c')
#
# print(data.group())  # 利用对象的group方法拿到匹配成功的数据





# 所有的大写字母  小写字母 数字  只会取一个 单个字符的匹配
#
# data = re.match(r'哈利波特[A-Za-z0-9]', '哈利波特B')
#
# print(data.group())  # 利用对象的group方法拿到匹配成功的数据


"""
单个字符
\d 单个整型
[] 单个里面列举的字符
\w	匹配单词字符, 即a-z,A-Z,0-9,_ 中文也可以匹配成功   字母和数字 中文 不常用....不精确
"""

# data = re.match(r'哈利波特\w', '哈利波特帅')
#
# print(data.group())  # 利用对象的group方法拿到匹配成功的数据

"""
.  匹配任意1个字符(除了\n之外)

"""
#                   任意单个字符
data = re.match(r'哈利波特.', '哈利波特%')

print(data.group())  # 利用对象的group方法拿到匹配成功的数据