"""
演示匹配开头和结尾
"""

# 判断一个变量名是否是符合标识符规范的变量名
# 并不能规范他的结尾.....
# import re
# while True:
#     name = input('请输入一个变量名:')
#     data = re.match('[a-zA-Z_][a-zA-Z0-9_]*', name)
#     if data:
#         print('%s是一个符合规范的变量名......' % name)
#         print(data.group())
#     else:
#         print('%s不是一个符合规范的变量名******' % name)



"""
如何规范结尾部分
match的特点,,,从头开始匹配(自动匹配开头)
匹配到能匹配的部分
结尾如何匹配
"""
# 取出关键字
import keyword

print(keyword.kwlist)
import re
while True:
    name = input('请输入一个变量名:')
    #              匹配开头                 匹配结尾
    data = re.match('^[a-zA-Z_][a-zA-Z0-9_]*$', name)
    if data:
        print('%s是一个符合规范的变量名......' % name)
        print(data.group())
    else:
        print('%s不是一个符合规范的变量名******' % name)

