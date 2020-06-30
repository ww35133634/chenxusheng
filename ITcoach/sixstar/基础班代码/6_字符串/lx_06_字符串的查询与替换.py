"""
演示字符串的查询与替换
"""

"""
find(字符串, 开始索引, 结束索引)	查询
rfind(字符串, 开始索引, 结束索引)	右侧查询
index(字符串, 开始索引, 结束索引)	查询
rindex(字符串, 开始索引, 结束索引)	右侧查询
replace(原字符, 新字符, 替换数量)	替换
expandtabs()					\t替换空格
"""

#       01234567891011      21
str1 = 'hello python, hello world'
# 根据数据拿到他的索引值
# print(str1.find('o'))  # 默认从索引0开始寻找 找到一个就满足了
# print(str1.find('a',5,11))

# right 从右边开始
# print(str1.rfind('o'))  # 默认从右边开始 找到一个就满足了

# index 就是找不到就发脾气 就报错,  find -1
# index(字符串, 开始索引, 结束索引)
# rindex(字符串, 开始索引, 结束索引)


# replace(原字符, 新字符, 替换数量)	替换 正则也有会替换
str1 = 'hello python, hello world'
# print(str1.replace('o','O'))  # 默认全部替换
print(str1.replace('o','O',-2))


#  expandtabs()			\t替换空格

































#
# print(str1.find('a'))  # 不存在 得到-1
# print(str1.index('a'))  # 不存在 报错 异常处理的东西




















































































































































































