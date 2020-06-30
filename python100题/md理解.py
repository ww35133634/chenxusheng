# 56. 题目：输入一个奇数，然后判断最少几个 9 除以该数的结果为整数。

# x = int(input("请输入一个奇数："))
# for i in range(1, 100):
#     if int("9"*i) % x == 0:
#         print(int("9"*i))
#         break
# else:
#     print("no way")

# x = int(input("请输入一个奇数："))
# i = 1
# while True:
#     if int("9" * i) % x == 0:
#         print(int("9"*i))
#         break
#     i += 1

# 55. 题目：求0—7所能组成的奇数个数。
# q = 0
# for i in range(1, 8):
#     for j in range(8):
#         for k in range(8):
#             for l in range(8):
#                 for m in range(8):
#                     for n in range(8):
#                         for o in range(8):
#                             for p in range(1, 8, 2):
#                                 q += 1
# print(q)
#
# s = 0
# for i in range(0, 8):
#     if i == 0:
#         s = 4
#     elif i == 7:
#         s *= 7
#     else:
#         s *= 8
# print(s)
