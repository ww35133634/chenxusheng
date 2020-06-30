"""
演示字符串的判断 is
"""

# str1 = 'hello,武汉加油,hello,周黑鸭加油'
# str1 = 'Abc拉拉'

# 判断是否是大写, 为真True  为假False
# print(str1.isupper())  # 其实并不是很准确 正则
#
# # 判断是否所有字母都是小写  并不是完全对立,,
# print(str1.islower())

str1 = 'Abc123哈哈'
# 判断是否都是字母
# print(str1.isalpha())  # 并不是很精准, 正则

# 判断是否由数字或字母组成
# print(str1.isalnum())  #


# str1 = 'ABC'  # 编码格式把中文归为了字母
# 判断是否都是数字
# print(str1.isdigit())  # 判断出来中文
# str1 = 'Title '
# # 判断首字母是否是大写
# print(str1.istitle())


str1 = 'hello,武汉加油,hello,周黑鸭加油'
"""
startwith(字符串)		是否指定字符开始
endswith(字符串)		是否指定字符结束
"""

# print(str1.startswith('hella'))
#
# print(str1.endswith('周黑鸭'))



#                 8 9  12           20
str1 = 'hello,武汉加油,hello,周黑鸭加油'
#                    代表从索引9的位置开始去寻找
print(str1.index('加', 9))  # 默认从0开始去寻找,找到一个就停止,,默认找到最后(0,-1)




































