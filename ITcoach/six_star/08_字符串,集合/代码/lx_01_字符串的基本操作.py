# """
# 字符串的基本操作的演示
# """
#
# str1 = "hello,武汉加油, hello,热干面加油"
#
# #长度len
# # print("使用len查看字符串的长度是:",len(str1))
#
# # 使用[]索引拿数据
# # print(str1[6])
#
# #根据数据是得到他的首次索引值
# # print(str1.index("武"))
#
# # 使用 count得到数据在该容器中的总数量
# # print(str1.count("l"))
#
# str1 = "hello,武汉加油, hello,热干面加油"
# # 判断该数据是否存在于字符串当中
# # if "长沙" in str1:
# #     print("存在")
# # else:
# #     print("不存在")
# # if "武汉" not in str1:
# #     print("正确的")
# # else:
# #     print("错误的")
#
# # 字符表,,,
# str1 = "hello,hello,"
#
# print(max(str1))
#
# print(min(str1))

#变量名.index(数据,开始索引,结束索引)
#获取数据在容器中指定范围内首次出现的索引值
str1 = "hello,武汉加油,hello,world"
print(str1.index("o",5,20))

