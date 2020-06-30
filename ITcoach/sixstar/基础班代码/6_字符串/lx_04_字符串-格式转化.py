"""
演示字符串的格式转化
"""

"""
strip(占位符)		去掉字符串左右两侧的指定占位字符
lstrip(占位符)		去掉字符串左侧指定占位符
rstrip(占位符)		去掉字符串右侧指定占位符

ljust(长度,占位符)	左边占位在右侧补占位符
rjust(长度,占位符)	右边占位在左侧补占位符
center(长度,占位符)	两侧补占位符

"""

str1 = 'hello,武汉加油'
print(len(str1))

# left  原有的字符串左移,
# print(str1.ljust(15, "*"))  #

# right 原有的字符串右移
# print(str1.rjust(15, "*"))

# center(长度,占位符)	两侧补占位符  中心
print(str1.center(15, "*"))  # 5个  2个半 优先左边给一个


# str1 = '***hello,武汉加油***'
# 去掉字符串左右两侧的指定占位字符
# print(str1.strip('*'))
#
# # left 去掉字符串左侧指定占位符
# print(str1.lstrip('*'))
#
# # right 右边 去掉字符串右侧指定占位符
# print(str1.rstrip("*"))




























































