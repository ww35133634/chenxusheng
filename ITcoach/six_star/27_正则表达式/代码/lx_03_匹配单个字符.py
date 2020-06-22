"""
演示匹配单个字符
"""

import re
"""
哈利波特1234567 abcd
"""
# print(re.match(r"哈利波特\d","哈利波特1"))
# demo_data = re.match(r"哈利波特\d","哈利波特8")
# demo_data = re.match(r"哈利波特[1-7]","哈利波特8")
# demo_data = re.match(r"哈利波特[a-d1-7A-Z]","哈利波特b")
# demo_data = re.match(r"哈利波特\w","哈利波特帅") # 符合unicode 很少去使用
demo_data = re.match(r"哈利波特.","哈利波特#")
print(demo_data.group())


# re.match(r"","哈利波特2")
# re.match(r"","哈利波特3")
# re.match(r"","哈利波特4")
# re.match(r"","哈利波特5")
# re.match(r"","哈利波特6")
# re.match(r"","哈利波特7")








































