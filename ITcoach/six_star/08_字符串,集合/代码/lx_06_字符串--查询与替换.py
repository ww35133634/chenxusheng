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

str1 = "hello world, hello python"
#find(字符串, 开始索引, 结束索引)	查询
# print(str1.find("o",5))
# print(str1.rfind("o")) # r >> 右边

# index find 功能一样,,,通过字符去找到他的索引值
# find 如果没有找到指定字符 会返回 -1
# index 如果没有找到指定字符 会报错
# print(str1.find("a"))
# print(str1.index("a"))

# 替换replace(原字符, 新字符, 替换数量)	替换
str1 = "hello world, hello python"
print(str1.replace("o","O",2))



