"""
演示异常处理方案三
"""


print("程序开始了")

try:
    i = '我可能会出问题'
    print(i)
    print(a)
    print('程序没有出现问题') #

except: # 对try里面的代码运行失败的总结
    print('六星教育帮助你')
else:# 当做是对try里面的代码运行成功的总结
    print('程序没有出现问题') #
finally:
    print("我一定会执行")
print('程序结束')

# try 有可能引发风险






























