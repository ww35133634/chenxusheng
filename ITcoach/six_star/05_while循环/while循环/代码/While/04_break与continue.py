"""
演示break和continue
break: 终止循环
continue: 提前结束本轮循环
"""

# 小刘, 10遍班规,

# i = 1
# while i <= 10:
#     print("小刘抄写了第%s遍班规" % i)
#     i += 1
# print("行了,,去教室吧..")


# 抄完5 学习 不用抄了 直接回到教室 break终止  if判断语句
# i = 1
# while i <= 10:
#     print("小刘抄写了第%s遍班规" % i)
#
#     if i == 5:
#         break
#     i += 1
# print("行了,,去教室吧..")



# 12345678 刚刚开始抄第九遍的时候 不用抄了  直接抄10遍,,continue  if判断语句,,
# i = 0
# while i < 10:
#     i += 1
#     if i == 9:
#         continue
#     print("小刘抄写了第%s遍班规" % i)
# print("行了,,去教室吧..")


# 1-10所有的奇数,,偶数我们不数直接跳过
i = 0
while i < 10:

    i += 1
    if i % 2 == 0:
        continue

    print(i)





