"""
演示if的嵌套
"""
# csdn
# 俄罗斯套娃  一个娃娃里面有另外一个娃娃
# if 语句里面有if

# 输入得到两个数字,首先判断哪个数字更大,,再判断较大值是否是偶数,,将结果格式化输出
a = int(input('请输入第一个数字:'))
b = int(input('请输入第二个数字:'))

if a > b:  # a为较大值
    if (a % 2) == 0:  # a为偶数
        print('%s是一个偶数' % a)
    else:  # a为奇数
        print('%s是一个奇数' % a)
elif a == b:
    if (b % 2) == 0:  # a为偶数
        print('%s是一个偶数' % b)
    else:  # a为奇数
        print('%s是一个奇数' % b)
else:  # b为较大值的情况
    if (b % 2) == 0:  # a为偶数
        print('%s是一个偶数' % b)
    else:  # a为奇数
        print('%s是一个奇数' % b)






















































