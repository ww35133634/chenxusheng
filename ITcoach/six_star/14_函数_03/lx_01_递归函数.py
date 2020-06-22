"""
演示递归函数
"""
# a()
#
#
# def b():
#     pass
#
# # 函数内部调用自己本身的情况,
# def a():
#

# i += 1 if i <= 100
# 设计一个函数,来完成1到指定数字的求和,,
# def sum0(i):
#     if i == 1:
#         return 1
#     return sum0(i-1) + i # sum0(99) + 100
#
# # sum0(100) # 1 到100的求和结果 sum0(99) + 100
# # sum0(99)# 1 到99的求和结果    sum0(98) + 99
# # sum0(98)# 1 到98的求和结果    sum0(97 ) + 98
# # sum0(1) # 1


#
# i = sum0(100)
# print(i)
# sum0(100) # 1 到100的求和结果 sum0(99) + 100
# sum0(99)# 1 到99的求和结果    sum0(98) + 99
# sum0(98)# 1到98的求和结果    sum0(97 ) + 98
# sum0(1) # 1
# i = sum0(100)

def sum0(i): # 10 9  8 7
    if i == 1:  # 10 + 9 + 8 + 7 +6+....+ 1 # 结束调用自身函数的条件
        return 1
    return sum0(i-1) + i

i = sum0(10)
print(i)



# 调用层数的问题,,只支持1000层一下的调用



# 案列 斐波那契数列

# 普通函数逻辑得到斐波那契数列
#(0) 1 1 2 3 5 8 13 21 .......

# def feibo(i):
#     list1 = [0,1]
#     if i <= 1:
#         return list1[1]
#     for i in range(2,i+1):
#         list1.append(list1[i-1]+list1[i-2])
#     return list1[i]
#
# print(feibo(1))
# print(feibo(2))
# print(feibo(3))
# print(feibo(4))
# print(feibo(5))
# print(feibo(6))

# 1 1 2 3 5 8 13 21
# 使用递归去得到斐波那契额数列的具体值
# def feibo(i):
#     if i == 1:
#         return 1
#     if i == 2:
#         return 1
#     return feibo(i-1)+feibo(i-2)
#
# print(feibo(1))
# print(feibo(2))
# print(feibo(3))
# print(feibo(4))
# print(feibo(5))




