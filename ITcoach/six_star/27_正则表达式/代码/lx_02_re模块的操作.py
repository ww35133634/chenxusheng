"""
演示re模块
"""
# import re
#
# demo_data = re.match("正则表达式","要被匹配处理的字符串")
# demo_data.group()

import re

# 正则满足条件提取数据成功,返回值 是一个对象,    不满足,, None 空
demo_data = re.match(r"hi","hello, 武汉加油")
print(demo_data) # 有对象则意味着正则表达式提取数据成功
































































